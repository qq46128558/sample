#!/usr/bin/env python3

""" 爬取在线教程转成pdf """

__author__='王强'

# https://readthedocs.org

from bs4 import BeautifulSoup
import requests
from requests.exceptions import RequestException
import pdfkit
import os

# 全局变量
base_url="http://python3-cookbook.readthedocs.io/zh_CN/latest/"
book_name=""
chapter_info=[]

def parse_title_and_url(html):
    """
    解析全部章节的标题和url
    :param html: 需要解析的网页内容
    :return None
    """
    soup=BeautifulSoup(html,'html.parser')

    # 获取书名
    book_name=soup.find('div',class_='wy-side-nav-search').a.text
    menu=soup.find_all('div',class_='section')
    chapters=menu[0].div.ul.find_all('li',class_='toctree-l1')
    for chapter in chapters:
        info={}
        # 获取一级标题和url
        # 标题中含有'/'和'*'会保存失败
        info['title']=chapter.a.text.replace("/",'').replace('*','')
        info['url']=base_url+chapter.a.get('href')
        info['child_chapters']=[]
        # 获取二级标题和url
        if chapter.ul is not None:
            child_chapters=chapter.ul.find_all('li')
            for child in child_chapters:
                url=child.a.get('href')
                # 如果在url中存在'#'，则此url为页面内链接，不会跳转到其他页面
                # 所以不需要保存
                if '#' not in url:
                    info['child_chapters'].append({
                        'title':child.a.text.replace('/','').replace('*',''),
                        'url':base_url+url,
                    })
        chapter_info.append(info)
        '''
        [
            {
                'title': 'first_level_chapter',
                'url': 'www.xxxxxx.com',
                'child_chapters': [
                    {
                        'title': 'second_level_chapter',
                        'url': 'www.xxxxxx.com',
                    }
                    ...            
                ]
            }
            ...
        ]
        '''

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""

# 构造html下载器
def get_one_page(url):
    try:
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Accept-Language': 'zh,zh-CN;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Host': 'python3-cookbook.readthedocs.io',
            }
        res=requests.get(url,headers=headers)
        if res.status_code==200:
            return res.text
        return None
    except RequestException:
        return None

def get_content(url):
    """
    解析URL，获取需要的html内容
    :param url: 目标网址
    :return: html
    """
    html=get_one_page(url)
    soup=BeautifulSoup(html,'html.parser')
    # 一级目录内容的元素位置和二级目录内容的元素位置相同
    content=soup.find('div',attrs={'itemprop':'articleBody'})
    html=html_template.format(content=content)
    return html

def save_pdf(html,filename):
    """
    把所有html文件保存到pdf文件
    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }

    pdfkit.from_string(html,filename,options=options)

def parse_html_to_pdf():
    """
    解析URL，获取html，保存成pdf文件
    :return: None
    """
    try:
        for chapter in chapter_info:
            ctitle=chapter['title']
            url=chapter['url']
            # 文件夹不存在则创建（多级目录）
            dir_name=os.path.join(os.path.dirname(__file__),'gen',ctitle)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            # 一级目录内容的元素位置和二级目录内容的元素位置相同
            html=get_content(url)
            padf_path=os.path.join(dir_name,ctitle+".pdf")
            save_pdf(html,padf_path)

            children=chapter['child_chapters']
            if children:
                for child in children:
                    html=get_content(child['url'])
                    pdf_path=os.path.join(dir_name,child['title']+'.pdf')
                    save_pdf(html,pdf_path)
    except Exception as e:
        print(e)


if __name__=='__main__':
    html=get_one_page(base_url)
    parse_title_and_url(html)
    # parse_html_to_pdf()
    print(chapter_info)

