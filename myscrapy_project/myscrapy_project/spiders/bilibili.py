# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
# from ArticleSpider.items import TutorialsVedioItem
try:
    import urlparse as parse
except:
    from urllib import parse


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['space.bilibili.com']
    start_urls = ['https://space.bilibili.com/40496566#!/']

    def parse(self, response):
        """
                1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
                2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
                """

        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析front_image_url

        post_nodes = response.css('#col-1 .content div')
        for post_node in post_nodes:
            # yield 关键字 代表下载解析request
            # front_image_url = post_node.css('img::attr(src)').extract_first("")
            post_url = post_node.css('a:nth-child(2)::attr(href)').extract_first("")

            yield Request(url=parse.urljoin(response.url, post_url),
                          # meta={"front_image_url": parse.urljoin(response.url, front_image_url)},
                          callback=self.parse_detail)

            # 提取下一页并交给scrapy进行下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):
        pass
