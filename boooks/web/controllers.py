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
    JSONNotFound,
    JSONException,
    JSONResource,
)

from boooks import settings
from boooks.framework.handy.functions import get_ip

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
    search_for_books('Popular')
    return render_template('index.html')


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
        result = search_for_books('Popular')
        return json_response(result, 200)


class SearchResource(ApiResource):
    def post(self):
        data = self.parse_json_fields([
            'keywords',
        ])

        books = search_for_books(keywords=data['keywords'].strip())

        return json_response(books, 200)


ENDPOINTS = [
    # index
    (IndexResource, '/api/index'),
    # search
    (SearchResource, '/api/search'),
]


for Resource, endpoint in ENDPOINTS:
    api.add_resource(Resource, endpoint)
