from unitls import ConfigureRule

web_list = [
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/", ],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", ],
    [3, "达赖喇嘛网站(英文、中文)", "http://www.dalailama.com/", ],
    [4, "西藏流亡政府教育部网站(英文)", "http://www.tcewf.org/", ],
    [5, "驻日内瓦办事处信息网(德文)", "http://www.tibetoffice.ch/", ],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/", ],
    [7, "驻伦敦代表处信息网(英文)", "http://www.tibet.com/", ],
    [8, "驻东京代表处信息网(日文)", "http://www.tibethouse.jp/", ],
    [9, "驻台北办事处信息网(中文)", "http://www.tibet.org.tw/", ],
    [10, "驻莫斯科代表处信息网(俄文)", "http://www.savetibet.ru/", ],
    [11, "欧盟联络处信息网(法文)", "http://users.skynet.be/reves/tibethome.html", ],
    [12, "中南美洲联络处信息网(西班牙文)", "http://tibetoffice.org/", ],
    [13, "驻堪培拉代表处信息网(英文)", "http://tibetoffice.com.au", ],
    [14, "藏医历算学院", "http://www.men-tsee-khang.org/", ],
    [15, "西藏视讯电视网", "http://www.tibetonline.tv/", ],
    [16, "罗布尔卡西藏文化中心", "https://www.norbulingka.org/", ],
    [17, "西藏表演艺术学院(TIPA)", "http://www.tibetanarts.org/", ],
    [18, "西藏文献图书馆", "http://tibetanlibrary.org/", ],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/", ],
    [20, "桑波扎西藏完全学校", "http://www.sambhota.org/", ],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", ],
    [22, "国际声援西藏中心", "http://www.savetibet.org/", ],
    [23, "西藏人权民主促进会", "http://www.tchrd.org/", ],
    [24, "西藏青年会", "http://tibetanyouthcongress.org/", ],
    [25, "西藏自由运动组织", "http://www.freetibet.org/", ],
    [26, "9•10•3组织", "http://www.guchusum.org/", ],
    [27, "西藏问题调解中心", "http://www.tccrinfo.org/", ],
    [28, "西藏妇女联合会", "http://www.tibetanwomen.org/", ],
    [29, "阿尼玛钦西藏文化研究所", "http://www.amnyemachen.org/", ],
    [30, "西藏青年会(台湾分会)", "http://rtyc-taiwan.blogspot.com/", ],
    [31, "妙宗班智达翻译小组会", "http://www.panditatranslation.org/", ],
    [32, "加拿大西藏同乡会", "http://www.tibet.ca/", ],
    [33, "西藏全球新闻(英文)", "http://www.tibetlink.com/", ],
    [34, "家乡(英)", "http://www.phayul.com/", ],
    [35, "西藏之声", "http://www.vot.org/", ],
    [36, "西藏讯息港(英)", "http://worldbridges.com/Tibet/", ],
    [37, "西藏在线", "http://www.tibet.org/", ],
    [38, "达兰萨拉信息网", "http://dharamsalanet.com/", ],
    [39, "大宝法王噶玛巴中文网站", "https://www.kagyuoffice.org.tw/", ],
    [40, "达兰萨拉利众中心", "http://kunphen.center/", ],
    [41, "大赦国际（国际特赦组织）", "https://www.amnesty.org", ],
    [42, "丹麦司法部所成立的西藏调查委员会", "http://tibetkommissionen.dk", ],
    [43, "德国西藏倡议组织（TID）", "https://www.tibet-initiative.de/", ],
    [44, "德国西藏圣山之家", "https://www.tibet-kailash-haus.de/", ],
    [45, "德国西藏之家", "https://www.tibethaus.com/home.html", ],
    [46, "德国援助藏人组织", "http://agerstner.homepage.tonline.de/tibet/english/tibetaid.htm", ],
    [47, "捷克支持西藏（Czechs Support Tibet）", "https://cesitibetpodporuji.cz/", ],
    [48, "解救西藏组织（FreeTibet Campaign）", "http://freetibetusa.weebly.com/", ],
    [49, "瑞士里肯西藏中心", "http://www.tibet-institut.ch/", ],
    [50, "流亡藏人科学协会", "http://tibetanscientificsociety.com/Portal/Home", ],

]

