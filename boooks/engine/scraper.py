#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import requests
from lxml import html as lhtml

book_url = 'https://www.goodreads.com/book/show/11284898-the-storyteller?ref=ru_lihp_nsup_binrsh_0_mclk-exp65cell142-nup1047455667'


class Page(object):
    def __init__(self, url):
        self.url = url

    def retrieve(self):
        response = requests.get(self.url)
        dom = lhtml.fromstring(response.content)
        return self.parse_data(dom)

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
        return data


class GenresRootPage(RootPage):
    url = 'https://www.goodreads.com/genres/list'

    def parse_data(self, dom):
        results = []

        for stat in dom.xpath('//div[@class="shelfStat"]'):
            link = stat.cssselect('.actionLinkLite')[0]
            total_books = stat.cssselect('.greyText')[0]
            data = {
                'name': link.text.strip(),
                'link': link.attrib['href'],
                'total_books': int(total_books.text.replace('books', '').strip().replace(',', ''))
            }
            results.append(data)

        return results


def main():
    #book = BookPage(book_url).retrieve()
    genres = GenresRootPage().retrieve()
    # print book
    print genres


if __name__ == '__main__':
    main()
