'''
Created on 2017. 7. 24.

@author: Bit
'''


import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from time import sleep
from collections import OrderedDict

driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

home_url = 'http://www.casamiashop.com/main.casa'
basic_url = 'http://www.casamiashop.com'


url = 'http://www.casamiashop.com/category/category.casa?ctgy_code=20002'
pages_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42']
"""
def kk():
    driver.refresh()
    driver.get(url)
    
    all_links = []
    
    for i in pages_num:
        page_num = driver.find_element_by_link_text(i)
        driver.implicitly_wait(5)
        page_num.click()
        
        sleep(2)

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
            page_next.click()        
            #sleep(3)
            
    return all_links

ff = kk()
print(ff)
"""

def fetch_pages_num(URL):      
    driver.refresh()
    driver.get(URL)
    print(URL)
   
    #sleep(3)
    all_pages_nums_text = []   

    
    for k in range(0,5): 
        if k>0:
            page_next = driver.find_element_by_partial_link_text('다음페이지')
            driver.implicitly_wait(5)
            page_next.click()
            sleep(2)
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
        except AttributeError:
            print('pages_nums에러발생')
            pages_nums_text = ['1']
    
        for j in pages_nums_text:
            all_pages_nums_text.append(j)
        
    
    all_pages_nums_int = []
    
    for k in all_pages_nums_text:
        all_pages_nums_int.append(int(k))
    
    mySet = set(all_pages_nums_int)
    changed_list = list(mySet)

    all_pages_nums_text = []
    
    for i in changed_list:
        all_pages_nums_text.append(str(i))

    print(all_pages_nums_text)
    
    return all_pages_nums_text

kk = fetch_pages_num(url)
print(kk)