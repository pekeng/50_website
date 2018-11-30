# -*- coding: utf-8 -*-
import re
import datetime
import scrapy
from ArticleSpider.items import ArticlespiderItem

try:
    from pipelines import ArticlespiderPipeline
    from unitls.ConfigureRule import XpathRule
    from unitls.save_file import save_file
    from unitls.date_trans import time_translate_dict, time_translate_dict2, time_translate_dict3, \
        time_translate_dict4, time_translate_dict5, translate_days, translate_months, translate_weeks, get_comment
except:
    from ArticleSpider.pipelines import ArticlespiderPipeline
    from ArticleSpider.unitls.ConfigureRule import XpathRule
    from ArticleSpider.unitls.save_file import save_file
    from ArticleSpider.unitls.date_trans import time_translate_dict, time_translate_dict2, time_translate_dict3, \
        time_translate_dict4, time_translate_dict5, translate_days, translate_months, translate_weeks, get_comment


class ExampleSpider(scrapy.Spider, ArticlespiderPipeline):
    name = 'file'
    DEBUG = True
    allowed_domains = [value['domain'] for key, value in XpathRule.items()]
    dalailama_headers = {
        'Proxy-Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
                        Chrome/68.0.3423.2 Safari/537.36'
    }
    domain_url = 'http://www.tibet.net/'

    custom_settings = {
        "DOWNLOAD_TIMEOUT": 120,
        "HTTP_ALLOWED_CODE": [302],
    }

    def __init__(self):
        ArticlespiderPipeline.__init__(self)

    def start_requests(self):
        for url_info in self.select_url():
            urlId = url_info.id
            webid = url_info.webid
            url = url_info.url
            name = url_info.name

            yield scrapy.Request(
                url=url,
                headers=self.dalailama_headers,
                callback=self.parse_detail,
                meta={
                    "webId": webid,
                    "urlId": urlId,
                    "name": name,
                }
            )

    # 所有页面的处理函数
    def parse_detail(self, response):

        webId = str(response.meta["webId"])
        urlId = str(response.meta["urlId"])
        name = response.meta["name"]
        print(webId, name, )
        item = ArticlespiderItem()
        try:
            # 提取标题
            if XpathRule[webId]["title"]["type"] == "xpath":
                title = ''.join(response.xpath(XpathRule[webId]["title"]["rule"]).extract()) \
                    .replace('&nbsp', '').strip()  # 标题
                # title = title if title else "无法找到标题"
            elif XpathRule[webId]["title"]["type"] == "re":
                title = "".join(re.findall(re.compile(r''), response.text))
                # title = title if title else "无法找到标题"
            else:
                title = ""
            if not title:
                title = "".join(response.xpath('//title/text()').extract())
                # title = title if title else "无法找到标题"
            if not title:
                title = "无法找到标题"

            # 提取作者
            if XpathRule[webId]["author"]["type"] == "xpath":
                author = ''.join(response.xpath(XpathRule[webId]["author"]["rule"]).extract()) \
                    .replace('&nbsp', '').replace(';', '').replace('Published By', '') \
                    .replace('Published By', '').replace('By', '').strip()  # 作者
                # author = author if author else "无法找到作者"
            elif XpathRule[webId]["author"]["type"] == "re":
                author = "".join(re.findall(re.compile(r'5px">By(.*?)<b'), response.text))
                # author = author if author else "无法找到作者"
            else:
                author = "无法找到作者"

            # 提取栏目
            if XpathRule[webId]["column"]["type"] == "xpath":
                if webId == '45':
                    if 'studium-buddhismus' in response.url or 'ausstellungen' in response.url:
                        column = ''.join(response.xpath(
                            '//ol[@class="breadcrumb pull-right hidden-xs"]/li[3]/a/span/text()').extract()).strip()
                        # column = column if column else "无法找到栏目"
                    else:
                        column = ''.join(response.xpath(XpathRule[webId]["column"]["rule"]).extract()).strip()  # 栏目
                        # column = column if column else "无法找到栏目"
                else:
                    column = ','.join(response.xpath(XpathRule[webId]["column"]["rule"]).extract()) \
                        .replace('DOWNLOAD', '').replace('Comment', '').replace('s', '').strip()  # 栏目
                # column = column if column else "无法找到栏目"
            elif XpathRule[webId]["column"]["type"] == "re":
                column = "".join(re.findall(re.compile(r''), response.text))
                # column = column if column else "无法找到栏目"
            else:
                column = "无法找到栏目"

            # 提取发布时间
            if XpathRule[webId]["public_time"]["type"] == "xpath":
                if webId == '19':
                    public_time = '/'.join(response.xpath(XpathRule[webId]["public_time"]["rule"]).extract()) \
                        .replace('(Last updated on', '').replace(')', '').replace('|', '')\
                        .replace('EVENT:', '').replace('Posted on', '').strip()
                    # public_time = public_time if public_time else "无法找到发布时间"
                elif webId == '39':
                    public_time = ''.join(re.findall(re.compile(r'\d{8}'), response.url))
                    if public_time:
                        public_time = '{}-{}-{}'.format(public_time[:4], public_time[4:6], public_time[6:8])
                        # public_time = public_time if public_time else "无法找到发布时间"
                    else:
                        public_time = ''.join(response.xpath(
                            XpathRule[webId]["public_time"]["rule"]).extract()).strip()
                        # public_time = public_time if public_time else "无法找到发布时间"
                else:
                    public_time = ''.join(response.xpath(XpathRule[webId]["public_time"]["rule"]).extract()) \
                        .replace('(Last updated on', '').replace(')', '').replace('|', '') \
                        .replace('EVENT:', '').replace('[', '').replace(']', '').replace('.', '').strip()
                # public_time = public_time if public_time else "无法找到发布时间"
            elif XpathRule[webId]["public_time"]["type"] == "re":
                if webId == '21':
                    if title:
                        public_time1 = "".join(re.findall(re.compile(r'\d+/\d+/\d+'), title)).strip()
                        public_time = public_time1.replace('/', '-')  # 发布时间
                        # public_time = public_time if public_time else "无法找到发布时间"
                    else:
                        public_time = '无法找到发布时间'
                else:  # 正常的处理路径
                    public_time = "".join(re.findall(re.compile(r'（(\d+年\d+月\d+日)'), response.text)).strip()
                # public_time = public_time if public_time else "无法找到发布时间"
            else:
                public_time = "无法找到发布时间"

            # 提取评论数
            if XpathRule[webId]["comment"]["type"] == "xpath":
                if webId == '19' or webId == '22' or webId == '48':
                    comment = "".join(response.xpath(XpathRule[webId]["comment"]["rule"]).extract()) \
                        .replace('Comment', '').replace('s', '').replace('Add comment', '')\
                        .replace('則留言:','').replace('沒有留言:','').strip()
                    comment = '0' if comment == "No" else comment
                    # comment = comment if comment else "无法找到评论数"
                else:
                    comment = len(response.xpath(XpathRule[webId]["comment"]["rule"]).extract())
                # comment = comment if comment else "无法找到评论数"
            elif XpathRule[webId]["comment"]["type"] == "re":
                num = ''.join(re.findall(re.compile(r'Detail/(\d+)/'), response.url))
                if num:
                    comment = get_comment(num)
                    # comment = comment if comment else "无法找到评论数"
                else:
                    comment = "无法找到评论数"
                # comment = comment if comment else "无法找到评论数"
            else:
                comment = "无法找到评论数"
            item['URLID'] = urlId
            item['webid'] = webId

            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['comment'] = comment
            # print(item)
            Path, Addpath = save_file(webId, response.url, response)
            item['Path'] = Path
            item['Addpath'] = Addpath
            # print(item)
            yield item
        except Exception as e:
            print('解析{}出错：{}'.format(name, e)) if self.DEBUG else ''


