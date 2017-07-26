'''
Created on 2017. 7. 25.

@author: dslc
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from time import sleep
from collections import OrderedDict
import mongoConnect

conn = mongoConnect.collection

#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')


basic_url = 'http://www.ariafurniture.co.kr'

def fetch_fur_kind_link():
    
    real_URL = 'http://www.ariafurniture.co.kr/shop/list.php?ca_id=1090'
    res = urllib.request.urlopen(real_URL)
    html = res.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.find('div', class_='lnb')
    
    lnb_ul = div.find_all('ul')
    
    total_links = []
    
    bedroom_ul = lnb_ul[0]
    bedroom_li = []
    bedroom_li = bedroom_ul.find_all('li')
    bedroom_links = [ab.find('a')['href'] for ab in bedroom_li]
    for i in range(0,2):
        total_links.append(bedroom_links[i])
    for i in range(4,11):
        total_links.append(bedroom_links[i])
    for i in range(14,17):
        total_links.append(bedroom_links[i])
    total_links.append('http://www.ariafurniture.co.kr/shop/list.php?ca_id=10b0')
    

    sofa_ul = lnb_ul[3]
    sofa_li = []
    sofa_li = sofa_ul.find_all('li')
    sofa_links = [ab.find('a')['href'] for ab in sofa_li]
    for link in sofa_links:
        total_links.append(link)
    
    livingroom_ul = lnb_ul[4]
    livingroom_li = []
    livingroom_li = livingroom_ul.find_all('li')
    livingroom_links = [ab.find('a')['href'] for ab in livingroom_li]
    for link in livingroom_links:
        total_links.append(link)
    
    homeoffice_ul = lnb_ul[6]
    homeoffice_li = []
    homeoffice_li = homeoffice_ul.find_all('li')
    homeoffice_links = [ab.find('a')['href'] for ab in homeoffice_li]
    for link in homeoffice_links:
        total_links.append(link)
    
    
    
    return total_links

#a = fetch_fur_kind_link()
#print(a)


def fetch_post_link(link):
    #real_URL = link
    #res = urllib.request.urlopen(real_URL)
    #html = res.read()
    
    driver.get(link)
    
    driver.implicitly_wait(3)
    #sleep(2)
    
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    div = soup.find('div', id='sct')
    item_ul = div.find('ul', class_='sct sct_10')
    item_li = item_ul.find_all('li')
    
    links = []
    links = [ab.find('a')['href'] for ab in item_li]
    
    return links

def fetch_contents_link(contents_link):
    driver.get(contents_link)
    
    driver.implicitly_wait(3)
    
    #sleep(2)
    
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='sub_con view_p')
    
    basic_info_div = div.find('div', id='sit')
    
    craw_fur_name =''
    craw_fur_item_no = ''
    craw_fur_brand = ''
    craw_fur_price = ''
    craw_fur_room_kind_name = ''
    craw_fur_kind_name = ''
    craw_fur_brand_site = contents_link
    craw_fur_img = ''
    craw_fur_size = []
    craw_fur_concept_name = ''
    

    #가구 이름
    craw_fur_name = basic_info_div.find('h2', class_='item_name_title').text
    craw_fur_name = re.sub('\n ', '', craw_fur_name)
    craw_fur_name = re.sub('\t', '', craw_fur_name)
    craw_fur_name = re.sub('\n\t', '', craw_fur_name)
    craw_fur_name = re.sub('\n', '', craw_fur_name)
    craw_fur_name = re.sub(' \t\t\t', '', craw_fur_name)
    craw_fur_name = re.sub('\t\t\t', '', craw_fur_name)
    
    
    #가구 이미지
    img_div = basic_info_div.find('div', id='sit_pvi_big')
    img_link = img_div.find('img')['src']
    craw_fur_img = img_link
   
    
    #가구 브랜드
    craw_fur_brand = basic_info_div.find('h2', class_='brand_title').text
    craw_fur_brand = re.sub('\n\t\t\t\t', '', craw_fur_brand)
    craw_fur_brand = re.sub('\t\t\t', '', craw_fur_brand)
    
    
    
    
    basic_info_table = basic_info_div.find('table', class_='sit_ov_tbl')
    basic_info_tr = basic_info_table.find_all('tr')
    
    #제품 번호
    pro_num_td = basic_info_tr[3].find('td').text
    craw_fur_item_no = pro_num_td
    
    
    #가구 가격
    try:
        price_text = basic_info_table.find('input', id='it_price')['value']
        craw_fur_price = price_text
    except:
        craw_fur_price = ''
        pro_num_td = basic_info_tr[2].find('td').text
        craw_fur_item_no = pro_num_td
    
    
    #가구 방종류
    room_location = div.find('div', id='aria_location')
    room_location_a = room_location.find_all('a')
    room_type = room_location_a[1].text
    
    if re.search('Bedroom', room_type):
        craw_fur_room_kind_name = '침실'
    elif re.search('Sofa', room_type):
        craw_fur_room_kind_name = '거실'
    elif re.search('Living', room_type):
        craw_fur_room_kind_name = '거실'
    elif re.search('Office', room_type):
        craw_fur_room_kind_name = '홈오피스'
    elif re.search('Accessories', room_type):
        if re.search('Closet', craw_fur_name):
            craw_fur_room_kind_name = '침실'
        else:
            craw_fur_room_kind_name = '홈오피스'  
      
    #가구 종류
    fur_type = room_location_a[2].text
    if re.search('협탁|테이블|I-DESK', fur_type):
        craw_fur_kind_name = '테이블'
    elif re.search('침대', fur_type):
        craw_fur_kind_name = '침대'
    elif re.search('책상', fur_type):
        craw_fur_kind_name = '책상'
    elif re.search('옷장|장농|드레스', fur_type):
        craw_fur_kind_name = '옷장'
    elif re.search('받침', fur_type):
        craw_fur_kind_name = '받침대'
    elif re.search('수납', fur_type):
        craw_fur_kind_name = '수납장'
    elif re.search('거실|엔터테인|장식장|거울장', fur_type):
        craw_fur_kind_name = '장식장'
    elif re.search('소파', fur_type):
        craw_fur_kind_name = '소파'
    elif re.search('책장', fur_type):
        craw_fur_kind_name = '책장'
    elif re.search('벤치|체어|의자', fur_type):
        craw_fur_kind_name = '의자'
    elif re.search('서랍', fur_type):
        craw_fur_kind_name = '서랍'
    elif re.search('화장대', fur_type):
        craw_fur_kind_name = '화장대'
    elif re.search('홈오피스', fur_type):
        if re.search('Desk', craw_fur_name):
            craw_fur_kind_name = '책상'
        elif re.search('Bookcase', craw_fur_name):
            craw_fur_kind_name = '책장'
    elif re.search('시스템가구', fur_type):
        if re.search('Closet|Cabinet|Hanger', craw_fur_name):
            craw_fur_kind_name = '옷장'
        elif re.search('Desk', craw_fur_name):
            craw_fur_kind_name = '책상'
        elif re.search('Unit', craw_fur_name):
            craw_fur_kind_name = '장식장'
        elif re.search('Bookcase', craw_fur_name):
            craw_fur_kind_name = '책장'
        elif re.search('Table', craw_fur_name):
            craw_fur_kind_name = '테이블'

    
    #사이즈
    detail_div = div.find('div', id='detail_view')
    detail_table_list = detail_div.find_all('table')
    size_table_tr_list = detail_table_list[1].find_all('tr')
    size_table_td_list = size_table_tr_list[1].find_all('td')
    fur_size = size_table_td_list[1].text
    
    craw_fur_size = re.split('\(', fur_size)
    size_list = craw_fur_size[0]
    #re.sub('\xa0', '', craw_fur_size)
    size_num = re.findall('\d+', size_list)
    
    craw_fur_size=[]
    
    if len(size_num) >= 3:
        for i in range(0,3):
            craw_fur_size.append(size_num[i])
    elif len(size_num) == 2:
        for i in range(0,2):
            craw_fur_size.append(size_num[i])
    else:
        craw_fur_size = ''
    
    #print(craw_fur_size)
    
    #craw_fur_size.append(fur_size)
    
    #가구 컨셉
    if re.search('LEGACY|Studio RTA|SOFIA\+SAM|TURNKEY|TVILUM|WHITE FEATHERS|WILLOW by Interwood', craw_fur_brand):
        craw_fur_concept_name = '내추럴'
    elif re.search('EHF LEATHER|FINE HOME|GENCECIX|HOLLAND HOUSE|INNOVATION', craw_fur_brand):
        craw_fur_concept_name = '북유럽'
    elif re.search('INTERSTIL|LAFORMA|MUSE|POWELL|PROGRESSIVE|SPIZY DENMARK|SUNPAN|TRADE POINT|ARIA FURNITURE', craw_fur_brand):
        craw_fur_concept_name = '북유럽'
    elif re.search('MAGNUSSEN|A.R.T|COAST TO COAST|LEGENDS|LIFESTYLE|MARTIN|MY HOME FURNISHINGS', craw_fur_brand):
        craw_fur_concept_name = '앤틱'
    elif re.search('NEW CLASSIC|PULASKI|PARKVIEW|RACHLIN|STEIN WORLD|STYLECRAFT|SAMUEL LAWRENCE', craw_fur_brand):    
        craw_fur_concept_name = '앤틱'
    else:
        craw_fur_concept_name = '모던'
    

    return  {
        'craw_fur_name' : craw_fur_name,       
        'craw_fur_item_no' : craw_fur_item_no,
        'craw_fur_brand' : craw_fur_brand,
        'craw_fur_price' : craw_fur_price,
        'craw_fur_room_kind_name' : craw_fur_room_kind_name,
        'craw_fur_kind_name' : craw_fur_kind_name,
        'craw_fur_brand_site' : craw_fur_brand_site,
        'craw_fur_img' : craw_fur_img,
        'craw_fur_size' : craw_fur_size,
        'craw_fur_concpet_name' : craw_fur_concept_name
        }

#b = 'http://www.ariafurniture.co.kr/shop/item.php?it_id=1479195328&ca_id=1070'
#a =fetch_contents_link(b)
#print(a)

fur_links = fetch_fur_kind_link()
total_contents_count = 0

for link in fur_links:
    post_links = fetch_post_link(link)
    for contents_link in post_links:
        result = fetch_contents_link(contents_link)
        conn.insert(result)
        print(result)
        total_contents_count = total_contents_count+1
        print(total_contents_count)

print(total_contents_count)










