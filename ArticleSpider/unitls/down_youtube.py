# -*- coding:utf-8 -*-
"""
__author__ = "jake"
__email__ = "jakejie@163.com"
FileName = down_youtube.py
site: 
version: python3.6
CreateDay:2018/8/26 11:24
"""
import sys
import time
import os
import re
import requests
from functools import wraps
from pytube import YouTube
from pathlib import Path
from lxml import etree

urls = (
    # 'https://www.youtube.com/watch?v=H0SbnlDsdAc',
    # 'https://www.youtube.com/watch?v=McVxUs7d7ok',
    # 'https://www.youtube.com/watch?v=5obRgTyTy7Q',
    # 'https://www.youtube.com/watch?v=ZKZW2M1C7jU',
    # 'https://www.youtube.com/watch?v=AjgD3CvWzS0',
    # 'https://www.youtube.com/watch?v=JmiKWTRoiMk',
    "https://www.youtube.com/embed/j9GqV2_IC7k?list=PLE7Wm-v0hYnkLNvOcFbBDpH39BaeXJUkG",
)


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("[TIME       ] {0}".format(getHumanTime(end - start)))
        return result

    return wrapper


def getHumanTime(sec):
    if sec >= 3600:  # Converts to Hours
        return '{0:d} hour(s)'.format(int(sec / 3600))
    elif sec >= 60:  # Converts to Minutes
        return '{0:d} minute(s)'.format(int(sec / 60))
    else:  # No Conversion
        return '{0:d} second(s)'.format(int(sec))


@timethis
def download(local_dir, html):
    """

    :param url:下载地址
    :param local_dir: 保存地址
    :return:
    """
    tree = etree.HTML(html)
    all_youtube_video = tree.xpath('//div[@class="imgbox fpthumb shadow5d"]/a/@href')
    for youtube_url in all_youtube_video:
        video_name = str(youtube_url).split('v=')[-1] + ".mp4"
        print("地址：{}".format(youtube_url))
        try:
            yt = YouTube(youtube_url)
        except Exception as e:
            print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
            return -1

        pattern = r'[\/.:*?"<>|]+'
        regex = re.compile(pattern)
        # filename = regex.sub('', yt.title). \
        #                replace('\'', '').replace('\\', '') + ".mp4"
        p = Path(local_dir)
        fp = p / video_name
        if fp.exists():
            print("[SKIP       ] {0}".format(video_name))
            return 0
        try:
            print("[DOWNLOAD   ] {0}".format(video_name))
            yt.streams.filter(subtype='mp4', progressive=True) \
                .order_by('resolution') \
                .desc() \
                .first().download(local_dir)

            print("[DONE       ] {0}".format(video_name))
            html = html.replace(youtube_url, local_dir + "/" + video_name)
        except Exception as e:
            print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
            return -1
    print(html)
    return 1


def main():
    url = "http://www.tibetonline.tv/sikyongs-talks-and-visits/"
    response = requests.get(url)
    html = response.text
    download('youtube', html)


def down_youtube():
    url = "https://www.youtube.com/watch?v=Fn30JuTJ0uk",
    local_dir = ''
    try:
        yt = YouTube(url)
    except Exception as e:
        print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
        return -1

    pattern = r'[\/.:*?"<>|]+'
    regex = re.compile(pattern)
    filename = regex.sub('', yt.title). \
                   replace('\'', '').replace('\\', '') + ".mp4"

    p = Path(local_dir)
    fp = p / filename
    if fp.exists():
        print("[SKIP       ] {0}".format(filename))
        return 0

    try:
        print("[DOWNLOAD   ] {0}".format(filename))
        yt.streams.filter(subtype='mp4', progressive=True) \
            .order_by('resolution') \
            .desc() \
            .first().download(local_dir)

        print("[DONE       ] {0}".format(filename))
    except Exception as e:
        print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
        return -1

    return 1


if __name__ == "__main__":
    # main()
    down_youtube()
