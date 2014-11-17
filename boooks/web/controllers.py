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
    search_for_books('Featured')
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

    def send_email(self, item):  # pragma: no cover
        from propellr.api.tasks import send_email_in_background
        return send_email_in_background.delay(item)

    @property
    def limit_by(self):
        limit = request.args.get('limit', None)
        if limit:
            return int(limit)

        return

    @property
    def offset_by(self):
        offset = request.args.get('offset', 0)
        if offset:
            return int(offset)

        return

    def get_user_dict(self, user):
        data = user.to_dict()
        data['first_name'] = None
        data['last_name'] = None
        data['investor_profile_status'] = INVESTOR_PROFILE_STATUS.INCOMPLETE

        user_info = user.info
        if user_info:
            data['first_name'] = user_info.first_name
            data['last_name'] = user_info.last_name
            data['investor_profile_status'] = user_info.investor_profile_status

        return data

    def get_model_or_404(self, model_class, **kw):
        result = model_class.find_one_by(**kw)
        if not result:
            msg = self.not_found_msg.format(model_class.__name__, kw)
            raise JSONNotFound(msg)

        return result

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

    def log(self, user_id, action_name, result_name):
        if settings.TESTING:
            return

        fmt = "{ip_address} [{method}] url: {url} - uid: %s - %s - %s".format(
            ip_address=get_ip(),
            method=request.method,
            url=request.url,
        )

        logger.info(fmt, user_id, action_name, result_name)

from boooks.engine.amazon import search_for_books


class IndexResource(ApiResource):
    def get(self):
        result = search_for_books('Featured')
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
