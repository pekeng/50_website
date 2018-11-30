# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import ArticlespiderItem
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ArticleSpider.settings import db_user, db_pawd, db_host, db_port, db_name
from ArticleSpider.models import WebList, StartUrl, WebDetail

# 创建对象的基类:
Base = declarative_base()


class ArticlespiderPipeline(object):
    def __init__(self):  # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def process_item(self, item, spider):
        info = WebDetail(
            webid=item['webid'],
            URLID=item['URLID'],

            title=item['title'],
            author=item['author'],
            column=item['column'],
            public_time=item['public_time'],
            comment=item['comment'],
            Path=item['Path'],
            Addpath=item['Addpath'],
            crawl_time=datetime.datetime.now(),
        )
        try:
            self.session.add(info)
            self.session.commit()
            print("成功：{}".format(item))
        except Exception as e:
            print("[UUU] 解析数据插入数据出错 Error :{} 地址：{}".format(e, item['URLID']))
            self.session.rollback()
        return item

    def select_url(self):
        try:
            result = self.session.query(StartUrl).filter(
                StartUrl.status == '0').all()
            return result
        except Exception as e:
            print("查询出错：{}".format(e))
            pass
