'''
Created on 2017. 7. 20.

@author: Bit
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

room_kind_link = []

home_url = 'http://mall.hanssem.com/main.do'
basic_url = 'http://mall.hanssem.com'

def fetch_room_kind_link():
    driver.get(home_url)
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    all_category = soup.find('div', class_='all_category')
    dep1_list = all_category.find_all('div', class_='dep1')
    
    lnb_list_links = [ab.find('a', class_='lnb_list')['href'] for ab in dep1_list]
    lnb_list_links = [lnb_list_links[0],lnb_list_links[1],lnb_list_links[2],lnb_list_links[3]]
    
    return lnb_list_links
#link = fetch_room_kind_link()

#print(link)


def fetch_fur_kind_link(fur_room_kind_link):
    driver.get(fur_room_kind_link)
    html = driver.page_source
       
    soup = BeautifulSoup(html, 'html.parser')
    contents_left = soup.find('div', class_='contents_left')
    contents_left_lnb = contents_left.find('div', class_='lnb')
    fur_kind_ul = contents_left_lnb.find('ul')
    link_list = fur_kind_ul.find_all('li', class_='dep1 bdt')
    
    links =[]
    links = [basic_url+ab.find('a')['href'] for ab in link_list]
    
    return links

#link1 = fetch_fur_kind_link('http://mall.hanssem.com/category/LCtgr3811.html?ctgrNo=3811&categoryall=L3811')
#print(link1)



def fetch_fur_link(fur_kind_link):
    driver.get(fur_kind_link)
    
    #kk = soup.find('a', onclick='linkPage(2); return false;')
    num_arr = ['1','2','3','4','5']
    result_links = []

    for num in num_arr:
        if num!='1':
            kk=driver.find_element_by_link_text(num)
            driver.implicitly_wait(10)
            kk.click()
    
        html = driver.page_source
    
        soup = BeautifulSoup(html, 'html.parser')
   
    
        #item_contents = soup.find('div', id_='tab_body_list')
        ul_list = soup.find('ul', id='mctgyList')
        product_list = ul_list.find_all('p', class_='prd_img label_link')
        links = []
    
        links = [basic_url+ab.find('a')['href'] for ab in product_list]
        result_links = links + result_links
        
    
 
    driver.close()
    return result_links.__len__()

link = fetch_fur_link('http://mall.hanssem.com/category/goHsmMctgy.do?ctgrNo=7412')
print(link)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    