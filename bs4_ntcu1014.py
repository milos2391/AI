#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install beautifulsoup4')


# In[2]:


import requests
from bs4 import BeautifulSoup

# 下載 數位系網 首頁內容
url = 'https://dct.ntcu.edu.tw/news_content.php'
r = requests.get(url)

# 確認是否下載成功
if r.status_code == requests.codes.ok:
  # 以 BeautifulSoup 解析 HTML 程式碼
  soup = BeautifulSoup(r.text, 'html.parser')

  a_tags = soup.find_all('a')
  for tag in a_tags:
    # 輸出超連結的文字
    print('網址：'+str(tag.string)+' -> '+tag.get('href'))    
    #print(tag.get('href'))

