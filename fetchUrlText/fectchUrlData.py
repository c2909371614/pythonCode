#coding = utf-8
import requests
from bs4 import BeautifulSoup
import re

def download_text():
    url = 'https://www.runoob.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # print(text)


# !/user/bin/env python
# -*- coding: utf-8 -*-
# des: 下载任何网页的图片

def download_img():
    error_count = 0
    success_count = 0
    url = input('请输入您要下载的图片的网址：')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75'
    }

    web_text = requests.get(url, headers=headers).text

    ex = '<img.*?src="(.*?)".*?'
    img_list = re.findall(ex, web_text)
    print('图片地址:', img_list)
    if len(img_list) == 0:
        print('该网站有反爬虫机制，爬取失败，请换个网站继续尝试。')

    for img in img_list:
        try:
            # 补充协议头
            if not (img.startswith('http') or img.startswith('https')):
                img = 'http:' + img
            img_binary = requests.get(img, headers=headers).content
            # 切割出最后一个字符串
            file_name = img.split('/')[-1]
            # 切割 query字符
            file_name = file_name.split('?')[0]
            with open(f'./img/{file_name}', 'wb') as fp:
                fp.write(img_binary)
            print(file_name, '，下载成功')
            success_count += 1
        except Exception as e:
            print(e)
            error_count += 1
        continue
    print('下载图片结束！')
    return success_count, error_count


if __name__ == '__main__':
    success_count, error_count = download_img()
    print(f'总计下载：{success_count}，下载失败：{error_count}')

