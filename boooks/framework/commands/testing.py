#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
from __future__ import unicode_literals

"""
boooks.commands.testing
~~~~~~~~~~~~~~~~~~~~~~

Contains commands for running tests in the local environment
"""
import os
import re
import sys
import subprocess
from flask.ext.script import Command, Option


def slugify(string):
    return re.sub(r'\W+', '-', string)


class RunTest(Command):  # pragma: no cover
    """Runs tests"""
    option_list = (
        Option('filenames', nargs='*'),
    )

    def __init__(self, kind):
        self.kind = kind
        self.module_name = 'tests.{0}'.format(self.kind)

    def get_arguments(self):
        args = [
            '--immediate',
            '--with-coverage',
            '--cover-min-percentage=100%',
            '--cover-erase',
            '--cover-package=boooks.api',
            '--cover-package=boooks.mail',
            '--cover-package=boooks.security',
            '--cover-package=boooks.framework',
            '--rednose',
            '--stop',
            '--s',
            '--verbosity=2',
        ]
        if self.kind == 'unit':
            args.insert(2, '--cover-branches')

        return args

    def run(self, filenames):
        os.environ['TESTING'] = 'true'
        if self.kind == 'unit':
            os.environ['UNIT_TESTING'] = 'true'

        print "Scanning for {0} tests".format(self.kind)

        base_args = self.get_arguments()
        if filenames:
            args = base_args + filenames
        else:
            args = base_args + ['tests/{0}'.format(self.kind)]

        code = subprocess.call(['nosetests'] + args)
        sys.exit(code)
