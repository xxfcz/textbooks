
# %%
import requests
from bs4 import BeautifulSoup

#headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
resp = requests.get('http://www.mxqe.com/qnj/50286.html')
resp.encoding = 'utf-8'  # 关键
html = BeautifulSoup(resp.text, 'html.parser')
print(html)

# %%
