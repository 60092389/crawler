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


#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=47096936&trTypeCd=20&trCtgrNo=585021&lCtgrNo=1001364&mCtgrNo=1002273'

def review_fetch():
    driver.refresh()
    driver.get(site)

    driver.switch_to_frame('ifrmReview')
    #text = driver.find_element_by_class_name('review_list').text
    
    
    contents = driver.find_elements_by_class_name('summ_conts')
    for j in range(0,len(contents)):
                print(contents[j].text)
                
                
review_fetch()