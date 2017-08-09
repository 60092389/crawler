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
import pymongo
from pip._vendor.requests.utils import _null
from selenium.common.exceptions import NoSuchElementException
import os


#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1322253347&trTypeCd=20&trCtgrNo=585021&lCtgrNo=1001364&mCtgrNo=1002273'
#site= 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=96531135&trTypeCd=20&trCtgrNo=1002273'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=32074832&trTypeCd=20&trCtgrNo=1002276'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1367968916&trTypeCd=20&trCtgrNo=1002276'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1335741053&trTypeCd=21&trCtgrNo=1002276'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1319927303&trTypeCd=20&trCtgrNo=1002276'

site_arr = ['http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1319927303&trTypeCd=20&trCtgrNo=1002276',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=247446895&trTypeCd=20&trCtgrNo=1002278',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=59339435&trTypeCd=20&trCtgrNo=1002278',
            'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=121939108&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=80528149&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=711796698&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=54588902&trTypeCd=20&trCtgrNo=1002279',
            'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=700206758&trTypeCd=21&trCtgrNo=1002279']

p = 7

def review_fetch(site):
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
    driver.implicitly_wait(2)
    sleep(1)
    driver.switch_to_frame('ifrmReview')
    page_num_div = driver.find_element_by_class_name('s_paging_v2')
    test = page_num_div.find_element_by_partial_link_text('3')
    print(test.text)
    

    
    
    for i in all_pages_nums_text:
        driver.implicitly_wait(2)
        print(i)
        sleep(1)
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
            try:
                next_click = driver.find_element_by_class_name('next')
                next_click.click()
                driver.implicitly_wait(3)
                sleep(1)
                print('다음페이지 클릭')
            except:
                print('다음페이지 없음')
            
            
            #all_reivew_contents = all_reivew_contents +'\n' + contents.text
            #print(contents.text)
            
    print(all_review_contents)
    
    fur_no = str(p)

  
    return {
        'fur_no' : fur_no,
        'fur_name' : '아아아아아',
        'fur_est_contents' : all_review_contents
        }


for site in site_arr:
    result = review_fetch(site)

    print(os.getcwd())

#os.chdir("C:\\Users\Bit\git\crawler")
    print(os.getcwd())

#os.mkdir("C:\\Users\Bit\git\crawler\\txtfile")

    os.chdir("C:\\Users\Bit\git\crawler\\txtfile")

    print(os.getcwd())
    file_no = result.get('fur_no')
    #file_name = result.get('fur_name')
    file_type = '.txt'

    content = result.get('fur_est_contents')

    #print(content)

    f = open(file_no+file_type, mode='w', encoding='UTF-8', errors='strict', buffering=1)
    f.write(content)
    f.close()
    p = p+1      
    print('완료')

"""
connection = pymongo.MongoClient('192.168.1.28', 27017)
db = connection.gaduda
collection = db.crawling_Furniture_Estimation
collection.insert(result)
"""  

        
        