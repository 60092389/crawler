'''
Created on 2017. 8. 1.

@author: Bit
'''


import urllib.request
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from time import sleep
from collections import OrderedDict
import mongoConnect
from pip._vendor.requests.utils import _null
from selenium.common.exceptions import NoSuchElementException
import cx_Oracle


#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=100719426&trTypeCd=20&trCtgrNo=585021'

def review_fetch():
   #driver.refresh()
    driver.get(site)

    driver.switch_to_frame('ifrmReview')
    text = driver.find_element_by_class_name('review_list').text
    
    
    #contents = driver.find_elements_by_class_name('summ_conts')
    
    all_review_contents = ''
    all_pages_nums_text = []
    page_nums_arr = []
    while True:
        page_nums = driver.find_element_by_class_name('s_paging_v2').text
        
        page_nums_arr = re.split(' ', page_nums)
        all_pages_nums_text = all_pages_nums_text + page_nums_arr
        print(page_nums_arr)        
        try:
            next_click = driver.find_element_by_class_name('next')
            next_click.click()
            driver.implicitly_wait(1)
            sleep(1)
            print('다음페이지 클릭')
        except NoSuchElementException:
            print('엘스문')
            break  
        
    print('와일문나옴')
    print(all_pages_nums_text)
    print(len(all_pages_nums_text))
    
    driver.get(site)
    driver.switch_to_frame('ifrmReview')
    page_num_div = driver.find_element_by_class_name('s_paging_v2')
    test = page_num_div.find_element_by_partial_link_text('3')
    print(test.text)
    
    
    
    for i in all_pages_nums_text:
        driver.implicitly_wait(2)
        print(i)
        if int(i)%10 != 1:
            #page_num_div = driver.find_element_by_class_name('s_paging_v2')
            #driver.implicitly_wait(2)
            page_num = driver.find_element_by_link_text(i)
            driver.implicitly_wait(2)
            page_num.click()
            sleep(1)
        
        contents = driver.find_elements_by_class_name('summ_conts')
        for j in range(0,len(contents)):
            #print(contents[j].text)
            all_review_contents = all_review_contents + '\n' + contents[j].text
            
        if int(i)%10 == 0:
            next_click = driver.find_element_by_class_name('next')
            next_click.click()
            driver.implicitly_wait(3)
            sleep(1)
            print('다음페이지 클릭')
            
            
            #all_reivew_contents = all_reivew_contents +'\n' + contents.text
            #print(contents.text)

    print(all_review_contents)
        
review_fetch()        
        
        
        