'''
Created on 2017. 7. 19.

@author: Bit
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from time import sleep


#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

home_url = 'http://www.casamiashop.com/main.casa'
basic_url = 'http://www.casamiashop.com'

"""
def fetch_fur_kind_link():
    driver.get(home_url)
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.find('div', id='gnb_all')
    link = div.find_all('li')
    
    links = []
    links = [basic_url+ab.find('a')['href'] for ab in link]
    
    total_links = []
    for i in range(0,10):
        total_links.append(links[i])
    
    for i in range(14,19):
        total_links.append(links[i])

    return total_links
    
"""
"""
result = fetch_fur_kind_link()
print(result)
"""

def fetch_fur_list(URL):
    driver.get(URL)
   
    #page_div = driver.find_element_by_class_name('sub_pagenation_wrap')
    page_num = driver.find_element_by_link_text('1')
    #page_next = driver.find_element_by_partial_link_text('다음페이지')
    driver.implicitly_wait(5)
    page_num.click()
    #page_next.click()
   
    sleep(3)
    
    
    page_sources = driver.page_source
    temp_soup = BeautifulSoup(page_sources, 'html.parser')
    page_nums_div = temp_soup.find('div', class_='sub_pagenation_wrap')
    pages_nums = []
    pages_nums = page_nums_div.find_all('li')
    pages_nums_text = []
    pages_nums_text = [ab.find('a').text for ab in pages_nums]
    print(pages_nums_text)
    
    
   
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    goods_view= soup.find('div', id='goodsInCategoryView')
    goods_list_thumb = goods_view.find_all('div', class_='goods_list_thumb')
    
    links = []
    links = [basic_url+ab.find('a')['href'] for ab in goods_list_thumb]


    return links

result = fetch_fur_list('http://www.casamiashop.com/category/category.casa?ctgy_code=20002')
print(result)
    
    


"""
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
"""
    