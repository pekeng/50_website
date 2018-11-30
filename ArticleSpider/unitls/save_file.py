# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:国明信息
FileName = PyCharm
Version:1.0
CreateDay:2018/8/24 19:23
"""
import os
import re
from urllib.parse import unquote
import requests
from lxml import etree
from pytube import YouTube
from pathlib import Path

BASE_DIR = '/opt/crawler/'
# BASE_DIR = '/'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
}


# 创建文件夹
def mk_dir(url_to_path):
    """
    file_path:最后文件存储的路径
    file_name:处理之后的文件名 以及静态文件存储的文件夹名字
    """
    # 初步处理掉空格
    url_to_path = url_to_path  # .replace(' ', '')
    # 有个特殊网站 通过新闻ID判断
    if 'news_id' in url_to_path:
        url_to_path = url_to_path.replace('.php?', '/').replace('=', '/')
    if "?aid1=" in url_to_path:
        url_to_path = url_to_path.replace('?aid1=', '')
    if 'www.vot.org' in url_to_path and '?type=' in url_to_path:
        url_to_path = url_to_path.replace('?type=', 'type/')
    if 'www.phayul.com' in url_to_path:
        article_id = "".join(re.findall(re.compile(r'id=([0-9]{2,10})&'), url_to_path))
        url_to_path = url_to_path.split('.aspx')[0]
        url_to_path = url_to_path + '/' + article_id
    if 'www.amnesty.org' in url_to_path:
        url_to_path = url_to_path.replace('?country=', 'country/')
    if 'tibet-kailash-haus.de' in url_to_path:
        url_to_path = url_to_path.replace('index.php?', '/index/').replace('&item=', '/item/').replace('=', '/')
    if 'www.tibethaus.com' in url_to_path:
        url_to_path = url_to_path.replace('.php?', '/').replace('=', '/').replace('&', '/')
    if 'tibetonline.tv' in url_to_path:
        url_to_path = url_to_path.replace('/?', '/').replace('=', '/')
    if 'dalailamaworld.com' in url_to_path:
        url_to_path = url_to_path.replace('.php?t=', '/').split('&')[0]
    if 'www.youtube.com' in url_to_path:
        url_to_path = url_to_path.replace('?v=', '/')

    # 去掉前面HTTP 去掉最后的?参数
    page_path = url_to_path.split('://')[-1].split('?')[0]
    if page_path.endswith('/'):  # 去掉结尾的/
        page_path = page_path[:-1]

    # 去掉最后的.html等   需要分网站 有的
    domain2 = ""
    if '.htm' in page_path:
        page_path = page_path.split('.htm')[0]
        domain2 = page_path
    #
    file_path = "/".join(page_path.split('/')[:-1])  # 文件夹基本路径--去掉文件名
    file_name0 = page_path.split('/')[-1]  # 文件名
    # 处理某些被编码过的网站地址
    file_name2 = unquote(file_name0)

    # 处理特殊字符串 文件夹不能有以下字符串 \ / : * ? < > " !
    for st in '\/:*?<>"!':
        file_name2 = file_name2.replace(st, '')
    # print("处理特殊字符串之后的file_name：{}".format(file_name2))

    # 控制文件夹长度 不超过
    if len(file_name2) > 30:
        file_name2 = file_name2[:30]
    page_path = "/".join(page_path.split('/')[:-1]) + '/' + file_name2

    # print("处理文件夹长度之后的file_name：{}  page_path：{}".format(file_name2, page_path))
    # print('\n\n')
    # print("PATH:{}".format(path))
    folder = os.path.exists(BASE_DIR + page_path)
    # print(folder)
    if not folder:
        os.makedirs(BASE_DIR + page_path)

    domain = page_path.split('/')[0]
    return BASE_DIR + file_path, file_name2, domain, domain2


# 网络请求
def get_content(url):
    try:
        response = requests.get(url, headers=headers, timeout=20)
        return response
    except Exception as e:
        print("请求错误：{} URL地址:{}".format(e, url))
        return ""


# 处理IMG标签
def parse_img(webId, file_name, file_path, domain, domain2, html):
    tree = etree.HTML(html)
    all_img = tree.xpath('//img/@src|link/@href')
    # print(all_img)
    for image in all_img:
        # print(img)
        img = str(image).replace(' ', '')
        print("初始img:{}".format(img))
        # if img:  # 过滤掉空字符串
        if img.startswith('//'):
            img_url = 'http:' + img
        elif img.startswith('/'):
            if str(domain) in img:
                img_url = 'http:/' + img
            else:
                img_url = 'http://' + domain + img
        elif img.startswith('http'):
            img_url = img
        else:
            if img:
                if "tibet.ca" in str(file_path):
                    img_url = 'http://' + domain + '/' + img
                elif "tibet-kailash-haus.de" in str(file_path):
                    img_url = 'http://' + domain + '/' + img
                elif "dalailamaworld.com" in str(file_path):
                    img_url = 'http://' + domain + '/' + img
                elif "www.tibethaus.com" in str(file_path):
                    img_url = 'http://' + domain + '/' + img
                else:
                    u = "/".join(domain2.split('/')[:-1])
                    img_url = 'http://' + u + '/' + img
            else:
                img_url = ""
        print(img_url)
        if img_url:
            image_name = img.split('?')[0].split('/')[-1]  # 去掉? 然后使用/分割 取最后文件名
            # 图片地址 file_path + 文件名
            image_path = file_path + '/' + image_name.replace(' ', '')
            print("图片原来地址:{}   图片保存地址:{}".format(img, image_path))
            html = html.replace(img, './' + file_name + '/' + image_name.replace(' ', ''))
            # 图片 保存
            try:
                with open(image_path, 'wb+') as img_file:
                    res = get_content(img_url)
                    img_file.write(res.content)
            except Exception as e:
                print("DOWN LOAD IMAGE ERROR :{} URL:{}".format(e, url))
    # print("最后的HTML页面：{}".format(html))
    return html


# 处理PDF 文件 所有a标签 .pdf结尾
def parse_pdf(webId, file_name, file_path, domain, domain2, html):
    tree = etree.HTML(html)
    all_pdf = tree.xpath('//a/@href')
    for pdfs in all_pdf:
        pdfs = str(pdfs)
        # print("A标签的地址：{}".format(pdfs))
        pdf_all = str(pdfs).replace(' ', '').split('http')  # 过滤掉空字符串
        if len(pdf_all) == 2 and '.pdf' in str(pdfs):
            print("初始PDF:{}".format(pdfs))
            if pdfs.startswith('//'):
                pdf_url = 'http:' + pdfs
            elif pdfs.startswith('/'):
                if str(domain) in pdfs:
                    pdf_url = 'http:/' + pdfs
                else:
                    pdf_url = 'http://' + domain + pdfs
            elif pdfs.startswith('http'):
                pdf_url = pdfs
            else:
                pdf_url = 'http://' + domain2 + '/' + pdfs
            print("pdf_url:{}".format(pdf_url))
            if pdf_url:
                pdf_name = pdf_url.split('?')[0].split('/')[-1]  # 去掉? 然后使用/分割 取最后文件名
                # PDF文件地址 file_path + 文件名
                pdf_path = file_path + '/' + pdf_name
                # print("PDF原来地址:{}   PDF保存地址:{}".format(pdf_url, pdf_path))
                html = html.replace(pdfs, './' + file_name + '/' + pdf_name)
                # PDF 保存
                try:
                    with open(pdf_path, 'wb+') as pdf_file:
                        res = get_content(pdf_url)
                        pdf_file.write(res.content)
                except Exception as e:
                    print("DOWN LOAD PDF ERROR :{} URL:{}".format(e, pdf_url))
    # print("最后的HTML页面：{}".format(html))
    return html


# 处理CSS样式文件
def parse_css(webId, file_name, file_path, domain, domain2, html):
    """
     :param file_path: 文件全路径
    :param file_name: 文件名称
    :param html: 需要处理的源码
    :return:
    """
    tree = etree.HTML(html)
    all_css = tree.xpath('//link/@href')
    for css in all_css:
        css_full_url = str(css)  # .replace(' ', '')
        if css_full_url.startswith('//'):
            css_url = 'http:' + css_full_url
        elif css_full_url.startswith('http'):
            css_url = css_full_url
        elif css_full_url.startswith('/'):
            if str(domain) in css_full_url:
                css_url = 'http:/' + css_full_url
            else:
                css_url = 'http://' + domain + css_full_url
        else:
            if "tibet.ca" in str(file_path):
                css_url = 'http://' + domain + '/' + css_full_url
            elif "tibet-kailash-haus.de" in str(file_path):
                css_url = 'http://' + domain + '/' + css_full_url
            elif "tibethaus.com" in str(file_path):
                css_url = 'http://' + domain + '/' + css_full_url
            elif 'dalailamaworld.com' in str(file_path):
                css_url = 'http://' + domain + '/' + css_full_url
            else:
                css_url = 'http://' + domain2 + '/' + css_full_url
        if '.css' in css_url:
            # CSS 样式文件名
            css_name = css_full_url.split('?')[0].split('/')[-1].replace('.gzip', '')
            # CSS地址 file_path + 文件名
            css_path = file_path + '/' + css_name
            print("CSS原来地址:{}  CSS保存地址:{}".format(css_url, css_path))
            html = html.replace(str(css), './' + file_name + '/' + css_name)
            # CSS 保存
            try:
                print("CSS_URL:{}".format(css_url))
                with open(css_path, 'w+', encoding='utf-8', errors='ignore') as css_file:
                    res = get_content(css_url)
                    res.encoding = 'utf-8'
                    css_file.write(res.text)
            except Exception as e:
                print("ERROR:{} URL:{}".format(e, css_url))

    # print("最后的HTML页面：{}".format(html))
    return html


# 处理CSS样式文件
def parse_js(webId, file_name, file_path, domain, domain2, html):
    """
     :param file_path: 文件全路径
    :param file_name: 文件名称
    :param html: 需要处理的源码
    :return:
    """
    tree = etree.HTML(html)
    all_js = tree.xpath('//script/@src')
    for js in all_js:
        js_full_url = str(js).replace(' ', '')
        if js_full_url.startswith('//'):
            js_url = 'http:' + js_full_url
        elif js_full_url.startswith('http'):
            js_url = js_full_url
        elif js_full_url.startswith('/'):
            if str(domain) in js_full_url:
                js_url = 'http:/' + js_full_url
            else:
                js_url = 'http://' + domain + js_full_url
        else:
            if "tibet.ca" in str(file_path):
                js_url = 'http://' + domain + '/' + js_full_url
            elif 'dalailamaworld.com' in str(file_path):
                js_url = 'http://' + domain + '/' + js_full_url
            else:
                js_url = 'http://' + domain2 + '/' + js_full_url
        if '.js' in js_url:
            # js 样式文件名
            js_name = js_full_url.split('?')[0].split('/')[-1].replace('.gzip', '')
            # js地址 file_path + 文件名
            js_path = file_path + '/' + js_name
            print("js原来地址:{}  js保存地址:{}".format(js_url, js_path))
            html = html.replace(js_full_url, './' + file_name + '/' + js_name)
            # CSS 保存
            try:
                print("JS_URL:{}".format(js_url))
                with open(js_path, 'w+', encoding='utf-8', errors='ignore') as js_file:
                    res = get_content(js_url)
                    res.encoding = 'utf-8'
                    js_file.write(res.text)
            except Exception as e:
                print("ERROR:{} URL:{}".format(e, js_url))
    # print("最后的HTML页面：{}".format(html))
    return html


# 处理音频文件 audio
def parse_audio(webId, file_name, file_path, domain, domain2, html):
    tree = etree.HTML(html)
    all_audio = tree.xpath('//audio/a/@href|//div[@class="entry-content"]/p/a/@href')
    for audio in all_audio:
        print("音频URL：{}".format(audio))
        audio_full_url = str(audio).replace(' ', '')
        if audio_full_url.startswith('//'):
            audio_url = 'http:' + audio_full_url
        elif audio_full_url.startswith('http'):
            audio_url = audio_full_url
        elif audio_full_url.startswith('/'):
            if str(domain) in audio_full_url:
                audio_url = 'http:/' + audio_full_url
            else:
                audio_url = 'http://' + domain + audio_full_url
        else:
            if "tibet.ca" in str(file_path):
                audio_url = 'http://' + domain + '/' + audio_full_url
            else:
                audio_url = 'http://' + domain2 + '/' + audio_full_url
        if '.mp3' in audio_url:
            # audio mp3文件名
            audio_name = audio_full_url.split('?')[0].split('/')[-1]
            # js地址 file_path + 文件名
            audio_path = file_path + '/' + audio_name
            print("audio原来地址:{}  audio保存地址:{}".format(audio_url, audio_path))
            html = html.replace(audio_full_url, './' + file_name + '/' + audio_name)
            # CSS 保存
            try:
                print("audio_URL:{}".format(audio_url))
                with open(audio_path, 'wb+', ) as audio_file:
                    res = get_content(audio_url)
                    audio_file.write(res.content)
            except Exception as e:
                print("ERROR:{} URL:{}".format(e, audio_url))
    # print("最后的HTML页面：{}".format(html))
    return html


# 下载函数 下载YouTube视频
def download_youtube_video(youtube_url, local_dir):
    print("YOUTUBE下载地址：{}".format(youtube_url))
    try:
        yt = YouTube(youtube_url)
    except Exception as e:
        print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
        return 0

    pattern = r'[\/.:*?"<>|]+'
    regex = re.compile(pattern)
    filename = regex.sub('', yt.title).replace('\'', '').replace('\\', '') + ".mp4"
    print("FILE NAME:{}".format(filename))
    try:
        p = Path(local_dir)
        fp = p / filename
        if fp.exists():  # 判断文件是否存在
            print("[SKIP       ] {0}".format(filename))
            return 0
        print("[DOWNLOAD   ] {0}".format(filename))
        yt.streams.filter(subtype='mp4', progressive=True) \
            .order_by('resolution').desc().first().download(local_dir)

        print("[DONE       ] {0}".format(filename))
    except Exception as e:
        print("[ERROR      ] {0}".format(str(e)).encode("utf-8"))
        return 0
    return filename


# 处理YouTube视频信息
def parse_video(webId, file_name, file_path, domain, domain2, html, url):
    # 西藏之声
    if 'www.vot.org' in str(file_path) or 'tibetanscientificsociety.com' in str(file_path) \
            or 'dalailamaworld.com' in str(file_path) or 'savetibet.ru' in str(file_path):
        # print("解析视频：{}".format(html))
        video_list = []
        all_video1 = re.findall(re.compile(r'(https://www\.youtube\.com/embed/.*?)"'), html)
        all_video2 = re.findall(re.compile(r'(http://www\.youtube\.com/embed/.*?)"'), html)
        all_video = all_video1 + all_video2
        for video in all_video:
            if video not in video_list:
                video_list.append(video)
        for video in video_list:
            video_id = video.split('embed/')[1].split('?')[0]
            video_url = "https://www.youtube.com/watch?v=" + video_id
            print("视频地址：{}".format(video_url))
            local_dir = file_path  # + '/' + file_name
            print("将要存储位置：{}".format(local_dir))
            # 视频文件名
            video_filename = download_youtube_video(video_url, local_dir)
            if video_filename != 0:
                print("视频文件的名字：{}".format(video_filename))
                print("存储文件的位置：{}".format(str(local_dir) + '/' + str(video_filename)))
                html = html.replace(video, './' + str(file_name) + '/' + video_filename)
    # 西藏人权民主促进会
    elif 'tchrd.org' in str(file_path):
        print("处理西藏人权民主促进会 视频数据")
        tree = etree.HTML(html)
        all_video = tree.xpath('//video/a/@href')
        for video in all_video:
            print("视频地址：{}".format(video))
            video_name = video.split('?')[0].split('/')[-1]
            video_url = str(video)
            video_path = file_path + '/' + video_name
            with open(video_path, 'wb+') as video_fi:
                response = get_content(video_url)
                video_fi.write(response.content)
            html = html.replace(video_url, './' + file_name + '/' + video_name)
    elif 'tibetanscientificsociety.com' in str(file_path):
        video_list = []
        all_video = re.findall(re.compile(r'(https://www\.youtube\.com/watch\?v=.*?)"'), html)
        for video in all_video:
            if video not in video_list:
                video_list.append(video)
        for video in video_list:
            video_id = video.split('v=')[1].split('?')[0]
            video_url = "https://www.youtube.com/watch?v=" + video_id
            print("视频地址：{}".format(video_url))
            local_dir = file_path  # + '/' + file_name
            print("将要存储位置：{}".format(local_dir))
            # 视频文件名
            video_filename = download_youtube_video(video_url, local_dir)
            if video_filename != 0:
                print("存储文件的位置：{}".format(str(local_dir) + '/' + str(video_filename)))
                html = html.replace(video, './' + str(file_name) + '/' + str(video_filename))
    elif 'tibetonline.tv' in str(file_path):
        video_list = []
        tree = etree.HTML(html)
        all_video = tree.xpath('//a[@class="magpopif"]/@href')
        for video in all_video:
            if video not in video_list:
                video_list.append(video)
        for video in video_list:
            # video_id = video.split('v=')[1].split('?')[0]
            # video_url = "https://www.youtube.com/watch?v=" + video_id
            video_url = str(video)
            print("视频地址：{}".format(video_url))
            local_dir = file_path  # + '/' + file_name
            print("将要存储位置：{}".format(local_dir))
            # 视频文件名
            video_filename = download_youtube_video(video_url, local_dir)
            if video_filename != 0:
                print("存储文件的位置：{}".format(str(local_dir) + '/' + str(video_filename)))
                html = html.replace(video, './' + str(file_name) + '/' + str(video_filename))
        video_list2 = []
        all_video = re.findall(re.compile(r'(https://www\.youtube\.com/embed/.*?)"'), html)
        for video in all_video:
            if video not in video_list:
                video_list2.append(video)
        for video in video_list2:
            video_id = video.split('embed/')[1].split('?')[0]
            video_url = "https://www.youtube.com/watch?v=" + video_id
            print("视频地址：{}".format(video_url))
            local_dir = file_path  # + '/' + file_name
            print("将要存储位置：{}".format(local_dir))
            # 视频文件名
            video_filename = download_youtube_video(video_url, local_dir)
            if video_filename != 0:
                print("存储文件的位置：{}".format(str(local_dir) + '/' + str(video_filename)))
                html = html.replace(video, './' + str(file_name) + '/' + str(video_filename))
    elif 'www.youtube.com' in str(file_path):
        video_url = url
        print("视频地址：{}".format(video_url))
        local_dir = file_path  # + '/' + file_name
        print("将要存储位置：{}".format(local_dir))
        # 视频文件名
        video_filename = download_youtube_video(video_url, local_dir)
        if video_filename != 0:
            print("存储文件的位置：{}".format(str(local_dir) + '/' + str(video_filename)))
            # html = html.replace(video_url, './' + str(file_name) + '/' + str(video_filename))

            print("视频地址：{}".format(url))
            video_name = url.split('?')[0].split('/')[-1]
            video_url = str(url)
            video_path = file_path + '/' + video_name
            with open(video_path, 'wb+') as video_fi:
                response = get_content(video_url)
                video_fi.write(response.content)
            # html = html.replace(video_url, './' + file_name + '/' + video_name)
            html = './' + str(file_name) + '/' + str(video_filename)
    # print("处理视频地址返回：{}".format(html))
    return html


# 保存HTML页面
def save_html(webId, file_path, file_name, domain, domain2, url, response):
    """

    :param file_path: 文件全路径
    :param file_name: 文件名称
    :param url: 请求地址
    静态文件路径:file_path + file_name 下
    :return:
    """

    if 'savetibet.ru' in url:
        response = requests.get(url, headers=headers)
        response.encoding = 'windows-1251'
        html = response.text
    else:
        # response.encoding = 'utf-8'
        html = response.text
    # print(response.text)
    print("FILE_PATH:{}".format(file_path))
    static_file_path = "{}/{}".format(file_path, file_name)
    # HTML页面源码处理 www.tibet.ca 网站有个base
    html = html.replace("<base href='http://www.tibet.ca/' />", "")
    html = html.replace('<base href="https://www.kagyuoffice.org.tw/karmapa-office/announcement/20130801" />', "")

    base = "".join(re.findall(re.compile(r'<base href=.*?/>'), html))
    html = html.replace(base, '')
    html = html.replace('<base href="/">', '')
    #
    # 网站的css文件 地址不正常
    if 'tibetkommissionen.dk' in url:
        html = html.replace('<style>@import url(', '<link type="text/css" rel="stylesheet" href=') \
            .replace('css");</style>', 'css"/>')
        html = html.replace('@import url(', '<link type="text/css" rel="stylesheet" href=').replace('p92wt7");', '"/>')
    if 'www.tibethaus.com' in url:
        html = html.replace('css?family=', 'css/family/')

    # # print("原来页面代码：{}".format(html))
    html = parse_img(webId, file_name, static_file_path, domain, domain2, html)  # 处理图片地址
    html = parse_css(webId, file_name, static_file_path, domain, domain2, html)  # 处理CSS地址
    html = parse_js(webId, file_name, static_file_path, domain, domain2, html)  # 处理JS地址
    html = parse_pdf(webId, file_name, static_file_path, domain, domain2, html)  # 处理PDF地址
    html = parse_audio(webId, file_name, static_file_path, domain, domain2, html)  # 处理MP3地址
    html = parse_video(webId, file_name, static_file_path, domain, domain2, html, url)  # 处理VIDEO地址
    # 获取网页编码

    # 写入本地
    if 'savetibet.ru' in url:
        with open('{}/{}.html'.format(file_path, file_name), 'w+', encoding='windows-1251') as file:
            file.write(html)
    elif 'www.youtube.com' in url:
        html = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            <video width="320" height="240" controls>
              <source src="''' + html + '''" type="video/mp4">
            
            </video>
            </body>
            </html>
        '''
        with open('{}/{}.html'.format(file_path, file_name), 'w+', encoding='utf-8') as file:
            print("写入文件的HTML：{}".format(html))
            file.write(html)
    else:
        with open('{}/{}.html'.format(file_path, file_name), 'w+', encoding='utf-8') as file:
            file.write(html)


def save_file(webId, url, response):
    file_path, file_name, domain, domain2 = mk_dir(url)  # path 存放该页面的静态文件 同样也是html页面的文件名
    print(file_path, file_name)
    save_html(webId, file_path, file_name, domain, domain2, url, response)
    return '{}/{}.html'.format(file_path, file_name), '{}/{}'.format(file_path, file_name)


if __name__ == "__main__":
    start_urls = [
        # "http://tibet.net/2018/08/his-holiness-the-dalai-lama-reiterates-importance-of-middle-way-approach/",
        # "http://tibet.net/2009/02/the-kashag-urges-china-to-withdraw-the-undeclared-martial-law-in-tibet/",
        # "http://tibet.net/2018/08/psc-announces-7-vacancies-at-office-of-auditor-general-cta/",
        # "http://tibet.net/2018/06/fifth-six-month-course-on-tibetan-language-and-buddhist-studies/",
        # "http://tibet.net/2018/08/malaysia-cancels-beijing-backed-pipelines-east-coast-rail-link/",
        # "http://tibet.net/2018/06/china-rout-has-1023-stocks-plunging-10-in-one-day/",
        # "http://tibet.net/2018/04/photo-news-nechung-kuten-rinpoche-visits-oot-washington/",
        # "http://tibet.net/2009/01/photo-news-tenshug-for-his-holiness-the-dalai-lama-in-sarnath/",
        # "http://tibet.net/2017/04/update-on-the-latest-self-immolation-protest-in-tibet/",
        # "http://tibet.net/2015/07/tibetan-monk-burns-self-in-kyegudo-self-immolation-reaches-141/",
        # "http://tibet.net/international-resolutions/us-senate-honours-his-holiness-the-dalai-lama-in-unanimous-resolution/",
        # "http://tibet.net/international-resolutions/italian-senate-committee-passes-resolution-on-tibet/",
        # "http://tibet.net/important-issues/factsheet-immolation-2011-2012/",
        # "http://tibet.net/2013/04/assessment-report-of-the-recent-landslide-event-in-the-gyama-valley/",
        # "http://tibet.net/2011/12/tibets-resource-curse/",
        # "http://tibet.net/2011/08/glacier-thawing-speeds-up-in-yangtze-river-sources/",
        # "http://tibet.net/2016/10/usaid-awards-a-grant-of-usd-23-million-to-strengthen-self-reliance-and-resilience-of-tibetan-communities-in-south-asia/",
        # "http://tibet.net/2016/10/his-holiness-the-dalai-lama-will-be-arriving-in-riga-today/",
        # "http://tibet.net/2018/07/kashags-statement-on-the-83rd-birthday-of-his-holiness-the-great-fourteenth-dalai-lama-of-tibet/",
        # "http://tibet.net/2017/03/statement-of-sikyong-on-the-58th-anniversary-of-tibetan-national-uprising-day/",
        # "http://tibet.net/2018/07/kashags-statement-on-the-83rd-birthday-of-his-holiness-the-great-fourteenth-dalai-lama-of-tibet/",
        # "http://tibet.net/2017/03/statement-of-sikyong-on-the-58th-anniversary-of-tibetan-national-uprising-day/",
        # "http://tibet.net/2013/04/assessment-report-of-the-recent-landslide-event-in-the-gyama-valley/",
        #
        # "http://xizang-zhiye.org/%E7%AC%AC%E4%B8%89%E5%8D%81%E5%85%AB%E5%B1%8A%E4%BA%BA%E6%9D%83%E7%90%86%E4%BA%8B%E4%BC%9A%E4%BC%9A%E8%AE%AE%E6%95%A6%E4%BF%83%E4%B8%AD%E5%85%B1%E9%87%8A%E6%94%BE%E6%89%8E%E8%A5%BF%E6%96%87%E8%89%B2/",
        # "http://xizang-zhiye.org/2011-01-31-08-25-01/",
        # "http://xizang-zhiye.org/%E8%AE%A9%E8%BE%BE%E8%B5%96%E5%96%87%E5%98%9B%E5%9B%9E%E5%AE%B6/",
        # "http://xizang-zhiye.org/2010-12-22-06-20-35/",
        # "http://xizang-zhiye.org/%E8%A5%BF%E8%97%8F%E5%A2%83%E5%86%85%E5%86%8D%E5%8F%91%E7%AC%AC151%E8%B5%B7%E8%87%AA%E7%84%9A%E6%8A%97%E8%AE%AE%E4%BA%8B%E4%BB%B6/",
        # "http://xizang-zhiye.org/2012-03-29-10-45-54/",
        # "http://xizang-zhiye.org/%E8%A5%BF%E8%97%8F%E9%80%9A%E8%A8%8A%E4%BA%8C%E9%9B%B6%E4%B8%80%E5%9B%9B%E5%B9%B4%E4%B8%89%E6%9C%88%E8%87%B3-%E5%85%AD%E6%9C%88%E8%99%9F/",
        # "http://xizang-zhiye.org/%E8%A5%BF%E8%97%8F%E7%82%BA%E4%BD%95%E7%87%83%E7%87%92%EF%BC%9F/",
        #
        # "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
        # "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
        # "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
        # "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
        # "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
        # "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
        # "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
        # "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
        # "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
        # "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
        # "http://tibetoffice.org/media-press/2016-tibetan-election",
        # "http://tibetoffice.org/media-press/featured-news/at-least-seven-reasons-why-beijing-is-responsible-for-the-self-immolations-in-tibet",
        # "http://tibetoffice.org/media-press/featured-news/memorandum-on-the-call-for-an-eu-special-coordinator-for-tibetan-affairs",
        # "http://tibetoffice.org/media-press/news/the-first-workshop-on-secular-ethics-and-youth-leadership-concludes-with-the-blessing-of-gyalwang-karmapa-rinpoche",
        # "http://tibetoffice.org/media-press/news/statement-of-the-kashag-on-the-occasion-of-international-solidarity-day-for-tibet-on-17-may-2014",
        # "http://tibetoffice.org/media-press/events/2016-tcv-summer-camp",
        # "http://tibetoffice.org/media-press/news/kalon-tripa-debate-2011-in-new-york",
        # "http://tibetoffice.org/media-press/march10/march-10th-chronicles-minneapolisst-paul",
        # "http://tibetoffice.org/media-press/commentaries-opinions/eat-pray-love-communist-party-road-trip-tibetan-lands-guided-china",
        # "http://tibetoffice.org/media-press/commentaries-opinions/the-dorje-shugden-conflict-an-interview-with-tibetologist-thierry-dodin",
        # "http://tibetoffice.org/picture-slide-shows/us-tom-lantos-human-rights-commission-hearing-tibet-3",
        # "http://tibetoffice.org/media-press/2016-tibetan-election",
        #
        # "http://www.tibetoffice.ch/2018/08/20/condolences-on-the-passing-away-of-kofi-annan/",
        # "http://www.tibetoffice.ch/2018/08/20/cta-president-condoles-demise-of-former-un-secretary-general-kofi-annan/",
        #
        # "http://www.tibchild.org/category/borrower/",
        # "http://www.tibchild.org/category/cash-back-offer/",
        #
        # "https://www.dalailama.com/news/2018/arrival-in-ladakh",
        #
        # "http://www.tibethouse.jp/news_release/2018/180820_HHDL_20180811.html",
        # "http://www.tibethouse.jp/news_release/2010/101025_protest.html",
        #
        # "http://www.tibet.org.tw/news_detail.php?news_id=9690",
        # "http://www.tibet.org.tw/news_detail.php?news_id=9675",
        #
        # "http://users.skynet.be/reves/tibethome.html",
        #
        # "http://tibetanlibrary.org/20th-august-2018-thai-monks-completed-their-course-at-ltwa/",
        # "http://tibetanlibrary.org/17th-august-2018-condolence-prayer/",
        #
        # "http://tibetoffice.com.au/his-holiness-the-dalai-lama-offers-condolences-at-death-of-senator-john-mccain/",
        # "http://tibetoffice.com.au/in-a-first-office-of-tibet-dc-organises-secular-ethics-and-youth-leadership-workshop/",
        # "http://tibetoffice.com.au/china-and-russia-strengthening-relationship-in-bid-to-thwart-us-dominance/",
        #
        # "http://www.men-tsee-khang.org/new-news/2018/His%20holiness%20visit%20to%20bengaluru/his%20holiness%20visit.html",
        # "http://www.men-tsee-khang.org/new-news/2018/Ladakh%20health%20talk%20august/ladakh%20healthtalk.html",
        # "http://www.men-tsee-khang.org/new-news/2018/kunphen/kunphen.html",
        #
        # "https://www.norbulingka.org/store/p177/Tibetan_Mastiff_T-shirt-black_.html",
        # "https://www.norbulingka.org/book-workshop.html",
        # "https://www.norbulingka.org/store/c18/Children.html",
        # "https://www.norbulingka.org/store/c4/Shawls.html",
        # "https://www.norbulingka.org/store/p59/Chocolate_Buray_Shawl.html",
        # "https://www.norbulingka.org/store/p61/Mustard_Buray_Shawl.html",
        # "https://www.norbulingka.org/store/c11/Malas.html",
        # "https://www.norbulingka.org/store/p83/Amethyst_Mala.html",
        #
        # "http://www.tibetanarts.org/accessories-3/",
        # "http://www.tibetanarts.org/tingshaw/",
        # "http://www.tibetanarts.org/lathed-tibetan-singing-bowl-3-75-9cm-taomm375/",
        # "http://www.tibetanarts.org/buddhas-cast-bowl-5-13cm-taobuddha5/",
        # "http://www.tibetanarts.org/classic-frosted-quartz-singing-bowl-9-432-hz-g-throat-chakra-c9gm30/",
        #
        # "http://sambhota.org/tibetan/default.html",
        # "http://sambhota.org/book-lekshey-tamgyu-1-12/",
        # "http://sambhota.org/book-rinpoche-diologue-with-petoen-students/",
        # "http://sambhota.org/tibetan/Quiz_dl2.html",
        #
        # "http://www.savetibet.org/chinese-courts-decision-to-uphold-tashi-wangchuks-prison-sentence-is-a-travesty-of-justice-ict-says/",
        # "http://www.savetibet.org/international-campaign-for-tibets-oral-statement-at-the-un-cerd-96th-session-in-geneva-on-august-7-2018/",
        # "http://www.savetibet.org/ict-urges-unesco-to-look-into-the-destruction-of-dalai-lamas-parents-home-in-tibet/",
        # "http://www.savetibet.org/rowell-fund-2019/",
        # "http://www.savetibet.org/about-ict/what-we-do/",
        #
        # "http://www.tibet.ca/en/activism/events/233",
        # "http://www.tibet.ca/en/library/wtn/14005",
        # "http://www.tibet.ca/en/library/wtn/14008",
        # "http://www.tibet.ca/en/library/media_releases/445",
        # "http://www.tibet.ca/en/library/media_releases/444",
        # "http://www.tibet.ca/en/library/photo_archive",
        # "http://www.tibet.ca/en/library/newsletter",
        #
        # "https://www.vot.org/%E0%BD%96%E0%BD%A6%E0%BD%BC%E0%BD%91%E0%BC%8B%E0%BD%93%E0%BD%98%E0%BD%A6%E0%BC%8B%E0%BD%9A%E0%BD%BA%E0%BC%8B%E0%BD%A2%E0%BD%B2%E0%BD%84%E0%BC%8B%E0%BD%95%E0%BD%A2%E0%BC%8B%E0%BD%A6%E0%BD%B2%E0%BC%8B/",
        # "https://www.vot.org/photo-gallery/?aid1=10150476912322917",
        # "https://www.vot.org/photo-gallery/?aid1=10153209453277917",
        # "https://www.vot.org/audio-features-archives/?type=history",
        # "https://www.vot.org/secular-ethics/",
        # #
        # "http://www.phayul.com/news/article.aspx?id=40695&article=Two+Tibetans+released+from+prison%2c+both+served+sentence+for+%E2%80%9Cinciting+separatism%E2%80%9D",
        # "http://www.phayul.com/news/article.aspx?c=8&t=1&id=39353&article=The+Paradox+of+Samsara%2c+Review+of+%E2%80%9CJigden%3a+The+Beginning+of+the+End%E2%80%9D",
        # "http://www.phayul.com/news/article.aspx?id=40711&article=Pro-Tibet+groups+slam+Google+over+plans+to+develop+censored+search+engine+in+China",
        # "http://www.phayul.com/news/article.aspx?id=40715&article=Middle+school+students+in+Occupied-Tibet+forced+to+undergo+military+training",
        #
        # "http://worldbridges.com/Tibet/2000/freespirit/index.html",
        # "http://worldbridges.com/Tibet/video/index.html",
        # "http://worldbridges.com/Tibet/Losar/index.html",
        # "http://worldbridges.com/Tibet/Dharamsala/index.html",
        # "http://worldbridges.com/Tibet/Dharamsala/guide/index.html",
        # "http://worldbridges.com/Tibet/Losar/main/index.html",
        # "http://worldbridges.com/Tibet/Tipa/jdorjeeiv.html",
        #
        # "http://dharamsalanet.com/links/teachings.htm",
        # "http://dharamsalanet.com/links/articles.htm",
        # "http://dharamsalanet.com/links/associations.htm",
        # "http://dharamsalanet.com/links/support.htm",
        # "http://dharamsalanet.com/links/worldnews.htm",
        # "http://dharamsalanet.com/links/weather.htm",
        # "http://dharamsalanet.com/links/webradio.htm",
        # "http://dharamsalanet.com/links/technology.htm",
        # "http://dharamsalanet.com/links/guides.htm",
        # "http://dharamsalanet.com/links/health.htm",
        # "http://dharamsalanet.com/links/women.htm",
        # "http://dharamsalanet.com/links/culture.htm",
        # "http://dharamsalanet.com/links/meditation.htm",
        #
        # "https://www.kagyuoffice.org.tw/karmapa-office/announcement/announcement-20080805",
        # "https://www.kagyuoffice.org.tw/karmapa-office/announcement/20130801",
        # "https://www.kagyuoffice.org.tw/karmapa-office/announcement/20151208",
        # "https://www.kagyuoffice.org.tw/karmapa-office/announcement/announcement-19921203",
        #
        # "http://kunphen.center/activities-at-kunphen-center/awarenes-and-fundraise-event/",
        # "http://kunphen.center/whats-happening-at-kunphen-center/plantation-by-boys-at-the-new-rahab-site/",
        # "http://kunphen.center/activities-at-kunphen-center/world-hepatitis-day-28th-july-2017/",
        # "http://kunphen.center/whats-happening-at-kunphen-center/hhdl-praises-kunphen-center/",
        # "http://kunphen.center/whats-happening-at-kunphen-center/client-gets-married/",
        # "http://kunphen.center/client-stories/",
        # "http://kunphen.center/about-kunphen-center-dharamsala/kunphen-center-magazine-2017/",
        # "http://kunphen.center/activities/",
        #
        # "https://www.amnesty.org/en/latest/news/2018/08/indonesia-dozens-killed-on-the-streets-in-police-crackdown-ahead-of-asian-games/"
        # "https://www.amnesty.org/en/search/?country=38526",
        # "https://www.amnesty.org/en/latest/news/2018/08/nigeria-sars-overhaul-is-positive-step-but-reforms-must-be-robust/",
        # "https://www.amnesty.org/en/latest/news/2018/08/malaysia-100-days-in-power-government-still-has-much-to-do-on-human-rights/",
        # "https://www.amnesty.org/en/latest/news/2018/08/turkey-amnesty-turkeys-chair-released-after-more-than-a-year-behind-bars/",
        # "https://www.amnesty.org/en/latest/research/",
        # "https://www.amnesty.org/en/get-involved/join/",
        # "https://www.amnesty.org/en/get-involved/take-action/",
        # "https://www.amnesty.org/en/who-we-are/",
        # "https://www.amnesty.org/en/what-we-do/",
        #
        # "http://tibetkommissionen.dk/node/39",
        # "http://tibetkommissionen.dk/node/38",
        # "http://tibetkommissionen.dk/node/37",
        # "http://tibetkommissionen.dk/node/35",
        # "http://tibetkommissionen.dk/node/31",
        # "http://tibetkommissionen.dk/node/32",
        # "http://tibetkommissionen.dk/node/29",
        #
        # "https://www.tibet-initiative.de/tsewang-norbu-founding-member-and-advisory-board-member-of-tibet-initiative-germany-passed-away/",
        # "https://www.tibet-initiative.de/tsewang-norbu-gruendungsmitglied-und-beiratsmitglied-der-tibet-initiative-deutschland-ist-verstorben/",
        # "https://www.tibet-initiative.de/gedenkfeier-fuer-liu-xiaobo-in-berlin/",
        # "https://www.tibet-initiative.de/tsewang-norbu-founding-member-and-advisory-board-member-of-tibet-initiative-germany-passed-away/",
        # "https://www.tibet-initiative.de/tashi-wangchuk-berufung-wurde-abgelehnt/",
        # "https://www.tibet-initiative.de/work/natalia-woerner/",
        # "https://www.tibet-initiative.de/work/ai-weiwei/",
        # "https://www.tibet-initiative.de/work/tanja-kinkel/",
        # "https://www.tibet-initiative.de/tsewang-norbu-gruendungsmitglied-und-beiratsmitglied-der-tibet-initiative-deutschland-ist-verstorben/",
        #
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=630",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=3",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=100&item=1",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=810",
        # "https://achtsamkeitstraining-freiburg.de/events/mbsr-kurs-freiburg-september-oktober-2018-donnerstag/",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=30",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=20",
        # "https://www.tibet-kailash-haus.de/index.php?TKH=c7238e1cc374395a82b9bb25000d2a05&id=600",
        # "https://www.tibet-kailash-haus.de/index.php?id=0",
        #
        # "https://cesitibetpodporuji.cz/blahoprejeme-svatosti-dalajlamovi-k-vyroci-83-narozenin-congratulations-h-h-dalai-lama-with-the-83rd-birthday-anniversary/",
        # "https://cesitibetpodporuji.cz/hlas-pro-tibet/",
        # "https://cesitibetpodporuji.cz/tibetsky-test-pristiho-prezidenta/",
        # "https://cesitibetpodporuji.cz/ucitel-tibetskeho-buddhismu-maleho-tibetu-prijizdi-potreti-cr/",
        # "https://cesitibetpodporuji.cz/tiskova-zprava-film-2017-festival-tibetskych-filmu-filmu-tibetu/",
        # "https://cesitibetpodporuji.cz/tibet-cinsti-delnici-demontuji-budovy-jednom-nejvetsich-tibetskych-mestecek-larung-gar-ktere-slouzi-jako-vyznamna-buddhisticka-vzdelavaci-akademie/",
        # "https://cesitibetpodporuji.cz/event/svatost-dalajlama-hradcanskem-namesti/",
        # "https://cesitibetpodporuji.cz/event/tibet-solidarity-rally-zeneva/",
        # "https://cesitibetpodporuji.cz/event/audience-u-dalailamy-dharamsale/",
        #
        # "http://freetibetusa.weebly.com/why-tibet.html",
        # "http://freetibetusa.weebly.com/news",
        # "http://freetibetusa.weebly.com/news/october-10th-2013",
        # "http://freetibetusa.weebly.com/news/the-gyalwang-karmapa-offers-condolences-at-the-tragic-passing-away-of-dr-choje-akong-tulku-rinpoche-oct8th-2013-new-delhi",
        # "http://freetibetusa.weebly.com/get-involved.html",
        # "http://freetibetusa.weebly.com/donate.html",
        # "http://freetibetusa.weebly.com/shop.html",
        #
        # "http://tibetanscientificsociety.com/Portal/Home",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/38/?Title=Snapshots-from-Tibetan-Science-Conclave---IV-in-Bangalore",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/35/?Title=Tibetan-Students-and-Researchers-Converge-for-a-Science-Meet-(Press-Release)",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/30/?Title=TSS-Members-Participate-in-MIND-&-LIFE-XXX",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/32/?Title=Project-Grant-from-Tibetan-Scientific-Society---2016",
        # "http://tibetanscientificsociety.com/Portal/EventDetail/24/?Title=Tibetan-Science-Conclave---II",
        # "http://tibetanscientificsociety.com/Portal/EventDetail/22/?Title=Important-Updates-on-Tibetan-School-Science-Essay-Contest-",
        # "http://tibetanscientificsociety.com/Portal/News",
        # "http://tibetanscientificsociety.com/Portal/Events",
        # "http://tibetanscientificsociety.com/Portal/VideoGallery",
        # "http://tibetanscientificsociety.com/Portal/Videos/5/?Title=Engineering-and-Technology",
        # "http://tibetanscientificsociety.com/Portal/Page/SupportUs",
        # "http://tibetanscientificsociety.com/Portal/Page/Contact",
        # "http://tibetanscientificsociety.com/Portal/Articles",
        # "http://tibetanscientificsociety.com/Portal/ArticleDetail/37/?Title=Phantom-Limbs-A-Quirk-of-the-Brain!",
        # "http://tibetanscientificsociety.com/Portal/ArticleDetail/23/?Title=The-Need-for-a-Quantum-Theory-of-Light-and-Matter",
        # "http://tibetanscientificsociety.com/Member/Users",
        # "http://tibetanscientificsociety.com/Member/User/ddolkar",
        # "http://tibetanscientificsociety.com/Member/User/Dekyi",
        # "http://tibetanscientificsociety.com/Portal/Page/AimsAndObjective",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/20/?Title=2nd-Tibetan-School-Science-Essay-Competition---2013",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/30/?Title=TSS-Members-Participate-in-MIND-&-LIFE-XXX",
        # "http://tibetanscientificsociety.com/Portal/NewsDetail/28/?Title=TSC-Participants-Take-Part-in-Ethics-Conference",
        # "http://tibetanscientificsociety.com/Portal/Video/18/?Title=Kunleng-VOA---19.04.2017-",
        # "http://tibetanscientificsociety.com/Portal/Video/17/?Title=Airplane-History",  # 该视频无法播放 失效了

        ## 视频文件名字太长 导致报错
        # "http://www.tibetonline.tv/sikyongs-talks-and-visits/",
        # "http://www.tibetonline.tv/tibet-policys-talk/", # 视频文件名字太长 导致报错
        # "http://www.tibetonline.tv/ttvnews/",
        # "http://www.tibetonline.tv/ttvnews/?ytpage1=6",
        # "http://www.tibetonline.tv/middle-way-approach-policy/",
        # "http://www.tibetonline.tv/documentaries-films/",
        # "http://www.tibetonline.tv/cultural/",
        # "http://www.tibetonline.tv/live-webcast-from-cta-dharamsala/",

        "http://www.dalailamaworld.com/topic.php?t=1039&sid=dbfb0147349ad3622758197dc30ef1dd",
        "http://www.dalailamaworld.com/topic.php?t=1038&sid=dbfb0147349ad3622758197dc30ef1dd",
        "http://www.dalailamaworld.com/topic.php?t=1037&sid=dbfb0147349ad3622758197dc30ef1dd",
        "http://www.dalailamaworld.com/topic.php?t=1035&sid=dbfb0147349ad3622758197dc30ef1dd",

        "https://www.tibethaus.com/programm/aktuelles-programm.html",
        "https://www.tibethaus.com/programm/studium-buddhismus.html",
        "https://www.tibethaus.com/programm/studium-buddhismus/ab-mai-2017-lorig.html",
        "https://www.tibethaus.com/programm/studium-buddhismus/ab-august-2017-praxis.html",
        "https://www.tibethaus.com/programm/studium-buddhismus/ab-sept-2017-lamrim.html",
        "https://www.tibethaus.com/programm/studium-buddhismus/ab-januar-2019-ttm.html",
        "https://www.tibethaus.com/index.php?id=591&L=0",
        "https://www.tibethaus.com/programm/besuch-von-schulklassen.html",
        "https://www.tibethaus.com/tibethaus-kulturstiftung.html",
        "https://www.tibethaus.com/publikationen/buecher.html",
        "https://www.tibethaus.com/programm/meditation-praxis.html",
        "https://www.tibethaus.com/programm/studium-buddhismus.html",
        "https://www.tibethaus.com/programm/besuch-von-schulklassen.html",
        "https://www.tibethaus.com/publikationen/buecher.html",
        "https://www.tibethaus.com/publikationen/details/artikel/aus-dem-herzen-gesprochen.html",
        "https://www.tibethaus.com/publikationen/details/artikel/in-the-service-of-the-13th-and-14th-dalai-lamas.html",
        "https://www.tibethaus.com/publikationen/details/artikel/tibetischer-buddhismus-im-westen.html",
        "https://www.tibethaus.com/publikationen/buecher/kategorie/vajrabhairava-yamantaka-1.html",
        "https://www.tibethaus.com/publikationen/buecher/kategorie/vajrasattva.html",
        "https://www.tibethaus.com/shugden-konflikt.html",
        "https://www.tibethaus.com/mitarbeiter-vor-ort.html",
        "https://www.tibethaus.com/programm/kompakt-kurse.html",
        "https://www.tibethaus.com/programm/woechentlich.html",
        "https://www.tibethaus.com/kunst-kultur/ausstellungen.html",
        "https://www.tibethaus.com/heilkunde/kurse.html",
        "https://www.tibethaus.com/wissenschaft/tibetologie.html",
        "https://www.tibethaus.com/wissenschaft/dialog.html",
        "https://www.tibethaus.com/heilkunde/kurse.html",
        "https://www.tibethaus.com/programm/aktuelles-programm/detailansicht/calendar/2018/11/02/event/tx_cal_phpicalendar/abendvortrag-dr-namgyal-optional.html"

        "http://www.tibet-institut.ch/content/tir/de/about_us_only.html",
        "http://www.tibet-institut.ch/content/tir/en/about_us_only.html",
        "http://www.tibet-institut.ch/content/tir/de/monastic_community.html",
        "http://www.tibet-institut.ch/content/tir/de/library.html",
        "http://www.tibet-institut.ch/content/tir/de/donation.html",
        "http://www.tibet-institut.ch/content/tir/de/documents.html",
        "http://www.tibet-institut.ch/content/tir/de/contacts.html",
        "http://www.tibet-institut.ch/content/tir/bod/about_us.html",

        "http://www.panditatranslation.org/copy-of-3-2",
        "http://www.panditatranslation.org/copy-of-2",
        "http://www.panditatranslation.org/link2",

        "http://tibetanwomen.org/the-four-major-ngos-from-dharamsala-has-organised-a-peaceful-cycle-rally-from-mcleod-ganj-main-square-to-norbulingka-to-commemorate-the-2008-national-uprising-in-tibet/",
        "http://tibetanwomen.org/women-in-tibet/",
        "http://tibetanwomen.org/books-reports/",
        "http://tibetanwomen.org/support/intern/",
        "http://tibetanwomen.org/newsletters/",
        "http://tibetanwomen.org/history/",
        "http://tibetanwomen.org/team/",
        "http://tibetanwomen.org/the-four-ngos-also-organised-a-similar-cycle-rally-at-delhi-starting-from-tibetan-camp-manju-ka-tilla-to-indian-parliament-street-with-the-sincere-participations-of-the-50-students-from-delhi-colleges/",
        "http://tibetanwomen.org/category/b-key-activities/4-research-media/",

        "http://savetibet.ru/2018/08/21/drepung-gomang.html",
        "http://savetibet.ru/2018/08/18/dalai-lama-14.html",

        "https://www.youtube.com/watch?v=KJjZEt7A6nU",
        "https://www.youtube.com/watch?v=FO2j96HhanI",
        #

        #

        #

        #

        #

        #
        # # 没有处理视频文件
        # "http://tchrd.org/annual-report-2014-human-rights-situation-in-tibet/",
        # "http://tchrd.org/un-committee-seeks-additional-information-from-china-on-elimination-of-racial-discrimination/",
        # "http://tchrd.org/china-deploys-security-forces-to-prevent-tibetans-from-protesting-water-diversion-project/",
        # "http://tchrd.org/two-tibetans-convicted-for-inciting-separatism-released-after-serving-long-prison-terms/",
        # "http://tchrd.org/tchrd-releases-2013-annual-report-and-special-report-on-re-education-through-labor/",
        #
        # # http://www.tcewf.org/ 跳转过来的
        # "http://sherig.org/en/category/announcement/job-vacancy/",
        # "http://sherig.org/en/correspondence-course-scholarship-2018/",
        # "http://sherig.org/en/2019-berea-college-scholarship/",

        # 处理好了
        # "http://www.tibetanreview.net/china-calls-on-its-panchen-to-shun-the-dalai-lama/",
        # "http://www.tibetanreview.net/chinas-minority-affairs-boss-emphasizes-sinicization-of-religion-during-tibet-tour/",

    ]
    for url in start_urls:
        save_file("1", url)
