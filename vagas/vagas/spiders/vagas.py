# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:11:04 2018

@author: Rodrigo
"""
import scrapy


class VagasSpider(scrapy.Spider):
    name = "vagas"

    start_urls = [
        'https://www.vagas.com.br/vagas-de-cientista-de-dados?'
     
    ]
  
    def parse(self, response):
        for vaga in response.css('a.link-detalhes-vaga'):
            yield {
                'vaga': vaga.css('a::attr(title)').extract_first(),
                'nivel': vaga.css('span.nivelVaga::text').extract_first(),
                'empresa': vaga.css('span.emprVaga::text').extract_first(),
                'link': vaga.css('a::attr(href)').extract(),
            }
            

   
