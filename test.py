# # -*- coding: utf-8 -*-
import re
import time
import requests
import json
from copy import deepcopy

try:
    from unitls.ConfigureRule import XpathRule
    from unitls.date_trans import time_translate_dict, time_translate_dict2, time_translate_dict3, \
        time_translate_dict4, time_translate_dict5, translate_days, translate_months, translate_weeks, get_comment
except:
    from ArticleSpider.unitls.ConfigureRule import XpathRule
    from ArticleSpider.unitls.date_trans import time_translate_dict, time_translate_dict2, time_translate_dict3, \
        time_translate_dict4, time_translate_dict5, translate_days, translate_months, translate_weeks, get_comment
import datetime
from lxml import etree

default_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/68.0.3423.2 Safari/537.36'
}


def main():
    url_list = [
        'https://www.youtube.com/watch?v=ma7r2HGqwXs',
    ]

    for url in url_list:
        res = requests.get(url=url, headers=default_headers)
        response = etree.HTML(res.text)
        try:
            title = ''.join(re.findall(
                re.compile(r'document.title = "(.*?)"'), res.text)).strip()  # 标题
            author = ''.join(re.findall(
                re.compile(r'"author":"(.*?)"'), res.text)).strip()  # 作者
            public_time = ''.join(re.findall(
                re.compile(r'"dateText":{"simpleText":"(.*?)"}'), res.text)).strip()  # 发布时间
            comment = getcomment(url)
            print('正在解析的url:{}'.format(res.url))
            print('文章题目：{}'.format(title))
            print('提取作者：{}'.format(author))
            print('提取栏目：{}'.format(column))
            print('提取发布时间：{}'.format(public_time))
            print('评论数：{}'.format(comment))
        except Exception as e:
            print('解析西藏之页出错：{}'.format(e))


def get_data(session, url):
    count = 0
    while True:
        response = session.get(url=url, headers=default_headers, )
        if response.status_code == 200:
            ctoken = "".join(re.findall(re.compile(r'continuation":"(.*?)",'), response.text, ))[:56]
            continuation = deepcopy(ctoken)
            itct = "".join(re.findall(r'wFAABgG","clickTrackingParams":"(.*?)","label":{"', response.text))
            session_token = "".join(re.findall(r'XSRF_TOKEN":"(.*?)","', response.text))
            page_label = "".join(re.findall(r'"PAGE_BUILD_LABEL":"(.*?)",', response.text))
            page_cl = "".join(re.findall(r'"PAGE_CL":(\d+),"', response.text))
            version = "".join(re.findall(r'"INNERTUBE_CONTEXT_CLIENT_VERSION":"(.*?)",', response.text))
            if all([ctoken, continuation, itct, session_token]):
                return ctoken, continuation, itct, session_token, page_label, page_cl, version
        if count > 5:
            return "", "", "", ""
        else:
            count = count + 1


def getcomment(url):
    ajax_url = 'https://www.youtube.com/comment_service_ajax'
    session = requests.Session()
    ctoken, continuation, itct, session_token, page_label, page_cl, version = get_data(session, url)
    time.sleep(3)
    headers = {
        'accept': '*/*',
        'accept-encoding': 'text',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.youtube.com',
        'referer': '{}'.format(url),
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'x-spf-previous': '{}'.format(url),
        'x-spf-referer': '{}'.format(url),
        'x-youtube-client-name': '1',
        'x-youtube-client-version': version,
        'x-youtube-page-cl': page_cl,
        'x-youtube-page-label': page_label,
        'x-youtube-utc-offset': '480',
    }
    data = {'session_token': session_token}
    params = {"action_get_comments": 1,
              "pbj": 1,
              "ctoken": ctoken,
              "continuation": continuation,
              "itct": itct,
              }
    resp = session.post(url=ajax_url,
                        data=data,
                        params=params,
                        headers=headers, )
    if resp.status_code == 200:
        comment = "".join(
            re.findall(r'"header":{"commentsHeaderRenderer":{"countText":{"simpleText":"(.*?)"}', resp.text)) \
            .replace('条评论', '').replace(',', '').strip()
    else:
        comment = ''
    return comment


if __name__ == '__main__':
    main()
