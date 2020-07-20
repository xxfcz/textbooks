#-*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup


root_dir = r'E:\download\历史'
if not os.path.exists(root_dir):
        os.makedirs(root_dir)

for page in range(17):
    fn = f'{page}.jpg'
    url = f'https://bkw-legacy.oss-cn-shenzhen.aliyuncs.com/transform/2020-03-20/kUgGWPrlTPerDcnzM5iEBA/{page}.jpg'
    print('正在下载 ' + url)
    res = requests.get(url)
    with open(root_dir+"\\"+ '{0:02d}.jpg'.format(page) ,'wb') as f:
        f.write(res.content)
        f.close()
        print(f'{fn} 文件保存成功')

#html = resp.text
#soup = BeautifulSoup(html, 'html.parser')
#div_content = soup.find('div', class_='detail-type-content')

