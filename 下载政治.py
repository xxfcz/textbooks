#-*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

# 答案圈
resp = requests.get('http://www.mxqe.com/qnj/50278.html')
resp.encoding = 'utf-8'
html = resp.text
soup = BeautifulSoup(html)
div_content = soup.find('div', class_='m-cmsinfo-cont')
root_dir = r'E:\download\政治'
if not os.path.exists(root_dir):
        os.makedirs(root_dir)
img_list = div_content.find_all('img')
page=0
for img in img_list:
    page=page+1
    src = 'http://www.mxqe.com/' + img['src']
    print(page, src, sep=',')
    r2 = requests.get(src)
    with open(root_dir+"\\"+ '{0:02d}.jpg'.format(page) ,'wb') as f:
        f.write(r2.content)
        f.close()
        print('文件保存成功')
