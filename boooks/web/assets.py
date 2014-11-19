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
from boooks.base.assets import angular
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

booksapp = Bundle('js/app*.js', filters=[JINJA_FILTER])
adminapp = Bundle('js/admin*.js', filters=[JINJA_FILTER])

angular_css = Bundle(
    'vendor/angular-loading-bar/build/loading-bar.css'
)

BUNDLES = [
    ('css-web', Bundle(angular_css, web_less,
                       output='build/boooks.css')),
    ('app-js', Bundle(angular, booksapp,
                      output='build/boooks.js')),
    ('admin-js', Bundle(angular, adminapp,
                        output='build/admin.js')),

]

for node in nodes:
    path = node.path.split("/static/js/")[-1]
    source = "/".join(["js", path])
    destination = "/".join(["build", path])
    BUNDLES.append((path, Bundle(source, output=destination)))