"""

    # 流亡藏人科学协会
    def parse_xzscience(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@id="story_center"]/h1/text()|\
                //div[@id="katyContainer"]/div/h1/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//span[@id="SpnDate"]/a/text()').extract()).strip()  # 作者
            column = ''.join(response.xpath(
                '//div[@id="breadCrumb"]/a[2]/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath('//span[@id="SpnDate"]/text()[2]').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(
                    data_time2[2], time_translate_dict[data_time2[0]], data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            print(response.xpath('//div[@id="divDataListCommentFn__"]/div').extract())
            num = ''.join(re.findall(re.compile(r'Detail/(\d+)/'), response.url))
            if num:
                comment = get_comment(num)
            else:
                comment = '-'
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('流亡藏人科学协会出错：{}'.format(e)) if self.DEBUG else ''

    # 瑞士里肯西藏中心
    def parse_ruishi(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@class="content"]/h1/text()|\
                //form[@name="step1"]/h1[1]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath(
                '//li[@class="selected"]/a/text()').extract()).strip()  # 栏目
            if column:
                pass
            else:
                column = 'publications'
            public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('瑞士里肯西藏中心出错：{}'.format(e)) if self.DEBUG else ''

    # 解救西藏组织（FreeTibet Campaign）
    def parse_savexz(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//h2[@class="blog-title"]/a/text()|\
                //a[@class="blog-title-link blog-link"]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath(
                '//p[@class="blog-category-list"]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath('//p[@class="blog-date"]/span/text()|\
                //span[@class="date-text"]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split('/')
                public_time = '{}-{}-{}'.format(
                    data_time2[2], data_time2[1], data_time2[0])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = ''.join(response.xpath('//div[@class="blog-comments-bottom"]/a/text()').extract()) \
                .replace('Comment', '').replace('s', '').strip()  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = str(comment)
            yield item
        except Exception as e:
            print('解救西藏组织（FreeTibet Campaign）出错：{}'.format(e)) if self.DEBUG else ''

    # 捷克支持西藏（Czechs Support Tibet）
    def parse_jieke(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//h1[@class="h2"]/text()|\
                //h1[@class="site__title"]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            if 'event' in response.url:
                column = 'Co děláme'  # 栏目
            else:
                column = 'Aktuality'
            data_time = ''.join(response.xpath('//time[@class="event__date"]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split('/')
                public_time = '{}-{}-{}'.format(data_time2[2], data_time2[1], data_time2[0])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('捷克支持西藏（Czechs Support Tibet）出错：{}'.format(e)) if self.DEBUG else ''

    # 德国援助藏人组织
    def parse_deguohelp(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('德国援助藏人组织出错：{}'.format(e)) if self.DEBUG else ''

    # 德国西藏之家）
    def parse_xzdeguohome(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@id="calendar-event"]/h3/text()|\
                //div[@id="partialContentMain"]/div[1]/div/h1/text()|\
                //div[@id="partialContentMain"]/div[1]/h1/text()|\
                //div[@class="csc-header csc-header-n2"]/h2/text()|\
                //div[@class="csc-header csc-header-n1"]/h2/text()|\
                //div[@class="csc-header csc-header-n2"]/h1/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//div[@id="calendar-event"]/p[2]/b/text()').extract()).replace('Kursleitung |', '').strip()  # 作者
            if 'studium-buddhismus' in response.url or 'ausstellungen' in response.url:
                column = ''.join(response.xpath(
                    '//ol[@class="breadcrumb pull-right hidden-xs"]/li[3]/a/span/text()').extract()).strip()
            else:
                column = ''.join(response.xpath('//ol[@class="breadcrumb pull-right hidden-xs"]/li/span/text()|\
                    //ol[@class="breadcrumb pull-right hidden-xs"]/li[3]/span/text()').extract()).strip()  # 栏目
            if column:
                pass
            else:
                column = '-'
            data_time = ''.join(response.xpath('//div[@id="calendar-event"]/p[1]/b/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(
                    data_time2[-1], time_translate_dict[data_time2[-2].upper()], data_time2[-3])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('德国西藏之家出错：{}'.format(e)) if self.DEBUG else ''

    # 德国西藏圣山之家
    def parse_xzshensan(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('德国西藏圣山之家出错：{}'.format(e)) if self.DEBUG else ''

    # 德国西藏倡议组织（TID）
    def parse_xzdeguo(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//h1[@class="post-title"]/a/span/text()|\
                    //section[@id="box"]/div[1]/div[1]/div/div/h1/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath(
                '//p[@class="meta cat tranz "]/a/text()').extract()).strip()  # 栏目
            public_time = ''.join(re.findall(re.compile(r'\d{8}'), response.url))
            if public_time:
                public_time = '{}-{}-{}'.format(public_time[:4], public_time[4:6], public_time[6:8])  # 没有用
            else:
                data_time = ''.join(response.xpath('//div[@id="content"]/div/p[2]/text()').extract()).strip()
                if data_time:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    public_time = '{}-{}-{}'.format(
                        data_time2[2], time_translate_dict[data_time2[1].upper()], data_time2[0])  # 发布时间
                else:
                    public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('德国西藏倡议组织（TID）出错：{}'.format(e)) if self.DEBUG else ''

    # 丹麦司法部所成立的西藏调查委员会
    def parse_xzdanmai(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="section"]/div/h1/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = '-'  # 栏目
            public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('丹麦司法部所成立的西藏调查委员会出错：{}'.format(e)) if self.DEBUG else ''

    # 大赦国际（国际特赦组织）
    def parse_amninternatl(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//h1[@class="heading--main heading--in-padded"]/text()|\
                //h1[@class="heading--main heading--uppercase heading--in-padded"]/text()|\
                //div[@class="col__content"]/h1/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath(
                '//li[@class="tags__item--bold"]/span/text()|\
                //span[@class="tags__icon--bold--documentsummary"]/text()').extract()).strip()  # 栏目
            public_time = ''.join(re.findall(re.compile(r'\d{8}'), response.url))
            if public_time:
                public_time = '{}-{}-{}'.format(public_time[:4], public_time[4:6], public_time[6:8])  # 没有用
            else:
                data_time = ''.join(response.xpath('//div[@class="meta__section "]/div/time/text()|\
                    //div[@class="col__content"]/p/time/text()').extract()).strip()
                if data_time:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    public_time = '{}-{}-{}'.format(
                        data_time2[2], time_translate_dict[data_time2[1]], data_time2[0])  # 发布时间
                else:
                    public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('大赦国际（国际特赦组织）出错：{}'.format(e)) if self.DEBUG else ''

    # 达兰萨拉利众中心
    def parse_dalancenter(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//h1[@class="entry-title"]/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath('//span[@class="author vcard"]/a/text()').extract()).strip()  # 作者
            column = '-'  # 栏目
            public_time = ''.join(re.findall(re.compile(r'\d{8}'), response.url))
            if public_time:
                public_time = '{}-{}-{}'.format(public_time[:4], public_time[4:6], public_time[6:8])  # 没有用
            else:
                data_time = ''.join(response.xpath(
                    '//time[@class="entry-date published"]/text()').extract()).strip()
                if data_time:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    public_time = '{}-{}-{}'.format(
                        data_time2[2], time_translate_dict[data_time2[0]], data_time2[1])  # 发布时间
                else:
                    public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('达兰萨拉利众中心出错：{}'.format(e)) if self.DEBUG else ''

    # 大宝法王噶玛巴中文网站
    def parse_dabao(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="item-page"]/h2/a/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath(
                '//dd[@class="gj-category-name"]/a/text()').extract()).strip()  # 栏目
            public_time = ''.join(re.findall(re.compile(r'\d{8}'), response.url))
            if public_time:
                public_time = '{}-{}-{}'.format(public_time[:4], public_time[4:6], public_time[6:8])
            else:
                data_time = ''.join(response.xpath(
                    '//div[@class="item-page"]/p[1]/text()[1]').extract()).strip()
                if data_time:
                    public_time = data_time.replace('年', '-').replace('月', '-') \
                        .replace('日', '').replace('時間：', '').replace('上午', '') \
                        .replace('下午', '').replace('中午', '').strip()  # 发布时间
                else:
                    public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('大宝法王噶玛巴中文网站出错：{}'.format(e)) if self.DEBUG else ''

    # 达兰萨拉信息网   # 跳转到家乡 (英)
    def parse_dalan(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('达兰萨拉信息网出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏在线   #跳转
    def parse_xzzaixian(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏在线)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏讯息港(英)   #
    def parse_xzxianggang(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏讯息港(英)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏之声    # 休眠状态
    def parse_xzzs(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//main[@class="main col-sm-9"]/div[1]/article/header/h1/text()|\
                //div[@class="page"]/article/header/h1/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ''.join(response.xpath('//span[@class="vcard author"]/span/text()|\
                //span[@class="fn"]/text()').extract()).strip()  # 栏目
            public_time = ''.join(response.xpath('//div[@class="page"]/article/header/div/time/text()|\
                //time[@class="published updated"]/text()').extract()).strip()  # 藏文日期
            # if data_time:
            #     data_time2 = data_time.replace(', ', ' ').split()
            #     public_time = '{}-{}-{}'.format(data_time2[3], time_translate_dict[data_time2[1]],
            #                                     data_time2[2])  # 发布时间
            # else:
            #     public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('西藏之声出错：{}'.format(e)) if self.DEBUG else ''

    # 家乡 (英)
    def parse_jiaxiang(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//span[@id="_ctl1_lblHeading"]/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//td[@id="_ctl1_story"]/div/text()[1]').extract()).replace('By', '').strip()  # 作者
            column = '-'  # 栏目
            data_time = ''.join(response.xpath('//span[@id="_ctl1_lblDate"]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[3], time_translate_dict[data_time2[1]],
                                                data_time2[2])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = str(len(response.xpath('//td[@class="newsDiscussionMessage"]/table/tr').extract()))  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('家乡 (英)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏全球新闻(英文) # 网站出售
    def parse_xzglobal(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏全球新闻(英文)出错：{}'.format(e)) if self.DEBUG else ''

    # 加拿大西藏同乡会
    def parse_canada(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@id="column_main"]/div/h1[1]/text()|\
                //div[@id="column_main"]/div/div[1]/h1[1]/text()|\
                //div[@class="upcoming_events"]/div[1]/h1[1]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = '-'  # 栏目
            data_time = ''.join(response.xpath(
                '//div[@class="date"]/text()').extract()).replace('EVENT:', '').strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('加拿大西藏同乡会出错：{}'.format(e)) if self.DEBUG else ''

    # 妙宗班智达翻译小组会
    def parse_xztranslate(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(re.findall(re.compile(r'<title>(.*?)</title>'), response.text))
            public_time = '-'  # 没有
            author = '-'  # 没有
            column = '-'  # 没有
            crawl_time = datetime.datetime.now()
            comment = '-'  # 没有
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('妙宗班智达翻译小组会出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏青年会(台湾分会) #
    def parse_xzyoungtaiwan(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏青年会(台湾分会)出错：{}'.format(e)) if self.DEBUG else ''

    # 阿尼玛钦西藏文化研究所 #
    def parse_xzculture(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('阿尼玛钦西藏文化研究所出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏妇女联合会
    def parse_xzwomen(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//h1[@class="post-title entry-title"]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath(
                '//ul[@class="post-meta"]/li/span/a/text()').extract()).strip().replace('\\', '')  # 栏目
            day_time = ''.join(response.xpath(
                '//span[@class="day"]/text()').extract()).strip()
            xpath_rule = '//span[@class="month"]/text()'
            month_time = ''.join(response.xpath().extract(xpath_rule)).strip()
            year_time = ''.join(response.xpath(
                '//span[@class="year"]/text()').extract()).strip()
            if month_time:
                public_time = '{}-{}-{}'.format(year_time, time_translate_dict4[month_time],
                                                day_time)  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('西藏妇女联合会出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏问题调解中心#
    def parse_xzresolve(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏问题调解中心出错：{}'.format(e)) if self.DEBUG else ''

    # 9•10•3组织 #
    def parse_xz9103(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('9•10•3组织出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏自由运动组织 #
    def parse_xzfreedom(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏人权民主促进会出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏青年会 #
    def parse_xzyoung(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏青年会出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏人权民主促进会
    def parse_xzrenquan(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@class="post-inner"]/h1/span/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath('//span[@class="post-cats"]/a/text()|\
            //div[@class="post-inner"]/p/span[2]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//div[@class="post-inner"]/p/span[1]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.split('/')
                public_time = '{}-{}-{}'.format(data_time2[2], data_time2[1], data_time2[0])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 没有评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('西藏人权民主促进会出错：{}'.format(e)) if self.DEBUG else ''

    # 国际声援西藏中心
    def parse_internet(self, response):
        item = ArticlespiderItem()
        if 'weblog' in response.url:
            try:
                title = ''.join(response.xpath(
                    '//h1[@class="entry-title"]/text()').extract()).strip()  # 标题
                author = ''.join(response.xpath(
                    '//div[@class="meta-item author"]/span/span/a/text()').extract()).replace('By:', '').strip()  # 没有作者
                column = 'ICT Blog'  # 栏目
                data_time = ''.join(response.xpath(
                    '//span[@class="updated"]/text()').extract()).strip()
                if data_time:
                    if 'month' in data_time:
                        public_time = translate_months(data_time)
                    elif 'yesterday' in data_time:
                        public_time = ((datetime.datetime.now() - datetime.timedelta(days=1)).date())
                    elif 'today' in data_time:
                        public_time = datetime.datetime.now().date()
                    elif 'day' in data_time:
                        public_time = translate_days(data_time)
                    elif 'week' in data_time:
                        public_time = translate_weeks(data_time)
                    else:
                        data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                        public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                        data_time2[1])  # 发布时间
                else:
                    public_time = ''
                    print('解析国际声援西藏中心微博出错') if self.DEBUG else ''
                crawl_time = datetime.datetime.now()  # 爬取时间
                comment = ''.join(response.xpath(
                    '//div[@class="meta-item comments"]/a/text()').extract()).replace(
                    'Comment', '').replace('s', '').strip()  # 评论数
                if 'Add comment' in comment:
                    comment = '-'
                else:
                    pass
                item['title'] = title
                item['public_time'] = public_time
                item['author'] = author
                item['column'] = column
                item['crawl_time'] = crawl_time
                item['comment'] = comment
                yield item
            except Exception as e:
                print('解析国际声援西藏中心微博出错：{}'.format(e)) if self.DEBUG else ''

        else:
            try:
                title = ''.join(response.xpath(
                    '//div[@id="main"]/div[1]/h1/text()|//h1[@class="title"]/text()').extract()).strip()  # 标题
                author = '-'  # 没有作者
                column = ','.join(response.xpath(
                    '//div[@class="post-meta"]/span/span/a/text()').extract()).strip()  # 栏目
                data_time = ''.join(response.xpath(
                    '//abbr[@class="date time published"]/text()').extract()).strip()
                if data_time:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                    data_time2[1])  # 发布时间
                else:
                    public_time = '-'
                crawl_time = datetime.datetime.now()  # 爬取时间
                comment = '-'  # 没有评论数
                item['title'] = title
                item['public_time'] = public_time
                item['author'] = author
                item['column'] = column
                item['crawl_time'] = crawl_time
                item['comment'] = comment
                yield item
            except Exception as e:
                print('解析国际声援西藏中心出错：{}'.format(e)) if self.DEBUG else ''

    # 达赖喇嘛官方华文网站
    def parse_huawen(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="subject_bg1 nav"]/text()').extract()).strip()  # 标题
            if title:
                public_time1 = "".join(re.findall(re.compile(r'\d+/\d+/\d+'), title)).strip()
                public_time = public_time1.replace('/', '-')  # 发布时间
            else:
                public_time = ''
            author = '-'  # 没有作者
            column = ','.join(response.xpath(
                '//a[@class="cattitle"]/text()').extract()).strip()  # 栏目
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '-'  # 没有评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('达赖喇嘛官方华文网站出错：{}'.format(e)) if self.DEBUG else ''

    # 桑波扎西藏完全学校
    def parse_xzwanquan(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//h1[@class="post_title single"]/span/a/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//li[@class="posted_by"]/a/text()').extract()).strip()  # 作者
            column = ','.join(response.xpath(
                '//li[@class="post_category"]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//li[@class="post_date"]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict4[data_time2[0]],
                                                data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = ''.join(response.xpath('//li[@class="post_comment"]/span/a/text()').extract()) \
                .replace('Comment', '').replace('s', '').replace('.', '').strip()  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('桑波扎西藏完全学校出错：{}'.format(e)) if self.DEBUG else ''

    # 达兰萨拉西藏儿童村(TCV)
    def parse_xzchilden(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//a[@rel="bookmark"]/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath(
                '//span[@class="cat-links"]/a/text()').extract()).strip()  # 栏目
            day_time = ''.join(response.xpath(
                '//span[@class="date-structure"]/h2/text()').extract()).strip()
            month_time = ''.join(response.xpath(
                '//span[@class="month"]/text()').extract()).strip()
            year_time = ''.join(response.xpath(
                '//span[@class="year"]/text()').extract()).strip()
            if month_time:
                public_time = '{}-{}-{}'.format(year_time, time_translate_dict4[month_time],
                                                day_time)  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = ''.join(response.xpath(
                '//span[@class="comments-link"]/a/text()').extract()).replace(
                'Comment', '').replace('s', '').strip()  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('达兰萨拉西藏儿童村(TCV)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏文献图书馆
    def parse_xzlibrary(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@class="post-inner"]/h1/span/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath('//span[@class="post-cats"]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//article[@id="the-post"]/div[2]/p/span[1]/text()|\
                //div[@class="post-inner"]/p/span[1]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('西藏文献图书馆出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏表演艺术学院 (TIPA) #
    def parse_xzarticle(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏表演艺术学院 (TIPA)出错：{}'.format(e)) if self.DEBUG else ''

    # 罗布尔卡西藏文化中心 #
    def parse_loubu(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('罗布尔卡西藏文化中心出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏视讯电视网 #
    def parse_xztv(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏视讯电视网出错：{}'.format(e)) if self.DEBUG else ''

    # 藏医历算学院 #
    def parse_zangyi(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('藏医历算学院出错：{}'.format(e)) if self.DEBUG else ''

    # 驻堪培拉代表处信息网 (英文) #
    def parse_kanpeila(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('驻堪培拉代表处信息网 (英文)出错：{}'.format(e)) if self.DEBUG else ''

    # 中南美洲联络处信息网 (西班牙文) #
    def parse_zhongnanmei(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//article[@id="the-post"]/div[2]/h1/span/text()|\
                //h1[@class="name post-title entry-title"]/span/text()|\
                //div[@class="post-inner"]/h1/span/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath(
                '//article[@id="the-post"]/div[2]/p/span[2]/a/text()|\
                //span[@class="post-cats"]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//article[@id="the-post"]/div[2]/p/span[1]/text()|\
                //div[@class="post-inner"]/p/span[1]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('中南美洲联络处信息网 (西班牙文)出错：{}'.format(e)) if self.DEBUG else ''

    # 欧盟联络处信息网 (法文)
    def parse_oumen(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('欧盟联络处信息网 (法文)出错：{}'.format(e)) if self.DEBUG else ''

    # 驻莫斯科代表处信息网 (俄文)
    def parse_moscow(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="text-02"]/div/h1[1]/text()|\
                //div[@class="text-02"]/div/h1[1]/font/font/text()').extract()).strip()  # 标题
            author = '-'  # 没有作者
            column = ''  # 无法区分栏目
            public_time = ''.join(response.xpath(
                '//div[@id="dle-content"]/div[1]/font/font/text()|\
                //div[@class="news-big-01"]/font/font/text()|\
                //*[@id="dle-content"]/div[1]/text()').extract()).strip().replace('|', '')  # 发布时间
            if public_time:
                public_time = public_time.split()
                public_time = '{}-{}-{}'.format(public_time[2], time_translate_dict3[public_time[1]],
                                                public_time[0])
            elif 'Вчера' in public_time:  # 昨天
                public_time = ((datetime.datetime.now() + datetime.timedelta(days=-1)).date())
            elif 'Сегодня' in public_time:  # 今天
                public_time = datetime.datetime.now().date()
            else:
                pass
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = str(len(response.xpath('//form[@id="dlemasscomments"]/div').extract()) - 1)  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('解析驻莫斯科代表处信息网 (俄文)出错：{}'.format(e)) if self.DEBUG else ''

    # 驻台北办事处信息网 (中文)
    def parse_taiwan(self, response):
        item = ArticlespiderItem()
        if 'statement' in response.url:
            try:
                title = ''.join(response.xpath(
                    '//p[@class="t11"]/strong/text()').extract()).strip()  # 标题
                author = '-'  # 作者
                column = ''.join(response.xpath(
                    '//span[@class="style2_title"]/text()').extract()).strip()  # 栏目
                public_time = ''.join(response.xpath(
                    '//td[@class="style3"]/blockquote/div/text()').extract()).strip()  # 发布时间
                if public_time:
                    public_time = ''.join(public_time[0]).replace('年', '-') \
                        .replace('月', '-').replace('日', '').replace('.', '-') \
                        .replace('.', '-').replace('/', '-').replace('/', '-')
                else:
                    public_time = '-'
                crawl_time = datetime.datetime.now()  # 爬取时间
                comment = '_'  # 评论数
                item['title'] = title
                item['public_time'] = public_time
                item['author'] = author
                item['column'] = column
                item['crawl_time'] = crawl_time
                item['comment'] = comment
                yield item
            except Exception as e:
                print('解析驻台北办事处信息网(中文)出错：{}'.format(e)) if self.DEBUG else ''
            pass
        elif 'com' or 'news' in response.url:
            try:
                title = ''.join(response.xpath(
                    '//p[@class="t11"]/strong/text()').extract()).strip()  # 标题
                if 'com' in response.url:
                    author = "".join(re.findall(re.compile(r'作者:(.*?)</strong>'), response.text)).strip()  # 作者
                elif 'com' in response.url:
                    author = "".join(re.findall(re.compile(r'資料來源:(.*?)</strong>'), response.text)).strip()
                else:
                    author = "-"
                    print('解析驻台北办事处信息网(中文)url出错') if self.DEBUG else ''
                column = ','.join(response.xpath(
                    '//span[@class="style2_title"]/text()').extract()).strip()  # 栏目
                public_time = "".join(re.findall(re.compile(r'(\d+-\d+-\d+)'), response.text)).strip()  # 发布时间
                crawl_time = datetime.datetime.now()  # 爬取时间
                comment = '_'  # 评论数
                item['title'] = title
                item['public_time'] = public_time
                item['author'] = author
                item['column'] = column
                item['crawl_time'] = crawl_time
                item['comment'] = comment
                yield item
            except Exception as e:
                print('解析驻台北办事处信息网(中文)出错：{}'.format(e)) if self.DEBUG else ''
        else:
            print('驻台北办事处信息网(中文)url有误') if self.DEBUG else ''

    # 驻东京代表处信息网 (日文)
    def parse_tokyo(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@id="main"]/div/h2/text()').extract()).strip()
            author = ''.join(response.xpath('//div[@class="translate"]/text()').extract()).strip()
            column = 'ニュース'  # 栏目
            data_time = "".join(re.findall(re.compile(r'（(\d+年\d+月\d+日)'), response.text)).strip()
            if data_time:
                public_time = data_time.replace('年', '-').replace('月', '-').replace('日', '')  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('解析驻东京代表处信息网 (日文)出错：{}'.format(e)) if self.DEBUG else ''

    # 驻伦敦代表处信息网 (英文) #同
    def parse_london(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="page-header"]/h1/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//div[@id="single_byline"]/text()').extract()).replace('Published By', '').strip()  # 作者
            column = ','.join(response.xpath(
                '//div[@id="single_meta"]/div[2]//a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//div[@id="single_meta"]/div[1]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                data_time2[1])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('解析驻伦敦代表处信息网 (英文)出错：{}'.format(e)) if self.DEBUG else ''

    # 驻纽约代表处信息网 (英文)
    def parse_tibetoffice_newyork(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@class="post-inner"]/h1/span/text()').extract()).strip()  # 标题
            author = '-'  # 作者
            column = ','.join(response.xpath('//span[@class="post-cats"]/a/text()|\
                    //div[@class="post-inner"]/p/span[2]/a/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//div[@class="post-inner"]/p/span[1]/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.split('/')
                public_time = '{}-{}-{}'.format(data_time2[2], data_time2[1], data_time2[0])  # 发布时间
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 没有评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('驻纽约代表处信息网 (英文)出错：{}'.format(e)) if self.DEBUG else ''

    # 驻日内瓦办事处信息网 (德文)
    def parse_tibetoffice_geneva(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//h1[@itemprop="headline"]/text()').extract()).strip()
            data_time = ''.join(response.xpath(
                '//main[@itemprop="mainContentOfPage"]/article/div/div/div/div/time/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]], data_time2[1])
            else:
                public_time = '-'
            author = '-'  # 没有作者 Source: dalailama.com
            column = '-'  # 无法区分
            crawl_time = datetime.datetime.now()
            comment = '-'
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('驻日内瓦办事处信息网 (德文)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏之页 (中文)
    def parse_xz_zhiye(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//main[@id="main-content-main"]/article/header/div[1]/h1/text()').extract()).strip()  # 标题
            author = ''.join(response.xpath(
                '//div[@id="single_byline"]/text()[2]').extract()).replace('&nbsp', '').replace(';', '').strip()  # 作者
            column = ','.join(response.xpath(
                '//div[@id="single_meta"]/div[2]//a/text()|//div[@id="single_byline"]/a[1]/text()').extract()).strip()  # 栏目
            data_time = ''.join(response.xpath(
                '//div[@id="single_meta"]/div[1]/text()').extract()).strip()
            if data_time:
                data_time2 = re.findall(re.compile(r'(\d+\/\d+\/\d+)|(\d+\-\d+\-\d+)'), data_time)
                if data_time2:
                    data_time2 = ''.join(data_time2[0]).replace('/', ' ').replace('-', ' ').split()
                    public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[1]],
                                                    data_time2[0])
                else:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    if len(data_time2) == 3:
                        public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                        data_time2[1])
                    elif len(data_time2) == 2:
                        public_time = '{}-{}'.format(data_time2[1], time_translate_dict[data_time2[0]])
                    else:
                        public_time = data_time2[0]
            else:
                public_time = '-'
            crawl_time = datetime.datetime.now()  # 爬取时间
            comment = '_'  # 评论数
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('解析西藏之页出错：{}'.format(e)) if self.DEBUG else ''

    # 藏人行政中央（藏、英）  ##同  ok
    def parse_tibet(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath('//div[@class="page-header"]/h1/text()').extract()).strip()
            data_time = ''.join(response.xpath('//div[@id="single_meta"]/div[1]/text()|\
                //main[@id="main-content-main"]/div/p[4]/em/text()').extract()) \
                .replace('(Last updated on', '').replace(')', '').strip()
            if data_time:
                data_time2 = re.findall(re.compile(r'(\d+\/\d+\/\d+)|(\d+\-\d+\-\d+)'), data_time)
                if data_time2:
                    data_time2 = ''.join(data_time2[0]).replace('/', ' ').replace('-', ' ').split()
                    public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[1]],
                                                    data_time2[0])
                else:
                    data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                    if len(data_time2) == 3:
                        public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]],
                                                        data_time2[1])
                    elif len(data_time2) == 2:
                        public_time = '{}-{}'.format(data_time2[1], time_translate_dict[data_time2[0]])
                    else:
                        public_time = data_time2[0]
            else:
                public_time = '-'
            author = ''.join(response.xpath(
                '//div[@id="single_byline"]/text()').extract()).replace('Published By', '').replace('&nbsp', '').strip()
            column = ','.join(response.xpath('//div[@id="single_meta"]/div[2]//a/text()|\
                //div[@id="single_byline"]/a/text()').extract()).replace('DOWNLOAD', '').strip()
            crawl_time = datetime.datetime.now()
            comment = '-'
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('解析藏人行政中央（藏、英）出错：{}'.format(e)) if self.DEBUG else ''

    # 达赖喇嘛网站 (英文、中文)
    def parse_dalailama(self, response):
        item = ArticlespiderItem()
        try:
            title = ''.join(response.xpath(
                '//div[@class="hideOnNavigation"]/section[1]/div/div/h1/text()').extract()).strip()
            data_time = ''.join(response.xpath(
                '//div[@class="hideOnNavigation"]/section[1]/div/div/h1/span/text()').extract()).strip()
            if data_time:
                data_time2 = data_time.replace(', ', ' ').replace('.', '').replace('，', '').split()
                public_time = '{}-{}-{}'.format(data_time2[2], time_translate_dict[data_time2[0]], data_time2[1])
            else:
                public_time = '-'
            author = 'THE OFFICE OF HIS HOLINESS THE DALAI LAMA'
            column = ','.join(response.xpath(
                '//div[@class="hideOnNavigation"]/section[1]/div/div/ul/li/a/text()').extract()).strip()
            crawl_time = datetime.datetime.now()
            comment = '-'
            item['title'] = title
            item['public_time'] = public_time
            item['author'] = author
            item['column'] = column
            item['crawl_time'] = crawl_time
            item['comment'] = comment
            yield item
        except Exception as e:
            print('达赖喇嘛网站 (英文、中文)出错：{}'.format(e)) if self.DEBUG else ''

    # 西藏流亡政府教育部网站 (英文) # pass
    def parse_tcewf(self, response):
        item = ArticlespiderItem()
        try:
            pass
        except Exception as e:
            print('西藏流亡政府教育部网站 (英文)出错：{}'.format(e)) if self.DEBUG else ''
"""
