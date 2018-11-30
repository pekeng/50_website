# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # DomainID = scrapy.Field()  # 域名id
    URLID = scrapy.Field()  # 输入urlid
    webid = scrapy.Field()

    title = scrapy.Field()  # 标题
    author = scrapy.Field()  # 作者
    column = scrapy.Field()  # 栏目
    public_time = scrapy.Field()  # 发布时间
    comment = scrapy.Field()  # 评论数

    Path = scrapy.Field()  # html路径
    Addpath = scrapy.Field()  # 附件路径

    crawl_time = scrapy.Field()  # 爬取时间
