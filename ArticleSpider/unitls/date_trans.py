# -*- coding:utf-8 -*-
"""
__author__ = "jake"
__email__ = "jakejie@163.com"
FileName = date_trans.py
site: 
version: python3.6
CreateDay:2018/8/27 22:30
"""
import time
import datetime
import calendar
import requests


# # 转换多少天以前日期
def translate_days(data_time):
    data_time = data_time.replace('day', '').replace('s', '').replace('ago', '').strip()
    n = int(data_time)
    public_time = ((datetime.datetime.now() - datetime.timedelta(days=n)).date())
    return public_time


# # 转换多少月以前日期
def translate_months(data_time):
    data_time = data_time.replace('month', '').replace('s', '').replace('ago', '').strip()
    month = int(data_time)
    year = time.strftime("%Y")
    m, n = calendar.monthrange(year, month)
    public_time = ((datetime.datetime.now() - datetime.timedelta(days=n)).date())
    return public_time


# # 转换多少星期以前日期
def translate_weeks(data_time):
    data_time = data_time.replace('week', '').replace('s', '').replace('ago', '').strip()
    n = int(data_time)
    public_time = ((datetime.datetime.now() - datetime.timedelta(weeks=n)).date())
    return public_time


def get_comment(num):
    from_data = {
        'PostId': "{}".format(num),
        'SortOrder': '0'
    }
    dalailama_headers = {
        # 'Proxy-Connection': 'keep-alive',
        # 'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/68.0.3423.2 Safari/537.36'
    }
    url = 'http://tibetanscientificsociety.com/Services/GetCommentList'
    response = requests.post(url=url, data=from_data, headers=dalailama_headers)
    data = response.json()
    return len(data)


# 英文1德语
time_translate_dict = {'January': 1,
                       'JANUAR': 1,
                       'February': 2,
                       'FEBRUAR': 2,
                       'March': 3,
                       'MÄRZ': 3,
                       'April': 4,
                       'APRIL': 4,
                       'May': 5,
                       'MAI': 5,
                       'June': 6,
                       'Juni': 6,
                       'JUNI': 6,
                       'July': 7,
                       'JULI': 7,
                       'August': 8,
                       'AUGUST': 8,
                       'September': 9,
                       'SEPTEMBER': 9,
                       'October': 10,
                       'OKTOBER': 10,
                       'November': 11,
                       'NOVEMBER': 11,
                       'December': 12,
                       'DEZEMBER': 12,
                       '01':1,
                       '02':2,
                       '03':3,
                       '04':4,
                       '05':5,
                       '06':6,
                       '07':7,
                       '08':8,
                       '09':9,
                       '10':10,
                       '11':11,
                       '12':12,
                       }
time_translate_dict2 = {'一月': 1,
                        '二月': 2,
                        '三月': 3,
                        '四月': 4,
                        '五月': 5,
                        '六月': 6,
                        '七月': 7,
                        '八月': 8,
                        '九月': 9,
                        '十月': 10,
                        '十一月': 11,
                        '十二月': 12,
                        }
# 俄语日期
time_translate_dict3 = {'января': 1,
                        'февраля': 2,
                        'марта': 3,
                        'апреля': 4,
                        'мая': 5,
                        'июня': 6,
                        'июля': 7,
                        'августа': 8,
                        'сентября': 9,
                        'октября': 10,
                        'ноября': 11,
                        'декабря': 12, }
# 英文2
time_translate_dict4 = {'Jan': 1,
                        'Feb': 2,
                        'Mar': 3,
                        'Apr': 4,
                        'May': 5,
                        'Jun': 6,
                        'Jul': 7,
                        'Aug': 8,
                        'Sep': 9,
                        'Oct': 10,
                        'Nov': 11,
                        'Dec': 12,
                        }
# 数字英文
time_translate_dict5 = {'One': 1,
                        'Two': 2,
                        'Three': 3,
                        'Four': 4,
                        'Five': 5,
                        'Six': 6,
                        'Seven': 7,
                        'Eight': 8,
                        'Nine': 9,
                        'Ten': 10,
                        'Eleven': 11,
                        'Twelve': 12,
                        'Thirteen': 13,
                        'Fourteen': 14,
                        'Fifteen': 15,
                        'Sixteen': 16,
                        'Seventeen': 17,
                        'Eighteen': 18,
                        'Nineteen': 19,
                        'Twenty': 20,
                        'Twenty-one': 21,
                        'Thirty': 30}

if __name__ == "__main__":
    comment_num = get_comment('19')
    print(comment_num)
