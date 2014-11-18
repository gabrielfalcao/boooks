#!/usr/bin/env python
# -*- coding: utf-8 -*-

from boooks.framework.db import (
    Model, db, MetaData,
    PrimaryKey,
    DefaultForeignKey
)
from boooks.framework.handy.functions import slugify


metadata = MetaData()


class SlugModel(Model):
    @classmethod
    def get_or_create_from_name(cls, name):
        name = unicode(name)
        slug = slugify(name)
        found = cls.get_or_create(slug=slug)
        found.name = name
        found.save()
        return found


class Author(SlugModel):
    table = db.Table(
        'book_author',
        metadata,
        PrimaryKey(),
        db.Column('name', db.Unicode(255)),
        db.Column('slug', db.Unicode(255)),
    )


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
        author = Author.get_or_create_from_name(data['author'])
        cleaned = {}
        cleaned['ASIN'] = unicode(data['ASIN'])
        cleaned['ISBN'] = unicode(data['ISBN'])
        cleaned['url'] = unicode(data['url'])
        cleaned['slug'] = slugify(data['title'])
        cleaned['title'] = unicode(data['title'])
        cleaned['number_of_pages'] = unicode(data['number_of_pages'])
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


class SearchCategory(SlugModel):
    table = db.Table(
        'search_category',
        metadata,
        PrimaryKey(),
        db.Column('name', db.Unicode(20)),
        db.Column('slug', db.Unicode(20)),
    )

    def get_keywords(self):
        return CategoryKeywords.find_by(search_category_id=self.id)


class SearchNiche(SlugModel):
    table = db.Table(
        'search_niche',
        metadata,
        PrimaryKey(),
        db.Column('name', db.Unicode(20)),
        db.Column('slug', db.Unicode(20)),
    )


class CategoryKeywords(Model):
    table = db.Table(
        'search_keywords',
        metadata,
        PrimaryKey(),
        DefaultForeignKey('search_niche_id', 'search_niche.id', nullable=True),
        DefaultForeignKey('search_category_id', 'search_category.id', nullable=True),
        db.Column('keywords', db.Unicode(255)),
    )

    def to_dict(self):
        data = self.serialize()
        data['category'] = self.category and self.category.to_dict() or None
        data['niche'] = self.niche and self.niche.to_dict() or None
        return data

    @classmethod
    def create_missing(cls):
        for category in SearchCategory.all():
            found = cls.get_or_create(
                search_category_id=category.id,
            )
            if not found.keywords:
                found.keywords = category.name
                found.save()

            for niche in SearchNiche.all():
                found = cls.get_or_create(
                    search_niche_id=niche.id,
                )
                if not found.keywords:
                    found.keywords = niche.name
                    found.save()

                found = cls.get_or_create(
                    search_category_id=category.id,
                    search_niche_id=niche.id,
                )
                if not found.keywords:
                    found.keywords = ' + '.join([niche.name, category.name])
                    found.save()

    @property
    def category(self):
        return SearchCategory.find_one_by(id=self.search_category_id)

    @property
    def niche(self):
        return SearchNiche.find_one_by(id=self.search_niche_id)