all_urls = [
    ["网站序号", "网站名称", "", "地址、链接"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/08/his-holiness-the-dalai-lama-reiterates-importance-of-middle-way-approach/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2009/02/the-kashag-urges-china-to-withdraw-the-undeclared-martial-law-in-tibet/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/08/psc-announces-7-vacancies-at-office-of-auditor-general-cta/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/06/fifth-six-month-course-on-tibetan-language-and-buddhist-studies/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/08/malaysia-cancels-beijing-backed-pipelines-east-coast-rail-link/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/06/china-rout-has-1023-stocks-plunging-10-in-one-day/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2018/04/photo-news-nechung-kuten-rinpoche-visits-oot-washington/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2009/01/photo-news-tenshug-for-his-holiness-the-dalai-lama-in-sarnath/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2017/04/update-on-the-latest-self-immolation-protest-in-tibet/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2015/07/tibetan-monk-burns-self-in-kyegudo-self-immolation-reaches-141/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/international-resolutions/us-senate-honours-his-holiness-the-dalai-lama-in-unanimous-resolution/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/international-resolutions/italian-senate-committee-passes-resolution-on-tibet/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/important-issues/factsheet-immolation-2011-2012/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2013/04/assessment-report-of-the-recent-landslide-event-in-the-gyama-valley/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2011/12/tibets-resource-curse/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2011/08/glacier-thawing-speeds-up-in-yangtze-river-sources/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2016/10/usaid-awards-a-grant-of-usd-23-million-to-strengthen-self-reliance-and-resilience-of-tibetan-communities-in-south-asia/"],
    [1, "藏人行政中央（藏、英）", "http://www.tibet.net/",
     "http://tibet.net/2016/10/his-holiness-the-dalai-lama-will-be-arriving-in-riga-today/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/达赖喇嘛尊者致函哀悼联合国前秘书长科菲·安南/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/2011-01-31-08-25-01/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/尊者达赖喇嘛83岁寿诞庆典感悟/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/2010-09-15-05-58-18/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/西藏境内再发第151起自焚抗议事件/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/西藏獨立宣言日；藏地發生自焚抗議/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/西藏通訊二零一四年三月至-六月號/"],
    [2, "西藏之页(中文)", "http://www.xizang-zhiye.org/", "http://xizang-zhiye.org/雪域境外流亡記/"],
    [3, "达赖喇嘛网站(英文、中文)", "http://www.dalailama.com/",
     "https://www.dalailama.com/news/2018/vidyaloke-talk-for-all-citizens-indian-wisdom-and-the-modern-world"],
    [4, "", "", ""],
    [5, "驻日内瓦办事处信息网(德文)", "http://www.tibetoffice.ch/",
     "http://www.tibetoffice.ch/2018/08/14/i-look-forward-to-a-good-rest-now-his-holiness-the-dalai-lama-returns-from-45-day-teaching-tour/"],
    [5, "驻日内瓦办事处信息网(德文)", "http://www.tibetoffice.ch/",
     "http://www.tibetoffice.ch/2018/08/20/condolences-on-the-passing-away-of-kofi-annan/"],
    [5, "驻日内瓦办事处信息网(德文)", "http://www.tibetoffice.ch/",
     "http://www.tibetoffice.ch/2018/08/20/cta-president-condoles-demise-of-former-un-secretary-general-kofi-annan/"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/", "http://tibetoffice.org/media-press/2016-tibetan-election"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibet.net/2018/07/kashags-statement-on-the-83rd-birthday-of-his-holiness-the-great-fourteenth-dalai-lama-of-tibet/"],
    [6, "驻纽约代表处信息网(英文)", "http://www.tibetoffice.org/en/",
     "http://tibet.net/2017/03/statement-of-sikyong-on-the-58th-anniversary-of-tibetan-national-uprising-day/"],
    [7, "", "", ""],
    [8, "http://www.tibethouse.jp/", "驻东京代表处信息网 (日文)",
     "http://www.tibethouse.jp/news_release/2018/180820_HHDL_20180811.html"],
    [8, "http://www.tibethouse.jp/", "驻东京代表处信息网 (日文)",
     "http://www.tibethouse.jp/news_release/2010/101025_protest.html"],
    [9, "驻台北办事处信息网 (中文)", "http://www.tibet.org.tw/", "http://www.tibet.org.tw/news_detail.php?news_id=9690"],
    [9, "驻台北办事处信息网 (中文)", "http://www.tibet.org.tw/", "http://www.tibet.org.tw/news_detail.php?news_id=9675"],
    [10, "驻莫斯科代表处信息网(俄文)", "http://www.savetibet.ru/", "http://savetibet.ru/2018/08/21/drepung-gomang.html"],
    [10, "驻莫斯科代表处信息网(俄文)", "http://www.savetibet.ru/", "http://savetibet.ru/2018/08/18/dalai-lama-14.html"],
    [11, "欧盟联络处信息网(法文)", "http://users.skynet.be/reves/tibethome.html", "http://users.skynet.be/reves/bluebook.htm"],
    [11, "欧盟联络处信息网(法文)", "http://users.skynet.be/reves/tibethome.html",
     "http://users.skynet.be/reves/bureaudutibet.html"],
    [12, "", "", ""],
    [13, "驻堪培拉代表处信息网(英文)", "http://tibetoffice.com.au",
     "http://tibetoffice.com.au/china-and-russia-strengthening-relationship-in-bid-to-thwart-us-dominance/"],
    [13, "驻堪培拉代表处信息网(英文)", "http://tibetoffice.com.au",
     "http://tibetoffice.com.au/his-holiness-the-dalai-lama-returning-june-2008/"],
    [14, "藏医历算学院", "http://www.men-tsee-khang.org/",
     "http://www.men-tsee-khang.org/new-news/2018/csrsr/chauntra-celebration.html"],
    [14, "藏医历算学院", "http://www.men-tsee-khang.org/",
     "http://www.men-tsee-khang.org/new-news/2018/Dr.Tamdin%20la/drtamdin.html"],
    [15, "", "", ""],
    [16, "", "", ""],
    [17, "", "", ""],
    [18, "西藏文献图书馆", "http://tibetanlibrary.org/",
     "http://tibetanlibrary.org/20th-august-2018-thai-monks-completed-their-course-at-ltwa/"],
    [18, "西藏文献图书馆", "http://tibetanlibrary.org/", "http://tibetanlibrary.org/ltwa-book-launch/"],
    [18, "西藏文献图书馆", "http://tibetanlibrary.org/", "http://tibetanlibrary.org/glimpses-of-the-book-launch/"],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/",
     "http://www.tibchild.org/annas-plan-to-get-an-low-interest-loan-for-people-with-no-credit/"],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/",
     "http://www.tibchild.org/ways-to-build-up-a-good-credit-rating/#comment-4"],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/", "http://www.tibchild.org/2018/01/"],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/", "http://www.tibchild.org/category/borrower/"],
    [19, "达兰萨拉西藏儿童村(TCV)", "http://www.tibchild.org/", "http://www.tibchild.org/category/usa/"],
    [20, "", "", ""],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1034"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1007"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1022"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=388"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=996"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=972"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1021"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1038"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1032"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=1000"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=970"],
    [21, "达赖喇嘛官方华文网站", "http://www.dalailamaworld.com/", "http://www.dalailamaworld.com/topic.php?t=645"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/denials-smokescreens-and-misleading-information-chinese-government-attempts-to-distort-its-record-on-tibet-at-un-committee-hearing-on-august-13-2018/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/un-committee-should-pressure-china-to-end-discrimination-against-tibetans-international-campaign-for-tibet-says-in-new-report/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/international-campaign-for-tibets-oral-statement-at-the-un-cerd-96th-session-in-geneva-on-august-7-2018/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/", "https://www.savetibet.org/rowell-fund-2019/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/new-fears-for-historic-structure-of-jokhang-temple-after-major-fire-as-china-covers-up-extent-of-damage/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/inside-tibet-dramatic-video-of-slow-moving-landslide-in-tibet-raises-questions-about-climate-change/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/a-short-note-on-recent-tibetan-chinese-relations/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/on-account-of-facebooks-deletion-of-information-more-than-20000-people-signed-a-petition/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/",
     "https://www.savetibet.org/senior-american-officials-call-for-international-coalition-to-press-china-on-religious-freedom-in-tibet/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/", "https://www.savetibet.org/his-holiness-visits-washington-d-c/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/", "https://www.savetibet.org/newsroom/tibet-weekly-updates/"],
    [22, "国际声援西藏中心", "http://www.savetibet.org/", "https://www.savetibet.org/newsroom/chinese-language-news/"],
    [23, "西藏人权民主促进会", "http://www.tchrd.org/",
     "http://tchrd.org/two-tibetans-convicted-for-inciting-separatism-released-after-serving-long-prison-terms/"],
    [23, "西藏人权民主促进会", "http://www.tchrd.org/", "http://tchrd.org/annual-report-2015/"],
    [23, "西藏人权民主促进会", "http://www.tchrd.org/",
     "http://tchrd.org/tchrd-releases-2013-annual-report-and-special-report-on-re-education-through-labor/"],
    [24, "", "", ""],
    [25, "西藏自由运动组织", "http://www.freetibet.org/", "https://www.freetibet.org/news-media/na/blog-london-tibetfest-2017"],
    [25, "西藏自由运动组织", "http://www.freetibet.org/",
     "https://www.freetibet.org/news-media/na/musician-released-prison-after-three-and-half-years"],
    [26, "", "", ""],
    [27, "", "", ""],
    [28, "", "", ""],
    [29, "", "", ""],
    [30, "", "", ""],
    [31, "", "", ""],
    [32, "加拿大西藏同乡会", "http://www.tibet.ca/", "http://www.tibet.ca/en/library/media_releases/445"],
    [32, "加拿大西藏同乡会", "http://www.tibet.ca/", "http://www.tibet.ca/en/library/wtn/14006"],
    [33, "", "", ""],
    [34, "家乡(英)", "http://www.phayul.com/",
     "http://www.phayul.com/news/article.aspx?id=40717&article=Tibetan+activist%27s+appeal+against+5-year+sentence+rejected&t=1&c=1"],
    [34, "家乡(英)", "http://www.phayul.com/", "http://www.phayul.com/news/article.aspx?id=40682"],
    [35, "西藏之声", "http://www.vot.org/", "https://www.vot.org/བོད་ནང་གི་བོད་མིའི་འཚོ/"],
    [35, "西藏之声", "http://www.vot.org/", "https://www.vot.org/ཨ་རི་དང་བཞུགས་སྒར་དུ་༸/"],
    [35, "西藏之声", "http://www.vot.org/", "https://www.vot.org/ལྷ་ས་གྲོང་ཁྱེར་ནང་སློབ1/"],
    [36, "", "", ""],
    [37, "", "", ""],
    [38, "", "", ""],
    [39, "大宝法王噶玛巴中文网站", "https://www.kagyuoffice.org.tw/",
     "https://www.kagyuoffice.org.tw/17th-karmapa/documents/20180815"],
    [39, "大宝法王噶玛巴中文网站", "https://www.kagyuoffice.org.tw/", "https://www.kagyuoffice.org.tw/news/20180711"],
    [40, "达兰萨拉利众中心", "http://kunphen.center/",
     "http://kunphen.center/events-organised-by-the-center/fund-raise-event-at-bodh-gaya-and-dharamsala/"],
    [40, "达兰萨拉利众中心",
     "http://kunphen.center/whats-happening-at-kunphen-center/plantation-by-boys-at-the-new-rahab-site/"],
    [41, "", "", ""],
    [22, "", "", ""],
    [22, "", "", ""],

]
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ArticleSpider.models import WebList, StartUrl, WebDetail
from ArticleSpider.settings import db_user, db_pawd, db_host, db_port, db_name

# 创建对象的基类:
Base = declarative_base()


class insert(object):
    def __init__(self):  # '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

    def insert_web_list(self):
        for web in web_list:
            info = WebList(
                webid=web[0],
                name=web[1],
                domain=web[2],
            )
            try:
                self.session.add(info)
                self.session.commit()
            except Exception as e:
                print("[UUU] 网站数据插入数据异常 Error :{}".format(e))
                self.session.rollback()

    def insert_start_url(self):
        for webId, info in ConfigureRule.XpathRule.items():
            webid = webId
            url_list = info['start_url']
            name = info['name']
            userid = 1
            status = 0
            for url in url_list:
                info = StartUrl(
                    webid=webid,
                    url=url,
                    name=name,
                    date=datetime.datetime.now(),
                    userid=userid,
                    type='非限制性',
                    status=status,
                )
                try:
                    self.session.add(info)
                    self.session.commit()
                except Exception as e:
                    print("[UUU] 起始url数据插入数据异常 Error :{}".format(e))
                    self.session.rollback()


if __name__ == '__main__':
    insert = insert()
    # insert.insert_start_url()
    # insert.insert_web_list()
