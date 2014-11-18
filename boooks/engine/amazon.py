#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import os
import re
import json

import redis
from logging import getLogger
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
        'ASIN': item.ASIN,
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
            'price': hasattr(item.Offers, 'Offer') and format_currency(item.Offers.Offer.OfferListing.Price.Amount) or None,
        })

        if hasattr(item.OfferSummary, 'LowestUsedPrice') and hasattr(item.OfferSummary.LowestUsedPrice, 'Amount'):
            data.update({
                'lowest_used_price_amount': format_currency(item.OfferSummary.LowestUsedPrice.Amount),
                'lowest_used_price_currency': item.OfferSummary.LowestUsedPrice.CurrencyCode,
            })
        if hasattr(item.OfferSummary, 'LowestNewPrice') and hasattr(item.OfferSummary.LowestNewPrice, 'Amount'):
            data.update({
                'lowest_new_price_amount': format_currency(item.OfferSummary.LowestNewPrice.Amount),
                'lowest_new_price_currency': item.OfferSummary.LowestNewPrice.CurrencyCode,
            })

    return data


def cache_key(keywords, max_price):
    return ":".join(['cache', keywords, max_price])


def get_from_cache(keywords, max_price):
    conn = redis.StrictRedis()
    raw = conn.get(cache_key(keywords, max_price))
    if raw:
        return json.loads(raw)


def set_in_cache(keywords, max_price, data):
    conn = redis.StrictRedis()
    conn.set(cache_key(keywords, max_price), json.dumps(data, cls=AmazonEncoder))


logger = getLogger()


def filter_by_reading_time(books, max_pages):
    if max_pages is None:
        return books
    else:
        return [d for d in books if int(d['number_of_pages'] or 0) < int(max_pages)]


def search_for_books(keywords, max_price='30', max_pages=None, limit=20):
    logger.info('keywords %s max_price %s', keywords, max_price)
    data = get_from_cache(keywords, max_price)
    if data:
        return filter_by_reading_time(json.loads(data), max_pages)

    results = api.item_search(
        'Books',
        Keywords=keywords,
        IncludeReviewsSummary=True,
        SearchIndex='Books',
        MaximumPrice=max_price,
        Sort='reviewrank',
        ResponseGroup=','.join([
            'Images',
            'OfferFull',
            'EditorialReview',
            'ItemAttributes',
        ])
    )
    data = filter(lambda x: x, [get_item_data(x) for index, x in enumerate(results)])

    set_in_cache(keywords, max_price, json.dumps(data, cls=AmazonEncoder))
    return filter_by_reading_time(data, max_pages)

if __name__ == '__main__':
    result = search_for_books('Jill Bolte Taylor')
    data = json.dumps(result, indent=2, cls=AmazonEncoder)
    with open("books.json", "w") as fd:
        fd.write(data)
