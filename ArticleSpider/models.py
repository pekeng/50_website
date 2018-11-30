#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import datetime
from sqlalchemy import Column, String, create_engine, Integer, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base
from ArticleSpider.settings import db_host, db_user, db_pawd, db_name, db_port

# 创建对象的基类:
Base = declarative_base()


# 网站列表
class WebList(Base):
    # 表的名字:
    __tablename__ = 'WebList'.lower()
    # 表的结构:
    id = Column(Integer, primary_key=True)
    webid = Column(Integer, )
    name = Column(String(300), )
    domain = Column(String(300))


# 输入的起始地址
class StartUrl(Base):
    # 表的名字:
    __tablename__ = 'StartUrl'.lower()
    # 表的结构:
    id = Column(Integer, primary_key=True)
    webid = Column(Integer, )
    url = Column(String(300), )
    name = Column(String(300), )
    date = Column(DateTime, default=datetime.datetime.now)
    userid = Column(Integer, default=1)
    type = Column(String(200), )
    status = Column(Integer, )  # 0表示未爬取 1 表示爬取中 2 表示爬取完成 3 爬取失败


# 网站内容提取
class WebDetail(Base):
    # 表的名字:
    __tablename__ = 'WebDetail'.lower()
    # 表的结构:
    id = Column(Integer, primary_key=True)
    webid = Column(Integer, )  # 网站ID 对应WEBLIST表的ID
    URLID = Column(String(300), )  # 输入urlid 对应STARTURL表的ID

    title = Column(String(300), )  # 标题
    author = Column(String(300), )  # 作者
    column = Column(String(300), )  # 栏目
    public_time = Column(String(300), )  # 发布时间
    comment = Column(String(300), )  # 评论数

    Path = Column(String(300), )  # html路径
    Addpath = Column(String(300), )  # 附件路径

    crawl_time = Column(DateTime, )  # 爬取时间


if __name__ == "__main__":
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'
                           .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
    Base.metadata.create_all(engine)
