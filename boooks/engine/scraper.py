#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import requests
import logging
from lxml import html as lhtml

book_url = 'https://www.goodreads.com/book/show/11284898-the-storyteller?ref=ru_lihp_nsup_binrsh_0_mclk-exp65cell142-nup1047455667'
logger = logging.getLogger('boooks.engine.scraper')


def ensure_full_link(link):
    if link.startswith('/'):
        return 'https://www.goodreads.com{0}'.format(link)
    elif link.startswith('http'):
        return link
    else:
        raise RuntimeError('got an unexpected url: {0}'.format(link))


class Page(object):
    def __init__(self, url):
        self.url = ensure_full_link(url)

    def retrieve(self):
        logger.debug('[BEGIN] %s.parse_data %s', self.__class__.__name__, self.url)

        response = requests.get(self.url)
        logger.debug('[REQUESTED] %s.parse_data %s', self.__class__.__name__, self.url)

        dom = lhtml.fromstring(response.content)
        logger.debug('[PARSING] %s.parse_data %s', self.__class__.__name__, self.url)

        result = self.parse_data(dom)
        logger.debug('[FINISHED] %s.parse_data %s', self.__class__.__name__, self.url)

        return result

    def parse_data(self, dom):
        raise NotImplementedError()


class RootPage(Page):
    def __init__(self):
        pass


class BookPage(Page):
    def parse_data(self, dom):
        keys = dom.xpath('//div[@id="bookDataBox"]//div[@class="infoBoxRowTitle"]/text()')
        values = dom.xpath('//div[@id="bookDataBox"]//div[@class="infoBoxRowItem"]/text()')
        keys = [k.lower().strip() for k in keys]
        values = [v.strip() for v in values]
        data = dict(zip(keys, values))
        data['type'] = 'book'
        return data


class GenresRootPage(RootPage):
    url = 'https://www.goodreads.com/genres/list'

    def parse_data(self, dom):
        results = []

        for stat in dom.xpath('//div[@class="shelfStat"]'):
            link = stat.cssselect('.actionLinkLite')[0]
            total_books = stat.cssselect('.greyText')[0]
            href = link.attrib['href']
            data = {
                'type': 'book_genre_page',
                'name': link.text.strip(),
                'link': href,
                'total_books': int(total_books.text.replace('books', '').strip().replace(',', '')),
                'page': BookCoverListPage(href)
            }
            results.append(data)

        return results


class BookCoverListPage(Page):
    def parse_data(self, dom):
        next_page_links = dom.xpath('//a[contains(@href, "shelf/show")]/@href')
        results = []
        for p in next_page_links:
            results.extend(PaginatedBookListPage(p).retrieve())

        return results


class PaginatedBookListPage(Page):
    def parse_data(self, dom):
        links = dom.xpath('//a[contains(@class, "bookTitle")]/@href')
        next_page_links = dom.xpath('//a[contains(@class, "next_page")]/@href')
        if next_page_links:
            next_page = self.__class__(next_page_links[0])
            links.extend(next_page.retrieve())

        return links


def main():
    # book = BookPage(book_url).retrieve()
    genres = GenresRootPage().retrieve()
    book_links = []
    for g in genres:
        book_links.extend(g['page'].retrieve())
        logger.info("%s books found so far", len(book_links))

    book_pages = [BookPage(u) for u in book_links]
    import ipdb;ipdb.set_trace()



if __name__ == '__main__':
    import coloredlogs
    coloredlogs.install(level=logging.DEBUG)
    main()
