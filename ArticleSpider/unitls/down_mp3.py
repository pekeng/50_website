# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:CrawlerProject
FileName = PyCharm
Version:1.0
CreateDay:2018/8/28 19:11
"""
import requests


def down_mp3():
    url = 'https://www.vot.org/wp-content/uploads/2018/05/Sonam-Gyatso-.mp3'
    response = requests.get(url)
    with open('Sonam-Gyatso-.mp3', 'wb+') as f:
        f.write(response.content)


if __name__ == "__main__":
    pass
