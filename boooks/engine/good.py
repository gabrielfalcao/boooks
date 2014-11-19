#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
from Goodreads.goodreads import Goodreads
from boooks.settings import GOODREADS_KEY, GOODREADS_SECRET


goodreads = Goodreads(GOODREADS_KEY, GOODREADS_SECRET)
