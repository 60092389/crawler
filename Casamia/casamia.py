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
from collections import OrderedDict
import casamia_contents_test
import mongoConnect

conn = mongoConnect.collection




#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

home_url = 'http://www.casamiashop.com/main.casa'
basic_url = 'http://www.casamiashop.com'


def fetch_fur_kind_link():
    #driver.get(home_url)
    
    #html = driver.page_source
    
    
    real_URL = home_url
    res = urllib.request.urlopen(real_URL)
    html = res.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    
    div = soup.find('div', id='gnb_all')
    link = div.find_all('li')
    
    links = []
    links = [basic_url+ab.find('a')['href'] for ab in link]
    
    total_links = []
    #for i in range(0,2):
    #for i in range(1,2):
    #    total_links.append(links[i])
    #for i in range(3,10):
    #    total_links.append(links[i])
    for i in range(4,10):
        total_links.append(links[i])    
    for i in range(14,19):
        total_links.append(links[i])
    
    return total_links
    



def fetch_pages_num(URL):      
    driver.refresh()
    driver.get(URL)
    print(URL)
   
    #sleep(3)
    all_pages_nums_text = []   

    
    for k in range(0,5): 
        if k>0:
            
            try:
                page_next = driver.find_element_by_partial_link_text('다음페이지')
                driver.implicitly_wait(6)
                page_next.click()
                sleep(3)
            except:
                page_next = driver.find_element_by_partial_link_text('다음페이지')
                driver.implicitly_wait(6)
                print('pagenum 세기 에러')
                page_next.click()
                sleep(3)
        else:
            driver.implicitly_wait(5)
            sleep(2)
            
        pages_nums_text = []
        try:  
            page_sources = driver.page_source
            temp_soup = BeautifulSoup(page_sources, 'html.parser')
            page_nums_div = temp_soup.find('div', class_='sub_pagenation_wrap')
            pages_nums = []
            pages_nums = page_nums_div.find_all('li')
        
            
            pages_nums_text = [ab.find('a').text for ab in pages_nums]
        except:
            print('pages_nums에러발생')
            pages_nums_text = ['1']
    
        for j in pages_nums_text:
            all_pages_nums_text.append(j)
        
    
    all_pages_nums_int = []
    
    for k in all_pages_nums_text:
        all_pages_nums_int.append(int(k))
    
    mySet = set(all_pages_nums_int)
    changed_list = list(mySet)
    #print(sorted(changed_list))
    
    all_pages_nums_text = []
    
    for i in changed_list:
        all_pages_nums_text.append(str(i))

    print(all_pages_nums_text)
    
    return all_pages_nums_text


def fetch_post_link(url, pages_num):
    driver.refresh()
    driver.get(url)
    
    all_links = []
    
    for i in pages_num:
        
        try:
            page_num = driver.find_element_by_link_text(i)
            print(i)
            print(page_num)
            driver.implicitly_wait(7)
            page_num.click()
            sleep(3)
        except:
            print('Pagenum 클릭에러')
            driver.refresh()
            page_num = driver.find_element_by_link_text(i)
            driver.implicitly_wait(8)    
            page_num.click()
            sleep(5)
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
    
        goods_view= soup.find('div', id='goodsInCategoryView')
        goods_list_thumb = goods_view.find_all('div', class_='goods_list_thumb')
    
        links = []
        links = [basic_url+ab.find('a')['href'] for ab in goods_list_thumb]
        
        all_links = all_links + links
        
        if int(i)%10==0:
            page_next = driver.find_element_by_partial_link_text('다음페이지')
            driver.implicitly_wait(5)
            try:
                page_next.click()
            except:
                print('다음페이지 클릭 에러')
                page_next.click()
                sleep(3)
        

    return all_links

#result = fetch_pages_num('http://www.casamiashop.com/category/category.casa?ctgy_code=20012')
#print(result)
"""
url = 'http://www.casamiashop.com/category/category.casa?ctgy_code=20012'
pages_num = ['1','2','3','4','5','6','7','8','9','10','11','12']

ok = fetch_post_link(url, pages_num)

print(ok)
"""



url_links = fetch_fur_kind_link()
print(url_links)

total_links_count = 0
total_contents_count = 0
for url in url_links:
    pages_nums = fetch_pages_num(url)
    post_links = fetch_post_link(url,pages_nums)
    for link in post_links:
        try:
            contents = casamia_contents_test.ferch_post_contents(link)      
            conn.insert(contents)
            print(contents)           
            total_contetns_count = total_contents_count +1
            print(total_contents_count)
        except:
            print('컨텐츠에서 에러')
            continue
print(total_contents_count)  





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
    