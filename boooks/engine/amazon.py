#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import os
import re
import json

import redis
from amazonproduct import API as AmazonProductApi
from lxml.objectify import StringElement, IntElement


class AmazonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (StringElement, IntElement)):
            return obj.text

        return json.JSONEncoder.default(self, obj)


def format_currency(x):
    return "${0}".format(re.sub(r'(\d{2})$', '.\g<1>', x.text))


def get_connection():
    config = {
        'access_key': os.environ['AWS_ACCESS_KEY_ID'],
        'secret_key': os.environ['AWS_SECRET_ACCESS_KEY'],
        'associate_tag': 'boooks06-20',
        'locale': 'us'
    }
    return AmazonProductApi(cfg=config)

api = get_connection()


def get_item_data(item):
    images = api.item_lookup(str(item.ASIN), ResponseGroup='Images')
    if not getattr(images.Items.Item, 'MediumImage', []):
        return

    offer = api.item_lookup(str(item.ASIN), ResponseGroup='OfferFull')
    editorial = api.item_lookup(str(item.ASIN), ResponseGroup='EditorialReview')
    attributes = api.item_lookup(str(item.ASIN), ResponseGroup='ItemAttributes')

    large = getattr(images.Items.Item, 'LargeImage', [])
    medium = getattr(images.Items.Item, 'MediumImage', [])
    small = getattr(images.Items.Item, 'SmallImage', [])

    data = {
        'asin': item.ASIN,
        'url': item.DetailPageURL,
        'author': getattr(item.ItemAttributes, 'Author', None),
        'title': item.ItemAttributes.Title,
        'images': {
            'large': len(large) and large.URL or None,
            'medium': len(medium) and medium.URL or None,
            'small': len(small) and small.URL or None,
        },
    }

    if hasattr(editorial.Items.Item, 'EditorialReviews'):
        data['review'] = editorial.Items.Item.EditorialReviews.EditorialReview.Content

    data['ISBN'] = getattr(attributes.Items.Item.ItemAttributes, 'ISBN', None)
    data['number_of_pages'] = getattr(attributes.Items.Item.ItemAttributes, 'NumberOfPages', None)

    if hasattr(offer.Items.Item, 'OfferSummary'):
        data.update({
            'total_new': offer.Items.Item.OfferSummary.TotalNew,
            'total_used': offer.Items.Item.OfferSummary.TotalUsed,
            'total_refurbished': offer.Items.Item.OfferSummary.TotalRefurbished,
        })
        if hasattr(offer.Items.Item.OfferSummary, 'LowestUsedPrice'):
            data.update({
                'lowest_used_price_amount': format_currency(offer.Items.Item.OfferSummary.LowestUsedPrice.Amount),
                'lowest_used_price_currency': offer.Items.Item.OfferSummary.LowestUsedPrice.CurrencyCode,
            })
        if hasattr(offer.Items.Item.OfferSummary, 'LowestNewPrice'):
            data.update({
                'lowest_new_price_amount': format_currency(offer.Items.Item.OfferSummary.LowestNewPrice.Amount),
                'lowest_new_price_currency': offer.Items.Item.OfferSummary.LowestNewPrice.CurrencyCode,
            })

    return data


def cache_key(keywords):
    return ":".join(['cache', keywords])


def get_from_cache(keywords):
    conn = redis.StrictRedis()
    raw = conn.get(cache_key(keywords))
    if raw:
        return json.loads(raw)


def set_in_cache(data, keywords):
    conn = redis.StrictRedis()
    conn.set(cache_key(keywords), json.dumps(data, cls=AmazonEncoder))


def search_for_books(keywords, limit=20):
    data = get_from_cache(keywords)
    if data:
        return data

    results = api.item_search('Books', Keywords=keywords, IncludeReviewsSummary=True, SearchIndex='Books', MaximumPrice='5')
    data = filter(lambda x: x, [get_item_data(x) for index, x in enumerate(results) if index < limit])
    set_in_cache(keywords, json.dumps(data, cls=AmazonEncoder))
    return data

if __name__ == '__main__':
    result = search_for_books('Jill Bolte Taylor')
    data = json.dumps(result, indent=2, cls=AmazonEncoder)
    with open("books.json", "w") as fd:
        fd.write(data)
