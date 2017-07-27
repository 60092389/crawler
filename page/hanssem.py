'''
Created on 2017. 7. 20.

@author: Bit
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from _ast import Div


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
    
    total_links = []
    
    bedroom_li = dep1_list[0].find_all('li')
    bedroom_links = [ab.find('a')['href'] for ab in bedroom_li]
    for i in range(2,6):
        total_links.append(bedroom_links[i])
    for i in range(8,10):
        total_links.append(bedroom_links[i])
    
    closet_li = dep1_list[1].find_all('li')
    closet_links = [ab.find('a')['href'] for ab in closet_li]
    for i in range(3,13):
        total_links.append(closet_links[i])
        
    
    livingroom_li = dep1_list[2].find_all('li')
    livingroom_links = [ab.find('a')['href'] for ab in livingroom_li]
    for i in range(0,10):
        total_links.append(livingroom_links[i])
    
    homeoffice_li = dep1_list[3].find_all('li')
    homeoffice_links = [ab.find('a')['href'] for ab in homeoffice_li]
    for i in range(0,6):
        total_links.append(homeoffice_links[i])
    
    
    return total_links
#link = fetch_room_kind_link()

#print(link)


def fetch_fur_link(fur_kind_link):
    driver.get(fur_kind_link)
    
    page_num_html = driver.page_source
    
    page_num_soup = BeautifulSoup(page_num_html, 'html.parser')
    
    page_div = page_num_soup.find('div', class_='paging')
    page_list = page_div.find('span', class_='list').text
    
    num_split = re.findall('\d', page_list)
    
    print(num_split)
    
    #kk = soup.find('a', onclick='linkPage(2); return false;')
    num_arr_str = num_split
    result_links = []
    num_arr = []
    
    for num in num_arr_str:
        num_arr.append(int(num))
    

    for num in num_arr:
        if num%5!=1:
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
        result_links = result_links + links
        
    
 
    return result_links

#link = fetch_fur_link('http://mall.hanssem.com/category/goHsmMctgy.do?ctgrNo=6998&categoryall=M6998')
#print(link)



def fetch_post_contents(post_link):
    URL = post_link
    res = urllib.request.urlopen(URL)
    html  = res.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.find('div', class_='detail_wrap')
    dd=''
    return div

b= 'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=210017&categoryPagelist=1'

a = fetch_post_contents(b)
print(a)





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    