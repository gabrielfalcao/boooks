#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2013 Gabriel Falcão <gabriel@boooks.com>
#
from __future__ import unicode_literals
import time
import json
import logging
from collections import defaultdict
from boooks.framework.http import (
    Api,
    json_response,
    JSONException,
    JSONResource,
)

from boooks import settings
from boooks.web.models import Book, SearchCategory, SearchNiche, CategoryKeywords
from flask import (
    Blueprint,
    render_template,
    request,
    session,
    url_for,
)


module = Blueprint('web', __name__)
api = Api(module)
logger = logging.getLogger('boooks.web')


@module.context_processor
def inject_basics():
    return dict(
        settings=settings,
        messages=session.pop('messages', []),
        github_user=session.get('github_user_data', None),
        json=json,
        len=len,
        full_url_for=lambda *args, **kw: settings.absurl(
            url_for(*args, **kw)
        ),
        ssl_full_url_for=lambda *args, **kw: settings.sslabsurl(
            url_for(*args, **kw)
        ),
        static_url=lambda path: "{0}/{1}?{2}".format(
            settings.STATIC_BASE_URL.rstrip('/'),
            path.lstrip('/'),
            time.time()
        ),
    )


@module.route('/')
def index():
    search_for_books('Best Seller')
    labeled_niches = json.dumps([{'value': n.id, 'label': n.name} for n in SearchNiche.all()])
    labeled_categories = json.dumps([{'value': n.id, 'label': n.name} for n in SearchCategory.all()])
    return render_template('index.html', niches=labeled_niches, categories=labeled_categories)


@module.route('/admin')
def admin():
    return render_template('admin.html')


@module.route('/reading-lists')
def reading_lists():
    return render_template('reading_lists.html')


class RawJSONError(JSONException):
    def __init__(self, errors, status_code=400):
        self.errors = errors
        self.status_code = status_code

    def __str__(self):
        return json.dumps(self.errors)

    def as_dict(self):
        return self.errors


class ApiResource(JSONResource):
    not_found_msg = "Could not find {0} with kwargs {1}"

    def get_json_request(self):
        try:
            data = json.loads(request.data)
        except ValueError:
            logger.exception(
                "Trying to parse json body in the %s to %s",
                request.method, request.url,
            )
            data = {}

        return data

    def parse_json_fields(
            self, fields, validate=True, failure_status_code=400):

        result = {}
        data = self.get_json_request()
        errors = defaultdict(list)

        for field in fields:
            value = data.get(field)
            if validate and value is None:
                errors[field].append('This field is required.')
            elif value is not None:
                result[field] = value

        if errors:
            raise RawJSONError({'errors': errors}, failure_status_code)

        return result

from boooks.engine.amazon import search_for_books


class IndexResource(ApiResource):
    def get(self):
        result = search_for_books('Best Seller')
        return json_response(result, 200)


class SearchResource(ApiResource):
    def post(self):
        data = self.parse_json_fields([
            'niche_id',
            'category_id',
            'max_price',
            'max_pages',
        ])

        niche_id = data.pop('niche_id')
        category_id = data.pop('category_id')

        keywords = CategoryKeywords.find_one_by(
            search_niche_id=niche_id,
            search_category_id=category_id
        )

        data['keywords'] = keywords.keywords
        logger.info('searching for %s', keywords.keywords)
        books = search_for_books(**data)

        return json_response(books, 200)


class AdminListCategories(ApiResource):
    def get(self):
        categories = [c.to_dict() for c in SearchCategory.all()]
        return json_response(categories, 200)

    def post(self):
        data = self.parse_json_fields([
            'name',
        ])
        result = SearchCategory.get_or_create_from_name(data['name'])
        CategoryKeywords.create_missing()
        return json_response(result.to_dict(), 200)


class AdminListNiches(ApiResource):
    def get(self):
        niches = [n.to_dict() for n in SearchNiche.all()]
        return json_response(niches, 200)

    def post(self):
        data = self.parse_json_fields([
            'name',
        ])
        result = SearchNiche.get_or_create_from_name(data['name'])
        CategoryKeywords.create_missing()
        return json_response(result.to_dict(), 200)


class AdminNiches(ApiResource):
    def delete(self, id):
        result = SearchNiche.find_one_by(id=id)
        result.delete()
        return json_response(result.to_dict(), 200)


class AdminCategories(ApiResource):
    def delete(self, id):
        result = SearchCategory.find_one_by(id=id)
        result.delete()
        return json_response(result.to_dict(), 200)


class AdminKeywords(ApiResource):
    def get(self):
        results = CategoryKeywords.all()
        return json_response([c.to_dict() for c in results], 200)

    def post(self):
        data = self.parse_json_fields([
            'possibilities',
        ])
        possibilities = data['possibilities']
        results = []
        for p in possibilities:
            r = CategoryKeywords.get_or_create(
                search_niche_id=p['niche']['id'],
                search_category_id=p['category']['id'],
            )
            keywords = p.get('keywords', '') or ''
            r.update(keywords=keywords)
            r.save()

            results.append(r.to_dict())

        return json_response(results, 200)


ENDPOINTS = [
    # index
    (IndexResource, '/api/index'),
    # search
    (SearchResource, '/api/search'),
    # admin niches
    (AdminListNiches, '/api/niches'),
    (AdminListCategories, '/api/categories'),
    (AdminNiches, '/api/niche/<int:id>'),
    (AdminCategories, '/api/category/<int:id>'),
    (AdminKeywords, '/api/keywords'),
]


for Resource, endpoint in ENDPOINTS:
    api.add_resource(Resource, endpoint)
