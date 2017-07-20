'''
Created on 2017. 7. 19.

@author: Bit
'''

import urllib.request
from bs4 import BeautifulSoup
import re

target_url = [
    
    ]

basic_url = 'http://www.casamiashop.com'

def fetch_post_list(URL):
    real_URL = URL
    res = urllib.request.urlopen(real_URL)
    html = res.read()
 
    
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='index_wrap')
    content_wrap = soup.find_all('div', class_='content_wrap')
    sub_page = content_wrap[1].find('div', class_='sub_pagenation_wrap')
    #print(content_wrap[1])
    #clear_div = content_wrap[1].find('div', class_='clear_div')
    #print(clear_div)
    #goodsIn = clear_div.find('div', id='goodInCategotyView')
    #print(goodsIn)
    
    links = []
    #links = [basic_url + ab.find('a')['href'] for ab in div_link_list]
    
    return soup;

result = fetch_post_list('http://www.casamiashop.com/category/category.casa?ctgy_code=20254')
print(result)
    