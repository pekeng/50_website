# -*- coding: utf-8 -*-
import sys
from scrapy import cmdline

if __name__ == '__main__':
    # cmdline.execute(['scrapy','crawl','example'])
    sys.path.append('D:\work\CrawlerProject')
    # cmdline.execute(['scrapy', 'crawl', 'example'])
    cmdline.execute(('scrapy crawl example --nolog').split())
