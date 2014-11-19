#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# flake8: noqa

from __future__ import unicode_literals

from flask.ext.assets import (
    Bundle,
)

jquery = Bundle('vendor/jquery/jquery.js')
angular = Bundle(
    'vendor/angularjs/angular.js',
    'vendor/angular-ui-router/release/angular-ui-router.js',
    'vendor/angular-local-storage/angular-local-storage.js',
    'vendor/angular-natural-language/build/angular-natural-language.js'
)

bootstrap_js = Bundle(
    "vendor/bootstrap/dist/js/bootstrap.js"
)

bootstrap_css = Bundle(
    "vendor/bootswatch/lumen/bootstrap.css",
)
