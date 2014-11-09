# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
import os
from flask.ext.assets import (
    Bundle,
)
from flask import url_for
from webassets.filter import get_filter

from webassets.filter.jinja2 import Jinja2
from boooks import settings
from plant import Node

static_url = lambda path: "{0}/{1}".format(
    settings.STATIC_BASE_URL.rstrip('/'),
    path.lstrip('/')
)

JINJA_FILTER = Jinja2(context={
    'settings': settings,
    'socketio_namespace': lambda name: settings.absurl(name),
    'url_for': lambda name: url_for(name),
    'image_url': lambda path: static_url("img/{0}".format(path)),
    'angular_template': lambda path: static_url("templates/{0}".format(path)),
})

os.environ['SASS_PATH'] = ":".join([
    settings.LOCAL_FILE('static/vendor/foundation/scss/'),
])

compass = get_filter('compass', config={
    'project_path': settings.LOCAL_FILE('static/scss/')
})


web_less = Bundle(
    'scss/app.scss',
    filters=(compass, ),
)

templates_node = Node(settings.LOCAL_FILE('static/js/templates'))
nodes = templates_node.find_with_regex("[.]html$")


BUNDLES = [
    ('css-web', Bundle(web_less,
                       output='build/boooks.css')),
]

for node in nodes:
    path = node.path.split("/static/js/")[-1]
    source = "/".join(["js", path])
    destination = "/".join(["build", path])
    BUNDLES.append((path, Bundle(source, output=destination)))
