# -*- coding:utf-8 -*-
"""
__author__ = "jake"
__email__ = "jakejie@163.com"
FileName = ConfigureRule.py
site: 
version: python3.6
CreateDay:2018/8/27 22:31
"""
XpathRule = {
    # 藏人行政中央（藏、英）
    "1": {
        "domain": "tibet.net",  # 主域名
        "name": "藏人行政中央（藏、英）",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibet.net/2018/08/his-holiness-the-dalai-lama-reiterates-importance-of-middle-way-approach/",
            "http://tibet.net/2009/02/the-kashag-urges-china-to-withdraw-the-undeclared-martial-law-in-tibet/",
            "http://tibet.net/2018/08/psc-announces-7-vacancies-at-office-of-auditor-general-cta/",
            "http://tibet.net/2018/06/fifth-six-month-course-on-tibetan-language-and-buddhist-studies/",
            "http://tibet.net/2018/08/malaysia-cancels-beijing-backed-pipelines-east-coast-rail-link/",
            "http://tibet.net/2018/06/china-rout-has-1023-stocks-plunging-10-in-one-day/",
            "http://tibet.net/2018/04/photo-news-nechung-kuten-rinpoche-visits-oot-washington/",
            "http://tibet.net/2009/01/photo-news-tenshug-for-his-holiness-the-dalai-lama-in-sarnath/",
            "http://tibet.net/2017/04/update-on-the-latest-self-immolation-protest-in-tibet/",
            "http://tibet.net/2015/07/tibetan-monk-burns-self-in-kyegudo-self-immolation-reaches-141/",
            "http://tibet.net/international-resolutions/us-senate-honours-his-holiness-the-dalai-lama-in-unanimous-resolution/",
            "http://tibet.net/international-resolutions/italian-senate-committee-passes-resolution-on-tibet/",
            "http://tibet.net/2013/04/assessment-report-of-the-recent-landslide-event-in-the-gyama-valley/",
            "http://tibet.net/2011/08/glacier-thawing-speeds-up-in-yangtze-river-sources/",
            "http://tibet.net/2016/10/his-holiness-the-dalai-lama-will-be-arriving-in-riga-today/",
            "http://tibet.net/important-issues/factsheet-immolation-2011-2012/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="page-header"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[1]/text()|\
                //main[@id="main-content-main"]/div/p[4]/em/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@id="single_byline"]/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[2]//a/text()|\
                //div[@id="single_byline"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": '-'
        },
    },
    # 西藏之页(中文)
    "2": {
        "domain": "xizang-zhiye.org",  # 主域名
        "name": "西藏之页(中文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://xizang-zhiye.org/藏人行政中央外交与新闻部举办中间道路培训/',
            'http://xizang-zhiye.org/29523-2/',
            'http://xizang-zhiye.org/达赖喇嘛尊者文集-有关教育方面的指示/',
            'http://xizang-zhiye.org/達賴喇嘛在3‧10四十二週年的演說2001-3-10/',
            'http://xizang-zhiye.org/達賴喇嘛在3‧10二十六週年的演說1985-3-10/',
            'http://xizang-zhiye.org/驚聞：西藏夏河再次發生自焚抗議/',
            'http://xizang-zhiye.org/西藏阿坝再次发生藏人抗议事件-据西藏/',
            'http://xizang-zhiye.org/西藏通訊-第一期/',
            'http://xizang-zhiye.org/西藏通訊二零一三年五月至-六月號/',
            'http://xizang-zhiye.org/略倫西藏與滿蒙關係史/',
            'http://xizang-zhiye.org/雪山下的火焰/',
            'http://xizang-zhiye.org/让达赖喇嘛回家/',
            'http://xizang-zhiye.org/西藏比如縣一作家和他的友人被抓/',
            'http://xizang-zhiye.org/中国主张对互联网行使主权/',
            'http://xizang-zhiye.org/中共嚴厲打擊圖伯特佛教的2016年/',
            'http://xizang-zhiye.org/西藏通訊二零一三年五月至-六月號/',
            'http://xizang-zhiye.org/西藏為何燃燒？/',
            'http://xizang-zhiye.org/2009-達賴喇嘛就昂山素季繼續被緬甸當局軟禁發表聲/',
            'http://xizang-zhiye.org/第十四世-達賴喇嘛-聖尊/達賴喇嘛-談佛教的基本見解/',
            'http://xizang-zhiye.org/達賴喇嘛接受bbc國際台專訪/',
            'http://xizang-zhiye.org/第十四世-達賴喇嘛-聖尊/達賴喇嘛-獎項與榮稱一覽表/',
            'http://xizang-zhiye.org/第十四世-達賴喇嘛-聖尊/達賴喇嘛客座《商業周刊》總編輯/',
            'http://xizang-zhiye.org/第十四世-達賴喇嘛-聖尊/達賴喇嘛舉行時輪金剛大法會紀錄表/',
            'http://xizang-zhiye.org/人性與世界和平/',
            'http://xizang-zhiye.org/藏傳佛教疑問解答120題/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//main[@id="main-content-main"]/article/header/div[1]/h1/text()|\
                    //div[@class="page-header"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[1]/text()',
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@id="single_byline"]/text()[2]'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[2]//a/text()|//div[@id="single_byline"]/a[1]/text()',
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": "-"
        },
    },
    # 达赖喇嘛网站(英文、中文)
    "3": {
        "domain": "dalailama.com",  # 主域名
        "name": "达赖喇嘛网站(英文、中文)",  # 网站名称
        # 测试起始地址
        "start_url": ['https://www.dalailama.com/news/2018/tribute-to-senator-john-mccain',
                      'https://www.dalailama.com/news/2018/donation-to-kerala-flood-relief',
                      'https://www.dalailama.com/news/2018/teachings-during-the-great-summer-debate',
                      'https://www.dalailama.com/news/2018/addressing-a-public-gathering-in-kargil',
                      'https://www.dalailama.com/news/2018/visits-to-eliezer-joldan-memorial-college-and-the-imam-barga',
                      'https://www.dalailama.com/news/2018/inauguration-of-the-great-summer-debate',
                      'https://www.dalailama.com/news/2017/three-principal-aspects-of-the-path',
                      'https://www.dalailama.com/pictures/visit-to-the-dalai-lama-institute-of-higher-education',
                      'https://www.dalailama.com/videos/teaching-at-tcv-2015',
                      'https://www.dalailama.com/pictures/meeting-with-five-fifty-youth-forum-participants',
                      'https://www.dalailama.com/pictures/talk-to-college-students-visit-to-chushot-yokma',
                      'https://www.dalailama.com/pictures/final-day-of-teachings-in-leh',
                      'https://www.dalailama.com/pictures/vidyaloke-talks-continue-in-bengaluru',
                      'https://www.dalailama.com/videos/thank-you-karnataka',
                      'https://www.dalailama.com/videos/yarchos-chenmo-2018-inaugural-address',
                      'https://www.dalailama.com/videos/death-as-a-part-of-life',
                      'https://www.dalailama.com/videos/how-to-achieve-long-lasting-happiness',
                      'https://www.dalailama.com/videos/kalachakra-ritual-offering-dance',
                      'https://www.dalailama.com/videos/inner-values-for-a-better-life',
                      'https://www.dalailama.com/videos/inner-peace',
                      'https://www.dalailama.com/videos/moving-towards-global-compassion',
                      'https://www.dalailama.com/videos/vidyaloke-mumbai-teachings',
                      'https://www.dalailama.com/videos/on-world-religion-diversity-not-dissension',
                      'https://www.dalailama.com/videos/bridging-buddhism-science',
                      'https://www.dalailama.com/videos/his-holiness-the-dalai-lama-talks-to-san-diegos-kpbs',
                      'https://www.dalailama.com/videos/inauguration-of-seminar-on-buddhism-in-ladakh',
                      'https://www.dalailama.com/videos/18-great-stages-of-the-path-lam-rim-commentaries-2013',
                      'https://www.dalailama.com/videos/world-peace-and-nonviolence-never-give-up-1',
                      'https://www.dalailama.com/videos/new-years-message',
                      'https://www.dalailama.com/videos/nobel-peace-prize-dayl',
                      ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="hideOnNavigation"]/section[1]/div/div/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="hideOnNavigation"]/section[1]/div/div/h1/span/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@class="hikojko"]/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@class="hideOnNavigation"]/section[1]/div/div/ul/li/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": "-"
        },
    },
    # 西藏流亡政府教育部网站(英文)    # 不能进去
    "4": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "re",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 驻日内瓦办事处信息网(德文)
    "5": {
        "domain": "tibetoffice.ch",  # 主域名
        "name": "驻日内瓦办事处信息网(德文",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibetoffice.ch/2018/08/20/condolences-on-the-passing-away-of-kofi-annan/",
            "http://www.tibetoffice.ch/2018/08/20/cta-president-condoles-demise-of-former-un-secretary-general-kofi-annan/",
            'http://www.tibetoffice.ch/2018/05/09/registration-open-for-five-fifty-youth-forum-shaping-tibets-future/',
            'http://www.tibetoffice.ch/2018/03/26/1691/',
            'http://www.tibetoffice.ch/2018/08/12/his-holiness-the-dalai-lama-gives-talk-on-indian-wisdom-in-the-modern-world/',
            'http://www.tibetoffice.ch/2018/08/14/committee-on-the-elimination-of-racial-discrimination-reviews-the-report-of-china/',
            'http://www.tibetoffice.ch/2018/08/06/tibet-and-india-are-a-family-rss-chief-shri-mohan-bhagwat-to-cta-president/',
            'http://www.tibetoffice.ch/2018/08/06/illegal-in-tibet-middle-way-mother-tongue-welfare-groups/',
            'http://www.tibetoffice.ch/2018/04/24/chinas-new-genetic-project-for-the-mass-surveillance-in-tibet/',
            'http://www.tibetoffice.ch/2018/04/11/with-its-latest-human-rights-council-resolution-china-continues-its-assault-on-the-un-human-rights-framework/',
            'http://www.tibetoffice.ch/application-of-green-book-swiss/',
            'http://www.tibetoffice.ch/visa-application-for-india/',
            'http://www.tibetoffice.ch/certificate/',
            'http://www.tibetoffice.ch/290-2/',
            'http://www.tibetoffice.ch/2013/04/17/hello-world-2/',
            'http://www.tibetoffice.ch/2017/03/29/sikyong-speaks-to-members-of-swiss-parliament/',
            'http://www.tibetoffice.ch/2018/01/26/1401/',
            'http://www.tibetoffice.ch/2018/03/30/representative-ngodup-dorjee-meet-with-czech-member-of-parliament-and-senators/',
            'http://www.tibetoffice.ch/2018/06/04/picture-story-of-sikyongs-meeting-with-tibetan-community-in-berlin-may-2018/',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@itemprop="headline"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="w-blog-post-meta"]/time/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ''
        },
        # 栏目
        "column": {
            "type": 'xpath',
            "rule": '//li[@class="menu-item menu-item-type-taxonomy menu-item-object-category current-post-ancestor current-menu-parent current-post-parent w-nav-item level_1 menu-item-1164"]/a/span[1]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 驻纽约代表处信息网(英文)
    "6": {
        "domain": "tibetoffice.org",  # 主域名
        "name": "驻纽约代表处信息网(英文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
            "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
            "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
            "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
            "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
            "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
            "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
            "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
            "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
            "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
            "http://tibetoffice.org/media-press/2016-tibetan-election",
            "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
            "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
            "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
            "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
            "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
            "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
            "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
            "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
            "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
            "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
            "http://tibetoffice.org/media-press/2016-tibetan-election",
            'http://tibetoffice.org/media-press/news/seeing-science-through-a-spiritual-lens',
            'http://tibetoffice.org/media-press/march10/tibet-day-proclamation-vermont',
            'http://tibetoffice.org/media-press/march10/march-10th-chronicles-san-francisco-bay-area',
            'http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul',
            'http://tibetoffice.org/media-press/events/tcv-summer-camp',
            'http://tibetoffice.org/media-press/news/tibetan-culture-immersion-summer-program-india-tibetan-youths',
            'http://tibetoffice.org/media-press/news/university-rochesters-tibetan-innovation-challenge',
            'http://tibetoffice.org/media-press/events/2016-tcv-summer-camp',
            'http://tibetoffice.org/media-press/commentaries-opinions/four-china-political-trends-to-watch-in-2011',
            'http://tibetoffice.org/media-press/commentaries-opinions/less-snow-in-tibet-means-more-heatwaves-in-europe',
            'http://tibetoffice.org/media-press/commentaries-opinions/tibet-cant-kick-its-subsidy-habit',
            'http://tibetoffice.org/picture-slide-shows/hhdl-congressional-delegation-dharamsala-2017',
            'http://tibetoffice.org/picture-slide-shows/holiness-dalai-lama-visiting-starkey-hearing-facilities-addressing-2000-starkey-employees-minnesota-june-22nd-morning',
            'http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3',
            'http://tibetoffice.org/media-press/2016-tibetan-election',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="post-inner"]/h1/span/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="post-inner"]/p/span[1]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ''
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="post-cats"]/a/text()|//div[@class="post-inner"]/p/span[2]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ''
        },
    },
    # 驻伦敦代表处信息网(英文)   # 和第一个一样
    "7": {
        "domain": "tibet.net",  # 主域名
        "name": "藏人行政中央（藏、英）",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibet.net/2018/08/his-holiness-the-dalai-lama-reiterates-importance-of-middle-way-approach/",
            "http://tibet.net/2009/02/the-kashag-urges-china-to-withdraw-the-undeclared-martial-law-in-tibet/",
            "http://tibet.net/2018/08/psc-announces-7-vacancies-at-office-of-auditor-general-cta/",
            "http://tibet.net/2018/06/fifth-six-month-course-on-tibetan-language-and-buddhist-studies/",
            "http://tibet.net/2018/08/malaysia-cancels-beijing-backed-pipelines-east-coast-rail-link/",
            "http://tibet.net/2018/06/china-rout-has-1023-stocks-plunging-10-in-one-day/",
            "http://tibet.net/2018/04/photo-news-nechung-kuten-rinpoche-visits-oot-washington/",
            "http://tibet.net/2009/01/photo-news-tenshug-for-his-holiness-the-dalai-lama-in-sarnath/",
            "http://tibet.net/2017/04/update-on-the-latest-self-immolation-protest-in-tibet/",
            "http://tibet.net/2015/07/tibetan-monk-burns-self-in-kyegudo-self-immolation-reaches-141/",
            "http://tibet.net/international-resolutions/us-senate-honours-his-holiness-the-dalai-lama-in-unanimous-resolution/",
            "http://tibet.net/international-resolutions/italian-senate-committee-passes-resolution-on-tibet/",
            "http://tibet.net/2013/04/assessment-report-of-the-recent-landslide-event-in-the-gyama-valley/",
            "http://tibet.net/2011/08/glacier-thawing-speeds-up-in-yangtze-river-sources/",
            "http://tibet.net/2016/10/his-holiness-the-dalai-lama-will-be-arriving-in-riga-today/",
            "http://tibet.net/important-issues/factsheet-immolation-2011-2012/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="page-header"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[1]/text()|\
                //main[@id="main-content-main"]/div/p[4]/em/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@id="single_byline"]/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="single_meta"]/div[2]//a/text()|\
                //div[@id="single_byline"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": '-'
        },
    },
    # 驻东京代表处信息网(日文)
    "8": {
        "domain": "tibethouse.jp",  # 主域名
        "name": "驻东京代表处信息网(日文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibethouse.jp/news_release/2018/180820_HHDL_20180811.html",
            "http://www.tibethouse.jp/news_release/2010/101025_protest.html",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="main"]/div/h2/text()',
        },
        # 发布时间
        "public_time": {
            "type": "re",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@class="translate"]/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="path"]/a[2]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ''
        },
    },
    # 驻台北办事处信息网(中文)
    "9": {
        "domain": "tibet.org.tw",  # 主域名
        "name": "驻台北办事处信息网(中文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibet.org.tw/news_detail.php?news_id=9690",
            "http://www.tibet.org.tw/news_detail.php?news_id=9675",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//p[@class="t11"]/strong/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//td[@class="style3"]/blockquote/div/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="style2_title"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 驻莫斯科代表处信息网(俄文)
    "10": {
        "domain": "savetibet.ru",  # 主域名
        "name": "驻莫斯科代表处信息网(俄文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://savetibet.ru/2018/08/21/drepung-gomang.html",
            "http://savetibet.ru/2018/08/18/dalai-lama-14.html",
            'http://savetibet.ru/2006/12/06/woser_exhibition.html',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="text-02"]/div/h1[1]/text()|\
                //div[@class="text-02"]/div/h1[1]/font/font/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="dle-content"]/div[1]/font/font/text()|\
                //div[@class="news-big-01"]/font/font/text()|\
                //*[@id="dle-content"]/div[1]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ''
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//form[@id="dlemasscomments"]/div'
        },
    },
    # 欧盟联络处信息网(法文)    # 打开里面不知道提取啥
    "11": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "re",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 中南美洲联络处信息网(西班牙文)      #和第六个一样
    "12": {
        "domain": "tibetoffice.org",  # 主域名
        "name": "中南美洲联络处信息网(西班牙文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
            "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
            "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
            "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
            "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
            "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
            "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
            "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
            "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
            "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
            "http://tibetoffice.org/media-press/2016-tibetan-election",
            "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
            "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
            "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
            "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
            "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
            "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
            "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
            "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
            "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
            "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
            "http://tibetoffice.org/media-press/2016-tibetan-election",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//article[@id="the-post"]/div[2]/h1/span/text()|\
                //h1[@class="name post-title entry-title"]/span/text()|\
                //div[@class="post-inner"]/h1/span/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//article[@id="the-post"]/div[2]/p/span[1]/text()|\
                //div[@class="post-inner"]/p/span[1]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//article[@id="the-post"]/div[2]/p/span[2]/a/text()|\
                //span[@class="post-cats"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 驻堪培拉代表处信息网(英文)          #没解析
    "13": {
        "domain": "tibetoffice.com.au",  # 主域名
        "name": "驻堪培拉代表处信息网(英文)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetoffice.com.au/his-holiness-the-dalai-lama-offers-condolences-at-death-of-senator-john-mccain/",
            "http://tibetoffice.com.au/in-a-first-office-of-tibet-dc-organises-secular-ethics-and-youth-leadership-workshop/",
            "http://tibetoffice.com.au/china-and-russia-strengthening-relationship-in-bid-to-thwart-us-dominance/",
            'http://tibetoffice.com.au/further-reading/important-documents/',
            'http://tibetoffice.com.au/further-reading/tio-newsletters/',
            'http://tibetoffice.com.au/protected-area-permit/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@class="entry-meta-date updated"]/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//span[@class="entry-meta-author vcard author"]/a/text()'
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 藏医历算学院
    "14": {
        "domain": "men-tsee-khang.org",  # 主域名
        "name": "藏医历算学院",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.men-tsee-khang.org/new-news/2018/His%20holiness%20visit%20to%20bengaluru/his%20holiness%20visit.html",
            "http://www.men-tsee-khang.org/new-news/2018/Ladakh%20health%20talk%20august/ladakh%20healthtalk.html",
            "http://www.men-tsee-khang.org/new-news/2018/kunphen/kunphen.html",
            'http://www.men-tsee-khang.org/new-news/2018/ladakh%20tuberclosis%20program/ladakh.html',
            'http://www.men-tsee-khang.org/new-news/2018/zanskar_new/medical%20camp.html',
            'http://www.men-tsee-khang.org/new-news/2018/Dr.%20Namdon%20lhamo%20and%20Russian%20Scientist/namdon%20lhamo.html',
            'http://www.men-tsee-khang.org/new-news/2018/ladakh%20health%20day/ladakh%20health%20day%20celebration.html'

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="welcomeBar"]/p[2]/text()|\
            //div[@id="welcomeBar"]/p[2]/strong/text()|\
            //div[@id="div"]/div/p[1]/text()|\
            //span[@class="main"]/strong/text()|\
            //span[@class="head4"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 西藏视讯电视网   # 跳转到youtube
    "15": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "re",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 罗布尔卡西藏文化中心   #
    "16": {
        "domain": "norbulingka.org",  # 主域名
        "name": "罗布尔卡西藏文化中心",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://www.norbulingka.org/store/p177/Tibetan_Mastiff_T-shirt-black_.html",
            "https://www.norbulingka.org/store/p59/Chocolate_Buray_Shawl.html",
            "https://www.norbulingka.org/store/p59/Chocolate_Buray_Shawl.html",
            "https://www.norbulingka.org/store/p61/Mustard_Buray_Shawl.html",
            "https://www.norbulingka.org/store/c18/Children.html",
            "https://www.norbulingka.org/store/p83/Amethyst_Mala.html",
            'https://www.norbulingka.org/store/p180/Tibetan_Mastiff_T-shirt-_white.html',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h2[@id="wsite-com-product-title"]/text()|//h2[@id="wsite-com-title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//ul[@id="wsite-com-breadcrumbs"]/li[3]/a/span/text()|\
            //h2[@id="wsite-com-title"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 西藏表演艺术学院(TIPA)
    "17": {
        "domain": "tibetanarts.org",  # 主域名
        "name": "西藏表演艺术学院(TIPA)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibetanarts.org/accessories-3/",
            "http://www.tibetanarts.org/tingshaw/",
            "http://www.tibetanarts.org/lathed-tibetan-singing-bowl-3-75-9cm-taomm375/",
            "http://www.tibetanarts.org/buddhas-cast-bowl-5-13cm-taobuddha5/",
            "http://www.tibetanarts.org/classic-frosted-quartz-singing-bowl-9-432-hz-g-throat-chakra-c9gm30/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="DetailRow"]/h1/text()|\
            //div[@id="CategoryHeading"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="ProductBreadcrumb"]/ul/li[2]/a/text()|\
            //div[@id="CategoryBreadcrumb"]/ul/li[2]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 西藏文献图书馆
    "18": {
        "domain": "tibetanlibrary.org",  # 主域名
        "name": "西藏文献图书馆",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetanlibrary.org/20th-august-2018-thai-monks-completed-their-course-at-ltwa/",
            "http://tibetanlibrary.org/17th-august-2018-condolence-prayer/",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="post-inner"]/h1/span/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//article[@id="the-post"]/div[2]/p/span[1]/text()|\
                //div[@class="post-inner"]/p/span[1]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="post-cats"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 达兰萨拉西藏儿童村(TCV)
    "19": {
        "domain": "tibchild.org",  # 主域名
        "name": "达兰萨拉西藏儿童村(TCV)",  # 网站名称
        # 测试起始地址
        "start_url": ["http://www.tibchild.org/category/borrower/",
                      "http://www.tibchild.org/category/cash-back-offer/",

                      ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//a[@rel="bookmark"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@class="year"]/text()|//span[@class="month"]/text()|//span[@class="date-structure"]/h2/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="cat-links"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//span[@class="comments-link"]/a/text()'
        },
    },
    # 桑波扎西藏完全学校
    "20": {
        "domain": "sambhota.org/",  # 主域名
        "name": "桑波扎西藏完全学校",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://sambhota.org/tibetan/default.html",
            "http://sambhota.org/book-lekshey-tamgyu-1-12/",
            "http://sambhota.org/book-rinpoche-diologue-with-petoen-students/",
            "http://sambhota.org/tibetan/Quiz_dl2.html",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="post_title single"]/span/a/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//li[@class="post_date"]/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//li[@class="posted_by"]/a/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="post_category"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//li[@class="post_comment"]/span/a/text()'
        },
    },
    # 达赖喇嘛官方华文网站
    "21": {
        "domain": "dalailamaworld.com",  # 主域名
        "name": "达赖喇嘛官方华文网站",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.dalailamaworld.com/topic.php?t=1039&sid=dbfb0147349ad3622758197dc30ef1dd",
            "http://www.dalailamaworld.com/topic.php?t=1038&sid=dbfb0147349ad3622758197dc30ef1dd",
            "http://www.dalailamaworld.com/topic.php?t=1037&sid=dbfb0147349ad3622758197dc30ef1dd",
            "http://www.dalailamaworld.com/topic.php?t=1035&sid=dbfb0147349ad3622758197dc30ef1dd",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="subject_bg1 nav"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "re",
            "rule": ''
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//a[@class="cattitle"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 国际声援西藏中心
    "22": {
        "domain": "savetibet.org",  # 主域名
        "name": "国际声援西藏中心",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.savetibet.org/chinese-courts-decision-to-uphold-tashi-wangchuks-prison-sentence-is-a-travesty-of-justice-ict-says/",
            "http://www.savetibet.org/international-campaign-for-tibets-oral-statement-at-the-un-cerd-96th-session-in-geneva-on-august-7-2018/",
            "http://www.savetibet.org/ict-urges-unesco-to-look-into-the-destruction-of-dalai-lamas-parents-home-in-tibet/",
            "http://www.savetibet.org/rowell-fund-2019/",
            "http://www.savetibet.org/about-ict/what-we-do/",
            'https://weblog.savetibet.org/2018/07/in-memoriam-nicole-rowell-ryan/',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()|\
            //div[@id="main"]/div[1]/h1/text()|\
            //h1[@class="title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@class="updated"]/text()|\
            //abbr[@class="date time published"]/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@class="meta-item author"]/span/span/a/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@class="post-meta"]/span/span/a/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//div[@class="meta-item comments"]/a/text()'
        },
    },
    # 西藏人权民主促进会
    "23": {
        "domain": "tchrd.org",  # 主域名
        "name": "西藏人权民主促进会",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tchrd.org/annual-report-2014-human-rights-situation-in-tibet/",
            "http://tchrd.org/un-committee-seeks-additional-information-from-china-on-elimination-of-racial-discrimination/",
            "http://tchrd.org/china-deploys-security-forces-to-prevent-tibetans-from-protesting-water-diversion-project/",
            "http://tchrd.org/two-tibetans-convicted-for-inciting-separatism-released-after-serving-long-prison-terms/",
            "http://tchrd.org/tchrd-releases-2013-annual-report-and-special-report-on-re-education-through-labor/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="post-inner"]/h1/span/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="post-inner"]/p/span[1]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="post-cats"]/a/text()|\
            //div[@class="post-inner"]/p/span[2]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 西藏青年会    #  打不开
    "24": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "re",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 西藏自由运动组织  #  打不开
    "25": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "re",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 藏人创业发展计划  ##jia
    "26": {
        "domain": "tibetanentrepreneurs.org",  # 主域名
        "name": "藏人创业发展计划",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://tibetanentrepreneurs.org/2016/06/30/ted-entrepreneurs-participate-in-business-plan-competition/',
            'http://tibetanentrepreneurs.org/2015/08/31/game-changers-conference-underway/',
            'http://tibetanentrepreneurs.org/ted-investment-award/',
            'http://tibetanentrepreneurs.org/2015/09/03/ted-awards-four-rising-tibetan-entrepreneurs-with-investment-award/',
            'http://tibetanentrepreneurs.org/2015/08/31/game-changers-conference-underway/',
            'http://tibetanentrepreneurs.org/game-changers-conference-2/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title fusion-post-title"]/text()|\
                //h1[@style="text-align: center;"]/text()|\
                //div[@class="fusion-text"]/h1/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="fusion-meta-info-wrapper"]/span[3]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="menu-item menu-item-type-post_type menu-item-object-page current-menu-ancestor current-menu-parent current_page_parent current_page_ancestor menu-item-has-children menu-item-13160 fusion-dropdown-menu"]/a/span/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 欧洲西藏青年协会   ##jia
    "27": {
        "domain": "vtje.org",  # 主域名
        "name": "欧洲西藏青年协会",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://vtje.org/en/news_container/news/podiumsdiskussion-chinas-langer-schatten/',
            'http://vtje.org/en/news_container/news/vtje-kinderlager-2018/',
            'http://vtje.org/en/activities/events/rap-for-tibet/',
            'http://vtje.org/en/activities/education/shenpen/',
            'http://vtje.org/en/activities/culture/tibet-film-festival/',
            'http://vtje.org/en/activities/action-and-campaigns/put-tibet-back-map/',
            'http://vtje.org/en/activities/culture/religion/',
            'http://vtje.org/en/activities/action-and-campaigns/deine-stimme-entscheidet/',
            'http://vtje.org/en/take-action/become-member/',
            'http://vtje.org/en/take-action/support-us/',
            'http://vtje.org/en/calender/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="col-sm-12"]/h2/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//time[@class="listing-hero-date"]/@datetime'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//ol[@class="breadcrumb"]/li[2]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 西藏妇女联合会
    "28": {
        "domain": "tibetanwomen.org",  # 主域名
        "name": "西藏妇女联合会",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetanwomen.org/the-four-major-ngos-from-dharamsala-has-organised-a-peaceful-cycle-rally-from-mcleod-ganj-main-square-to-norbulingka-to-commemorate-the-2008-national-uprising-in-tibet/",
            "http://tibetanwomen.org/women-in-tibet/",
            "http://tibetanwomen.org/books-reports/",
            "http://tibetanwomen.org/support/intern/",
            "http://tibetanwomen.org/newsletters/",
            "http://tibetanwomen.org/history/",
            "http://tibetanwomen.org/team/",
            "http://tibetanwomen.org/the-four-ngos-also-organised-a-similar-cycle-rally-at-delhi-starting-from-tibetan-camp-manju-ka-tilla-to-indian-parliament-street-with-the-sincere-participations-of-the-50-students-from-delhi-colleges/",
            "http://tibetanwomen.org/category/b-key-activities/4-research-media/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="post-title entry-title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@class="year"]/text()|//span[@class="month"]/text()|//span[@class="day"]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//ul[@class="post-meta"]/li/span/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 北美科罗拉多藏人协会  ##jia
    "29": {
        "domain": "coloradotibetans.org",  # 主域名
        "name": "北美科罗拉多藏人协会",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://coloradotibetans.org/?page_id=40',
            'https://www.eventbrite.com/e/denver-home-show-april-12th-14th-2019-tickets-45767553986?aff=erelexpmlt',
            'https://www.eventbrite.com/e/2018-denver-tequila-taco-cerveza-fest-at-mile-high-station-tickets-43455777400?aff=erelexpmlt',
            'http://coloradotibetans.org/?event=losar-2018',
            'http://coloradotibetans.org/?event=2017-sikyong-visit',
            'http://coloradotibetans.org/?gallery=candle-light-vigil',
            'http://coloradotibetans.org/?page_id=31',
            'http://coloradotibetans.org/?page_id=530',
            'http://coloradotibetans.org/?page_id=463',
            'http://coloradotibetans.org/?page_id=74',
            'http://coloradotibetans.org/?page_id=323'
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()|//h1[@class="listing-hero-title"]/text()|\
                //h1[@class="home_page_title entry-header"]/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//time[@class="listing-hero-date"]/@datetime'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="menu-item menu-item-type-post_type menu-item-object-page current-menu-ancestor current-menu-parent current_page_parent current_page_ancestor menu-item-has-children menu-item-79"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 自由亚洲电台藏区局势  ##jia
    "30": {
        "domain": "rfa.org",  # 主域名
        "name": "自由亚洲电台藏区局势",  # 网站名称
        # 测试起始地址
        "start_url": [
            'https://www.rfa.org/mandarin/yataibaodao/shaoshuminzu/gf1-01042018102108.html',
            'https://www.rfa.org/mandarin/yataibaodao/jingmao/gf2-08272018103001.html',
            'https://www.rfa.org/mandarin/yataibaodao/jingmao/gr-12232013100905.html',
            'https://www.rfa.org/mandarin/yataibaodao/zhengzhi/ql1-08232018101012.html',
            'https://www.rfa.org/mandarin/yataibaodao/zhengzhi/cyl-12312013141310.html',
            'https://www.rfa.org/mandarin/yataibaodao/renquanfazhi/wy-08272018104518.html',
            'https://www.rfa.org/mandarin/yataibaodao/renquanfazhi/nu-12312013141729.html',
            'https://www.rfa.org/mandarin/yataibaodao/meiti/nu-08222018105655.html',
            'https://www.rfa.org/mandarin/yataibaodao/meiti/vt-12312013142131.html',
            'https://www.rfa.org/mandarin/yataibaodao/shehui/ql2-08242018100409.html',
            'https://www.rfa.org/mandarin/yataibaodao/shehui/hc-12312013135150.html',
            'https://www.rfa.org/mandarin/yataibaodao/huanjing/nu-08232018110012.html',
            'https://www.rfa.org/mandarin/yataibaodao/huanjing/yf1-12302013100043.html',
            'https://www.rfa.org/mandarin/yataibaodao/junshiwaijiao/ko-08282018095701.html',
            'https://www.rfa.org/mandarin/yataibaodao/junshiwaijiao/nz-12312013134220.html',
            'https://www.rfa.org/mandarin/yataibaodao/kejiaowen/hj-07232018110732.html',
            'https://www.rfa.org/mandarin/yataibaodao/kejiaowen/zaa-12302013113936.html',
            'https://www.rfa.org/mandarin/pinglun/weise/ws-08252018135725.html',
            'https://www.rfa.org/mandarin/duomeiti/huandengtuji/biantailajiaomanhua/biantailajiao-08212018161743.html',
            'https://www.rfa.org/mandarin/duomeiti/yatailianbo/yt-12312013162154.html',
            'https://www.rfa.org/mandarin/zhuanlan/laobaixingdeshengyin/people-08272018120154.html',
            'https://www.rfa.org/mandarin/zhuanlan/laobaixingdeshengyin/m1231people-12312014124017.html',
            'https://www.rfa.org/mandarin/yataibaodao/junshiwaijiao/gf2-07302018100153.html',
            'https://www.rfa.org/mandarin/pinglun/liudi/ld-07302018165238.html',
            'https://www.rfa.org/mandarin/video?v=1_jgvjfhhp',
            'https://www.rfa.org/mandarin/video?v=1_eftj9a39',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="storypagemaincol"]/h1/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="story_date"]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="current-section"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//div[@id="commentcount"]/span[2]/text()'
        },
    },
    # 妙宗班智达翻译小组会
    "31": {
        "domain": "",  # 主域名
        "name": "",  # 网站名称
        # 测试起始地址
        "start_url": [

        ],
        # 标题
        "title": {
            "type": "",
            "rule": "",
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 加拿大西藏同乡会
    "32": {
        "domain": "tibet.ca",  # 主域名
        "name": "加拿大西藏同乡会",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibet.ca/en/activism/events/233",
            "http://www.tibet.ca/en/library/wtn/14005",
            "http://www.tibet.ca/en/library/wtn/14008",
            "http://www.tibet.ca/en/library/media_releases/445",
            "http://www.tibet.ca/en/library/media_releases/444",
            "http://www.tibet.ca/en/library/photo_archive",
            "http://www.tibet.ca/en/library/newsletter",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="column_main"]/div/h1[1]/text()|\
                //div[@id="column_main"]/div/div[1]/h1[1]/text()|\
                //div[@class="upcoming_events"]/div[1]/h1[1]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="upcoming_events"]/div[1]/text()|\
            //div[@id="text"]/div/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 国际声援西藏运动ICT比利时      ##jia
    "33": {
        "domain": "savetibet.fr",  # 主域名
        "name": "国际声援西藏运动ICT比利时",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://www.tibetpolicy.eu/mass-migration-program-highlights-contested-nomads-resettlement-policies-in-tibet/',
            'http://www.tibetpolicy.eu/international-campaign-for-tibets-oral-statement-at-the-un-cerd-96th-session-in-geneva-on-august-7-2018/',
            'http://www.tibetpolicy.eu/denials-smokescreens-and-misleading-information-chinese-government-attempts-to-distort-its-record-on-tibet-at-un-committee-hearing-on-13-august-2018/',
            'http://www.tibetpolicy.eu/european-parliament-calls-for-the-release-of-nobel-laureate-liu-xiaobo-and-regrets-that-failure-of-the-eu-to-deliver-an-item-4-statement-at-the-uns-human-rights-council/',
            'http://www.tibetpolicy.eu/chinese-courts-decision-to-uphold-tashi-wangchuks-prison-sentence-is-a-travesty-of-justice-ict-says/',
            'http://www.tibetpolicy.eu/tibetan-language-rights-advocate-tashi-wangchuk-sentenced-to-five-years-in-prison/',
            'http://www.tibetpolicy.eu/british-premier-phones-chinese-premier-on-tibet-development-says-will-meet-dalai-lama-during-london-visit/',
            'http://www.tibetpolicy.eu/tibet-brief-edition-64/',
            'http://www.tibetpolicy.eu/tibet-brief-edition-01-2/',
            'http://www.tibetpolicy.eu/destruction-commercialization-fake-replicas-new-report-on-lhasa-as-unesco-world-heritage-committee-meets/',
            'http://www.tibetpolicy.eu/un-special-rapporteur-on-tortures-2005-china-mission-report-excerpts-on-tibet-march-2006/',
            'http://www.tibetpolicy.eu/self-immolations/',
            'http://www.tibetpolicy.eu/religious-repression-in-tibet/',
            'http://www.tibetpolicy.eu/serf-day/',
            'http://www.tibetpolicy.eu/tiananmen-and-tibet-ict-analysis/',
            'http://www.tibetpolicy.eu/policy-center/recommendations/',
            'http://www.tibetpolicy.eu/category/policy-center/central-tibetan-administration/',
            'http://www.tibetpolicy.eu/dr-lobsang-sangays-statement-on-the-54th-anniversary-of-the-tibetan-uprising-day/',
            'http://www.tibetpolicy.eu/where-is-china-heading-on-tibet-remarks-by-lodi-gyaltsen-gyari-to-the-council-on-foreign-relations-washington-dc-april-23-2012/',
            'http://www.tibetpolicy.eu/note-on-the-memorandum-on-genuine-autonomy-for-the-tibetan-people/',
            'http://www.tibetpolicy.eu/european-parliament-resolutions-2000-2016/',
            'http://www.europarl.europa.eu/sides/getDoc.do?type=TA&reference=P7-TA-2012-0503&language=EN&ring=A7-2012-0377',
            'http://www.europarl.europa.eu/sides/getDoc.do?pubRef=-//EP//TEXT+TA+P5-TA-2000-0026+0+DOC+XML+V0//EN&language=EN',
            'http://www.tibetpolicy.eu/category/policy-center/european-union-institutions/eu-council-eu-presidency/',
            'http://www.tibetpolicy.eu/remarks-by-president-donald-tusk-after-the-19th-eu-china-summit/',
            'http://www.tibetpolicy.eu/declaration-by-the-presidency-on-behalf-of-the-european-union-regarding-the-recent-executions-of-two-tibetans/',
            'http://www.tibetpolicy.eu/international-campaign-for-tibets-oral-statement-at-the-un-cerd-96th-session-in-geneva-on-august-7-2018/',
            'http://www.tibetpolicy.eu/un-human-rights-council-publishes-written-statement-on-discrimination-in-tibet/',
            'http://www.tibetpolicy.eu/state-media-confirms-xi-jinping-in-lhasa-for-celebrations/',
            'http://www.tibetpolicy.eu/religious-repression-in-tibet/',
            'http://www.tibetpolicy.eu/statement-by-the-ict-on-recent-events-in-tibet/',
            'http://www.tibetpolicy.eu/striking-hard-torture-in-tibet/',
            'http://www.tibetpolicy.eu/monk-in-tibet-sets-himself-on-fire-shot-by-police-during-protest/',
            'http://www.tibetpolicy.eu/the-question-of-tibet-and-the-rule-of-law-1959-and-1960/',
            'http://www.tibetpolicy.eu/fire-in-the-land-of-snow-self-immolations-in-tibet/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@class="entry-date"]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="breadcrumbs"]/a[2]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 家乡(英)
    "34": {
        "domain": "phayul.com",  # 主域名
        "name": "家乡(英)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.phayul.com/news/article.aspx?id=40695&article=Two+Tibetans+released+from+prison%2c+both+served+sentence+for+%E2%80%9Cinciting+separatism%E2%80%9D",
            "http://www.phayul.com/news/article.aspx?c=8&t=1&id=39353&article=The+Paradox+of+Samsara%2c+Review+of+%E2%80%9CJigden%3a+The+Beginning+of+the+End%E2%80%9D",
            "http://www.phayul.com/news/article.aspx?id=40711&article=Pro-Tibet+groups+slam+Google+over+plans+to+develop+censored+search+engine+in+China",
            "http://www.phayul.com/news/article.aspx?id=40715&article=Middle+school+students+in+Occupied-Tibet+forced+to+undergo+military+training",
            'http://www.phayul.com/news/article.aspx?id=26561&article=Sarkozy+visit+%27delights%27+China&t=1&c=1',
            'http://www.phayul.com/news/article.aspx?id=26607&article=China+government%27s+undesired+websites+unveiled&t=1&c=1',
            'http://www.phayul.com/news/article.aspx?id=26589&article=Upto+30K+Yuan+as+reward+for+festive+losar&t=1&c=1',
            'http://www.phayul.com/news/article.aspx?id=26558&article=Losar+bringing+Tibetans+closer&t=1&c=1'],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//span[@id="_ctl1_lblHeading"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@id="_ctl1_lblDate"]/text()'
        },
        # 作者
        "author": {
            "type": "re",
            "rule": ''
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//td[@class="newsDiscussionMessage"]/table/tr'
        },
    },
    # 西藏之声
    "35": {
        "domain": "vot.org",  # 主域名
        "name": "西藏之声",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://www.vot.org/", "https://www.vot.org/ལྷ་ས་གྲོང་ཁྱེར་ནང་སློབ1/'
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//main[@class="main col-sm-9"]/div[1]/article/header/h1/text()|\
                //div[@class="page"]/article/header/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="page"]/article/header/div/time/text()|\
                //time[@class="published updated"]/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="vcard author"]/span/text()|\
                //span[@class="fn"]/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": ""
        },
    },
    # 国际声援西藏运动ICT德国   ##jia
    "36": {
        "domain": "savetibet.de",  # 主域名
        "name": "国际声援西藏运动ICT德国",  # 网站名称
        # 测试起始地址
        "start_url": [
            'https://savetibet.de/kampagnen/online-petition/petition-tibeter-in-nepal2012/',
            'https://savetibet.de/kampagnen/tibet-im-fokus-bundestagswahlen-2017/',
            'https://savetibet.de/kampagnen/online-petition/keine-gedankenkontrolle/#c10627',
            'https://savetibet.de/kampagnen/online-petition/petition-meinungsfreiheit/',
            'https://savetibet.de/kampagnen/online-petition/kirti/',
            'https://savetibet.de/kampagnen/online-petition/folterstoppen-seite/',
            'https://savetibet.de/kampagnen/online-petition/folterstoppen-seite/',
            'https://savetibet.de/kampagnen/online-petition/',
            'https://savetibet.de/kampagnen/urgent-appeals/panchen-lama00/',
            'https://savetibet.de/ict/',
            'https://savetibet.de/tibet/umwelt/',
            'https://savetibet.de/kampagnen/online-petition/petition-religionsfreiheit2011/menschenrechte0/',
            'https://savetibet.de/tibet/sino-tibetischer-dialog/',
            'https://savetibet.de/tibet/menschenrechte/',
            'https://savetibet.de/spenden/foerdern/',
            'https://savetibet.de/mediathek/bildergalerien/bildergalerie1/wahlen-exilparlament/',
            'https://savetibet.de/mediathek/publikationen/',
            'https://savetibet.de/mediathek/publikationen/tibet-journal/',
            'https://savetibet.de/mediathek/videos/',
            'https://savetibet.de/tibet/umwelt/',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="inhalte"]/h1/text()'
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@class="rootline"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 为西藏而拍      ##jia
    "37": {
        "domain": "filmingfortibet.org",  # 主域名
        "name": "为西藏而拍",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://www.filmingfortibet.org/2013/06/21/dhondup-wangchen-awarded-with-freedom-award/',
            'http://www.filmingfortibet.org/2014/06/05/tibetan-filmmaker-dhondup-wangchen-released-from-prison/',
            'http://www.filmingfortibet.org/2018/02/12/tibetans-have-not-given-up-their-struggle-for-freedom/',
            'http://www.filmingfortibet.org/2011/10/31/the-rise-in-tibetan-video-activism/',
            'http://www.filmingfortibet.org/2010/05/06/message-of-support-from-filmmaker-ken-loach/',
            'http://www.filmingfortibet.org/2011/05/01/amnesty-international-events-in-support-of-dhondup-wangchen/',
            'http://www.filmingfortibet.org/projects/leaving-fear-behind/',
            'http://www.filmingfortibet.org/projects/tibet-film-festival/',
            'http://www.filmingfortibet.org/projects/imprisoned/',
            'http://www.filmingfortibet.org/2012/11/30/filming-for-tibet-contests-the-official-arrest-order-for-jigme-gyatso-missing-since-september-2012/',
            'http://www.filmingfortibet.org/2011/07/10/tibet-film-festival/',
            'http://www.filmingfortibet.org/2018/02/09/tibetan-activist-dhondup-wangchen-to-testify-before-united-states-congress/',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()|//div[@class="headline_area"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//abbr[@class="published"]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 台湾自由图博|西藏学会  ##jia
    "38": {
        "domain": "sft-taiwan.blogspot.com",  # 主域名
        "name": "台湾自由图博|西藏学会",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://sft-taiwan.blogspot.com/2014/06/blog-post.html',
            'http://sft-taiwan.blogspot.com/2014/02/blog-post.html',
            'http://sft-taiwan.blogspot.com/2014/06/blog-post.html',
            'http://sft-taiwan.blogspot.com/2013/09/unite-for-tibet.html'
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h3[@class="post-title entry-title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//h2[@class="date-header"]/span/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//span[@class="post-author vcard"]/span/a/span/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//span[@class="pot-author vcard"]/font/span/a/span/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 大宝法王噶玛巴中文网站
    "39": {
        "domain": "kagyuoffice.org.tw",  # 主域名
        "name": "大宝法王噶玛巴中文网站",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://www.kagyuoffice.org.tw/karmapa-office/announcement/announcement-20080805",
            "https://www.kagyuoffice.org.tw/karmapa-office/announcement/20130801",
            "https://www.kagyuoffice.org.tw/karmapa-office/announcement/20151208",
            "https://www.kagyuoffice.org.tw/karmapa-office/announcement/announcement-19921203",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="item-page"]/h2/a/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="item-page"]/p[1]/text()[1]'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//dd[@class="gj-category-name"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 达兰萨拉利众中心
    "40": {
        "domain": "kunphen.center",  # 主域名
        "name": "达兰萨拉利众中心",  # 网站名称
        # 测试起始地址
        "start_url": [

            "http://kunphen.center/activities-at-kunphen-center/awarenes-and-fundraise-event/",
            "http://kunphen.center/whats-happening-at-kunphen-center/plantation-by-boys-at-the-new-rahab-site/",
            "http://kunphen.center/activities-at-kunphen-center/world-hepatitis-day-28th-july-2017/",
            "http://kunphen.center/whats-happening-at-kunphen-center/hhdl-praises-kunphen-center/",
            "http://kunphen.center/whats-happening-at-kunphen-center/client-gets-married/",
            "http://kunphen.center/client-stories/",
            "http://kunphen.center/about-kunphen-center-dharamsala/kunphen-center-magazine-2017/",
            "http://kunphen.center/activities/",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="entry-title"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//time[@class="entry-date published"]/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//span[@class="author vcard"]/a/text()'
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 大赦国际（国际特赦组织）
    "41": {
        "domain": "amnesty.org",  # 主域名
        "name": "大赦国际（国际特赦组织）",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://www.amnesty.org/en/search/?country=38526",
            "https://www.amnesty.org/en/latest/news/2018/08/nigeria-sars-overhaul-is-positive-step-but-reforms-must-be-robust/",
            "https://www.amnesty.org/en/latest/news/2018/08/malaysia-100-days-in-power-government-still-has-much-to-do-on-human-rights/",
            "https://www.amnesty.org/en/latest/news/2018/08/turkey-amnesty-turkeys-chair-released-after-more-than-a-year-behind-bars/",
            "https://www.amnesty.org/en/latest/research/",
            "https://www.amnesty.org/en/get-involved/join/",
            "https://www.amnesty.org/en/get-involved/take-action/",
            "https://www.amnesty.org/en/who-we-are/",
            "https://www.amnesty.org/en/what-we-do/",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="heading--main heading--in-padded"]/text()|\
                //h1[@class="heading--main heading--uppercase heading--in-padded"]/text()|\
                //div[@class="col__content"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@class="meta__section "]/div/time/text()|\
                    //div[@class="col__content"]/p/time/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="tags__item--bold"]/span/text()|\
                //span[@class="tags__icon--bold--documentsummary"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 丹麦司法部所成立的西藏调查委员会
    "42": {
        "domain": "tibetkommissionen.dk",  # 主域名
        "name": "丹麦司法部所成立的西藏调查委员会",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetkommissionen.dk/node/39",
            "http://tibetkommissionen.dk/node/38",
            "http://tibetkommissionen.dk/node/37",
            "http://tibetkommissionen.dk/node/35",
            "http://tibetkommissionen.dk/node/31",
            "http://tibetkommissionen.dk/node/32",
            "http://tibetkommissionen.dk/node/29",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="section"]/div/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 德国西藏倡议组织（TID）
    "43": {
        "domain": "tibet-initiative.de",  # 主域名
        "name": "德国西藏倡议组织（TID）",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://www.tibet-initiative.de/tsewang-norbu-founding-member-and-advisory-board-member-of-tibet-initiative-germany-passed-away/",
            "https://www.tibet-initiative.de/tsewang-norbu-gruendungsmitglied-und-beiratsmitglied-der-tibet-initiative-deutschland-ist-verstorben/",
            "https://www.tibet-initiative.de/gedenkfeier-fuer-liu-xiaobo-in-berlin/",
            "https://www.tibet-initiative.de/tsewang-norbu-founding-member-and-advisory-board-member-of-tibet-initiative-germany-passed-away/",
            "https://www.tibet-initiative.de/tashi-wangchuk-berufung-wurde-abgelehnt/",
            "https://www.tibet-initiative.de/work/natalia-woerner/",
            "https://www.tibet-initiative.de/work/ai-weiwei/",
            "https://www.tibet-initiative.de/work/tanja-kinkel/",
            "https://www.tibet-initiative.de/tsewang-norbu-gruendungsmitglied-und-beiratsmitglied-der-tibet-initiative-deutschland-ist-verstorben/",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="post-title"]/a/span/text()|\
                    //section[@id="box"]/div[1]/div[1]/div/div/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="content"]/div/p[2]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//p[@class="meta cat tranz "]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 德国西藏圣山之家
    "44": {
        "domain": "tibet-kailash-haus.de",  # 主域名
        "name": "德国西藏圣山之家",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=630",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=3",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=1",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=810",
            "https://achtsamkeitstraining-freiburg.de/events/mbsr-kurs-freiburg-september-oktober-2018-donnerstag/",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=30",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=20",
            "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=600",
            "https://www.tibet-kailash-haus.de/index.php?id=0",

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="seiteninhalt"]/h1/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": '//li[@class="selected"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 德国西藏之家
    "45": {
        "domain": "tibethaus.com",  # 主域名
        "name": "德国西藏之家",  # 网站名称
        # 测试起始地址
        "start_url": [
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=630",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=3",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=1",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=810",
            # "https://achtsamkeitstraining-freiburg.de/events/mbsr-kurs-freiburg-september-oktober-2018-donnerstag/",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=30",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=20",
            # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=600",
            # "https://www.tibet-kailash-haus.de/index.php?id=0",
            'https://www.tibethaus.com/kunst-kultur/ausstellungen/2012.html',
            'https://www.tibethaus.com/programm/studium-buddhismus/ab-januar-2019-ttm.html',
            'https://www.tibethaus.com/kunst-kultur/ausstellungen/2013.html'],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="calendar-event"]/h3/text()|\
                //div[@id="partialContentMain"]/div[1]/div/h1/text()|\
                //div[@id="partialContentMain"]/div[1]/h1/text()|\
                //div[@class="csc-header csc-header-n2"]/h2/text()|\
                //div[@class="csc-header csc-header-n1"]/h2/text()|\
                //div[@class="csc-header csc-header-n2"]/h1/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="calendar-event"]/p[1]/b/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//div[@id="calendar-event"]/p[2]/b/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//ol[@class="breadcrumb pull-right hidden-xs"]/li/span/text()|\
                    //ol[@class="breadcrumb pull-right hidden-xs"]/li[3]/span/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 世界西藏日  ##jia
    "46": {
        "domain": "worldtibetday.org",  # 主域名
        "name": "世界西藏日",  # 网站名称
        # 测试起始地址
        "start_url": [
            'http://worldtibetday.org/wtd_down.html',
            'http://worldtibetday.org/events.html',
            'http://worldtibetday.org/getinvolved.html',
            'http://worldtibetday.org/contact.html',
            'http://worldtibetday.org/support.html',
            'http://worldtibetday.org/message.html',
            'http://worldtibetday.org/index.html',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//p[@class="style5"]/text()|//p[@class="style6"]/text()',
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "",
            "rule": ""
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 捷克支持西藏（Czechs Support Tibet）
    "47": {
        "domain": "cesitibetpodporuji.cz",  # 主域名
        "name": "捷克支持西藏（Czechs Support Tibet)",  # 网站名称
        # 测试起始地址
        "start_url": [
            "https://cesitibetpodporuji.cz/blahoprejeme-svatosti-dalajlamovi-k-vyroci-83-narozenin-congratulations-h-h-dalai-lama-with-the-83rd-birthday-anniversary/",
            "https://cesitibetpodporuji.cz/hlas-pro-tibet/",
            "https://cesitibetpodporuji.cz/tibetsky-test-pristiho-prezidenta/",
            "https://cesitibetpodporuji.cz/ucitel-tibetskeho-buddhismu-maleho-tibetu-prijizdi-potreti-cr/",
            "https://cesitibetpodporuji.cz/tiskova-zprava-film-2017-festival-tibetskych-filmu-filmu-tibetu/",
            "https://cesitibetpodporuji.cz/tibet-cinsti-delnici-demontuji-budovy-jednom-nejvetsich-tibetskych-mestecek-larung-gar-ktere-slouzi-jako-vyznamna-buddhisticka-vzdelavaci-akademie/",
            "https://cesitibetpodporuji.cz/event/svatost-dalajlama-hradcanskem-namesti/",
            "https://cesitibetpodporuji.cz/event/tibet-solidarity-rally-zeneva/",
            "https://cesitibetpodporuji.cz/event/audience-u-dalailamy-dharamsale/",
            'https://cesitibetpodporuji.cz/tibetsky-test-pristiho-prezidenta/',
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//h1[@class="h2"]/text()|\
                //h1[@class="site__title"]/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//time[@class="event__date"]/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="menu__item menu__item--highlight"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 解救西藏组织（FreeTibet Campaign）
    "48": {
        "domain": "freetibetusa.weebly.com",  # 主域名
        "name": "解救西藏组织（FreeTibet Campaign）",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://freetibetusa.weebly.com/why-tibet.html",
            "http://freetibetusa.weebly.com/news",
            "http://freetibetusa.weebly.com/news/october-10th-2013",
            "http://freetibetusa.weebly.com/news/the-gyalwang-karmapa-offers-condolences-at-the-tragic-passing-away-of-dr-choje-akong-tulku-rinpoche-oct8th-2013-new-delhi",
            "http://freetibetusa.weebly.com/get-involved.html",
            "http://freetibetusa.weebly.com/donate.html",
            "http://freetibetusa.weebly.com/shop.html",
        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="wsite-content"]/div[1]/div[1]/h2/a/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//div[@id="wsite-content"]/div[1]/div[1]/p[1]/span/text()'
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//p[@class="blog-category-list"]/a/text()'
        },
        # 评论数
        "comment": {
            "type": "xpath",
            "rule": '//div[@id="wsite-content"]/div[1]/div[1]/p[2]/a/text()'
        },
    },
    # 瑞士里肯西藏中心
    "49": {
        "domain": "tibet-institut.ch",  # 主域名
        "name": "瑞士里肯西藏中心",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://www.tibet-institut.ch/content/tir/de/about_us_only.html",
            "http://www.tibet-institut.ch/content/tir/en/about_us_only.html",
            "http://www.tibet-institut.ch/content/tir/de/monastic_community.html",
            "http://www.tibet-institut.ch/content/tir/de/library.html",
            "http://www.tibet-institut.ch/content/tir/de/donation.html",
            "http://www.tibet-institut.ch/content/tir/de/documents.html",
            "http://www.tibet-institut.ch/content/tir/de/contacts.html",
            "http://www.tibet-institut.ch/content/tir/bod/about_us.html",
            'http://www.tibet-institut.ch/content/tir/de/library_usage.html',

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@class="content"]/h1/text()|\
                //form[@name="step1"]/h1[1]/text()'
        },
        # 发布时间
        "public_time": {
            "type": "",
            "rule": ""
        },
        # 作者
        "author": {
            "type": "",
            "rule": ""
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//li[@class="selected"]/a/text()|//a[@class="selected"]/text()'
        },
        # 评论数
        "comment": {
            "type": "",
            "rule": ""
        },
    },
    # 流亡藏人科学协会
    "50": {
        "domain": "tibetanscientificsociety.com",  # 主域名
        "name": "流亡藏人科学协会",  # 网站名称
        # 测试起始地址
        "start_url": [
            "http://tibetanscientificsociety.com/Portal/Home",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/38/?Title=Snapshots-from-Tibetan-Science-Conclave---IV-in-Bangalore",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/35/?Title=Tibetan-Students-and-Researchers-Converge-for-a-Science-Meet-(Press-Release)",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/30/?Title=TSS-Members-Participate-in-MIND-&-LIFE-XXX",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/32/?Title=Project-Grant-from-Tibetan-Scientific-Society---2016",
            "http://tibetanscientificsociety.com/Portal/EventDetail/24/?Title=Tibetan-Science-Conclave---II",
            "http://tibetanscientificsociety.com/Portal/EventDetail/22/?Title=Important-Updates-on-Tibetan-School-Science-Essay-Contest-",
            "http://tibetanscientificsociety.com/Portal/News",
            "http://tibetanscientificsociety.com/Portal/Events",
            "http://tibetanscientificsociety.com/Portal/VideoGallery",
            "http://tibetanscientificsociety.com/Portal/Videos/5/?Title=Engineering-and-Technology",
            "http://tibetanscientificsociety.com/Portal/Page/SupportUs",
            "http://tibetanscientificsociety.com/Portal/Page/Contact",
            "http://tibetanscientificsociety.com/Portal/Articles",
            "http://tibetanscientificsociety.com/Portal/ArticleDetail/37/?Title=Phantom-Limbs-A-Quirk-of-the-Brain!",
            "http://tibetanscientificsociety.com/Portal/ArticleDetail/23/?Title=The-Need-for-a-Quantum-Theory-of-Light-and-Matter",
            "http://tibetanscientificsociety.com/Member/Users",
            "http://tibetanscientificsociety.com/Member/User/ddolkar",
            "http://tibetanscientificsociety.com/Member/User/Dekyi",
            "http://tibetanscientificsociety.com/Portal/Page/AimsAndObjective",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/20/?Title=2nd-Tibetan-School-Science-Essay-Competition---2013",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/30/?Title=TSS-Members-Participate-in-MIND-&-LIFE-XXX",
            "http://tibetanscientificsociety.com/Portal/NewsDetail/28/?Title=TSC-Participants-Take-Part-in-Ethics-Conference",
            "http://tibetanscientificsociety.com/Portal/Video/18/?Title=Kunleng-VOA---19.04.2017-",
            "http://tibetanscientificsociety.com/Portal/Video/17/?Title=Airplane-History",  # 该视频无法播放 失效了

        ],
        # 标题
        "title": {
            "type": "xpath",
            "rule": '//div[@id="story_center"]/h1/text()|\
                //div[@id="katyContainer"]/div/h1/text()'
        },
        # 发布时间
        "public_time": {
            "type": "xpath",
            "rule": '//span[@id="SpnDate"]/text()[2]|\
            //div[@style="margin-left: 0;"]/span/text()'
        },
        # 作者
        "author": {
            "type": "xpath",
            "rule": '//span[@id="SpnDate"]/a/text()'
        },
        # 栏目
        "column": {
            "type": "xpath",
            "rule": '//div[@id="breadCrumb"]/a[2]/text()'
        },
        # 评论数
        "comment": {
            "type": "re",
            "rule": ""
        },
    },
}

"""
 allowed_domains__2 = ['tibet.net', 'xizang-zhiye.org',
                          'dalailama.com', 'tcewf.org',
                          'tibetoffice.ch', 'tibethouse.jp',
                          'tibet.org.tw', 'savetibet.ru',
                          'tibetoffice.org', 'tibetanlibrary.org',
                          'tibchild.org', 'sambhota.org',
                          'dalailamaworld.com', 'savetibet.org',
                          'tchrd.org', 'tibetanwomen.org',
                          'panditatranslation.org', 'tibet.ca',
                          'phayul.com', 'vot.org',
                          'worldbridges.com', 'kagyuoffice.org.tw',
                          'kunphen.center', 'amnesty.org',
                          'tibetkommissionen.dk', 'tibet-initiative.de',
                          'tibet-kailash-haus.de', 'tibethaus.com',
                          'cesitibetpodporuji.cz', 'freetibetusa.weebly.com',
                          'tibet-institut.ch'
                          ]

"""

if __name__ == "__main__":
    pass
