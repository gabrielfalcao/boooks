#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from boooks.framework.db import (
    Model, db, MetaData,
    PrimaryKey,
    DefaultForeignKey
)
from boooks.framework.handy.functions import slugify


metadata = MetaData()


class Author(Model):
    table = db.Table(
        'book_author',
        metadata,
        PrimaryKey(),
        db.Column('name', db.Unicode(255)),
        db.Column('slug', db.Unicode(255)),
    )

    @classmethod
    def get_or_create_by_name(cls, name):
        slug = slugify(name)
        found = cls.get_or_create(slug=slug)
        found.name = name
        found.save()
        return found


class Book(Model):
    table = db.Table(
        'book',
        metadata,
        PrimaryKey(),
        db.Column('ASIN', db.Unicode(20)),
        db.Column('ISBN', db.Unicode(20)),
        db.Column('title', db.Unicode(255)),
        db.Column('slug', db.Unicode(255)),
        db.Column('url', db.Unicode(255)),
        db.Column('number_of_pages', db.Integer),
        db.Column('price', db.Numeric),
        db.Column('stars', db.Integer),
        db.Column('ranking', db.Integer),
        db.Column('total_reviews', db.Integer),
        DefaultForeignKey('author_id', 'book_author.id'),
    )

    @classmethod
    def get_or_create_from_dict(cls, data):
        author = Author.get_or_create_by_name(data['author'])
        cleaned = {}
        cleaned['ASIN'] = data['ASIN']
        cleaned['ISBN'] = data['ISBN']
        cleaned['url'] = data['url']
        cleaned['slug'] = slugify(data['title'])
        cleaned['title'] = data['title']
        cleaned['number_of_pages'] = data['number_of_pages']
        cleaned['price'] = (
            data.get('price', None) or
            data.get('lowest_used_price_amount', None) or
            data.get('lowest_new_price_amount', None) or '0.00'
        )

        found = cls.get_or_create(
            author_id=author.id,
            ASIN=cleaned['ASIN'])

        found.update(**cleaned)
        found.save()
        return found
