# -*- coding: utf-8 -*-
import scrapy


class VagasSpider(scrapy.Spider):
    name = 'vagas'
    allowed_domains = ['vagas.com']
    start_urls = ['http://vagas.com/']

    def parse(self, response):
        pass
