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
    return "{0}".format(re.sub(r'(\d{2})$', '.\g<1>', x.text))


def get_connection():
    config = {
        'access_key': os.getenv('AWS_ACCESS_KEY_ID'),
        'secret_key': os.getenv('AWS_SECRET_ACCESS_KEY'),
        'associate_tag': 'boooks06-20',
        'locale': 'us'
    }
    return AmazonProductApi(cfg=config)

api = get_connection()

URL_CACHE = []


def get_item_data(item):
    if item.DetailPageURL in URL_CACHE:
        return

    URL_CACHE.append(item.DetailPageURL)
    large = getattr(item, 'LargeImage', [])
    medium = getattr(item, 'MediumImage', [])
    small = getattr(item, 'SmallImage', [])

    if not len(large) or not len(medium) or not len(small):
        return

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

    if hasattr(item, 'EditorialReviews'):
        data['review'] = item.EditorialReviews.EditorialReview.Content

    data['ISBN'] = getattr(item.ItemAttributes, 'ISBN', None)
    data['number_of_pages'] = getattr(item.ItemAttributes, 'NumberOfPages', None)

    if hasattr(item, 'OfferSummary'):
        data.update({
            'total_new': item.OfferSummary.TotalNew,
            'total_used': item.OfferSummary.TotalUsed,
            'total_refurbished': item.OfferSummary.TotalRefurbished,
            'price': item.Offers.Offer.OfferListing.Price.Amount,
        })

        if hasattr(item.OfferSummary, 'LowestUsedPrice'):
            data.update({
                'lowest_used_price_amount': format_currency(item.OfferSummary.LowestUsedPrice.Amount),
                'lowest_used_price_currency': item.OfferSummary.LowestUsedPrice.CurrencyCode,
            })
        if hasattr(item.OfferSummary, 'LowestNewPrice'):
            data.update({
                'lowest_new_price_amount': format_currency(item.OfferSummary.LowestNewPrice.Amount),
                'lowest_new_price_currency': item.OfferSummary.LowestNewPrice.CurrencyCode,
            })

    return data


def cache_key(keywords):
    return ":".join(['cache', keywords])


def get_from_cache(keywords):
    conn = redis.StrictRedis()
    raw = conn.get(cache_key(keywords))
    if raw:
        return json.loads(raw)


def set_in_cache(keywords, data):
    conn = redis.StrictRedis()
    conn.set(cache_key(keywords), json.dumps(data, cls=AmazonEncoder))


def search_for_books(keywords, limit=20):
    data = get_from_cache(keywords)
    if data:
        return json.loads(data)

    results = api.item_search('Books', Keywords=keywords, IncludeReviewsSummary=True, SearchIndex='Books', MaximumPrice='30', ResponseGroup='Images,OfferFull,EditorialReview,ItemAttributes')
    data = list([get_item_data(x) for index, x in enumerate(results)])

    set_in_cache(keywords, json.dumps(data, cls=AmazonEncoder))
    return data

if __name__ == '__main__':
    result = search_for_books('Jill Bolte Taylor')
    data = json.dumps(result, indent=2, cls=AmazonEncoder)
    with open("books.json", "w") as fd:
        fd.write(data)
