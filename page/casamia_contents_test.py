'''
Created on 2017. 7. 24.

@author: dslc
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
from time import sleep
from collections import OrderedDict

#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')


basic_url = 'http://www.casamiashop.com'
link = 'http://www.casamiashop.com/goods/detail.casa?pkg_code=0017899'
#link = 'http://www.casamiashop.com/goods/detail.casa?pkg_code=0016282'

def ferch_post_contents(link):
    #URL = link
    #res = urllib.request.urlopen(URL)
    #html = res.read()
    driver.refresh()
    driver.get(link)
    html = driver.page_source
    
    driver.implicitly_wait(3)
    
    soup = BeautifulSoup(html, 'html.parser')
    basic_info_div = soup.find('div', class_='goods_info_box')
    #print(basic_info_div)
    
    detail_info_table = soup.find('table', class_='write_form')
    #print(detail_info_table)
    
    table_tr = detail_info_table.find_all('tr')
    #print(table_tr)   
    name_tr = table_tr[0]
    name_td = name_tr.find_all('td')
    color_tr = table_tr[1] 
    color_td = color_tr.find_all('td')
    size_tr = table_tr[3]
    size_td = size_tr.find_all('td')
    
    
    
    craw_fur_name =''
    craw_fur_item_no = ''
    craw_fur_brand = ''
    craw_fur_price = ''
    craw_fur_room_kind_name = ''
    craw_fur_kind_name = ''
    craw_fur_brand_site = ''
    craw_fur_img = ''
    craw_fur_size = []
    craw_fur_concept_name = ''
    
    #제품명
    #craw_fur_name = basic_info_div.find('li', class_='goods_subject').text
    #craw_fur_name = re.sub('\r\n\t\t\t\t\t\t\r\n\t\t\t\t \t\t\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t', '', craw_fur_name)
    #craw_fur_name = re.sub('\r\n\t\t\t\t\t\t\n', '', craw_fur_name)
    #craw_fur_name = re.sub('\t\n\n\n', '', craw_fur_name)
    craw_fur_name = name_td[1].text
    
    
    #가격
    temp_craw_fur_price = basic_info_div.find('li', class_='goods_amount').text
    if re.search(']', temp_craw_fur_price):
        craw_fur_price = re.split('] ', temp_craw_fur_price)
        temp_craw_fur_price = re.findall("\d+", craw_fur_price[1])
    else:
        temp_craw_fur_price = re.findall("\d+", temp_craw_fur_price)
    
    craw_fur_price = ''
    for price in temp_craw_fur_price:
        craw_fur_price = craw_fur_price + price
        
    #이미지
    craw_fur_img_div = soup.find('ul', class_='thumb_slider')
    craw_fur_img = craw_fur_img_div.find('img')['src']

    
    #방종류
    kind_name_div = soup.find('div', class_='navi')
    room_kind_basic = kind_name_div.find_all('a')
    if re.search('침실', room_kind_basic[1].text):
        craw_fur_room_kind_name = '침실'
    elif re.search('거실', room_kind_basic[1].text):
        craw_fur_room_kind_name = '거실'
    elif re.search('홈오피스', room_kind_basic[1].text):
        craw_fur_room_kind_name = '홈오피스'
        
        
    #가구종류
    fur_kind_basic = kind_name_div.find_all('a')
    if re.search('서랍장', fur_kind_basic[2].text):
        craw_fur_kind_name = '서랍'
        if re.search('테이블', craw_fur_name):
            craw_fur_kind_name = '테이블'
    elif re.search('침대', fur_kind_basic[2].text):
        craw_fur_kind_name = '침대'
    elif re.search('장롱', fur_kind_basic[2].text):
        craw_fur_kind_name = '옷장'
    elif re.search('스툴', fur_kind_basic[2].text) and re.search('화장대', craw_fur_name):
        craw_fur_kind_name = '화장대'
    elif re.search('스툴', fur_kind_basic[2].text) and re.search('콘솔', craw_fur_name):
        craw_fur_kind_name = '장식장'
    elif re.search('스툴', fur_kind_basic[2].text):
        craw_fur_kind_name = '의자'
    elif re.search('소파', fur_kind_basic[2].text):
        craw_fur_kind_name = '소파'
    elif re.search('거실장', fur_kind_basic[2].text):
        craw_fur_kind_name = '장식장'
    elif re.search('테이블', fur_kind_basic[2].text):
        craw_fur_kind_name = '테이블'
    elif re.search('책상', fur_kind_basic[2].text):
        craw_fur_kind_name = '책상'
    elif re.search('책장', fur_kind_basic[2].text):
        craw_fur_kind_name = '책장'
    elif re.search('의자', fur_kind_basic[2].text):
        craw_fur_kind_name = '의자'
    elif re.search('수납', fur_kind_basic[2].text):
        craw_fur_kind_name = '수납장'
    elif re.search('선반', fur_kind_basic[2].text):
        if re.search('체어', craw_fur_name):
            craw_fur_kind_name = '의자'
        elif re.search('선반', craw_fur_name):
            craw_fur_kind_name = '장식장'
        elif re.search('수납', craw_fur_name):
            craw_fur_kind_name = '수납장'
            
        
    #브랜드 사이트
    craw_fur_brand_site = link
    
    #브랜드이름
    craw_fur_brand = '까사미아OEM'
    
    #가구 사이즈
    size = size_td[1].text
    
    size_list = []
    if re.search('/', size):
        size_list = re.split('/', size)
        size = size_list[0]
    elif re.search('.', size):
        size_list = re.split(',', size)
        size = size_list[0]
    elif re.search('\+', size):
        size_list =re.split('\+', size)
        size = size_list[0]
    
    try:
        if re.search('\d', size):
            size_split = re.findall('\d+', size)
            #print(size)
            #print(size_split)
        else:
            craw_fur_size='사이트참고'
    
        for i in (0,1,2):
            craw_fur_size.append(size_split[i])
    except:
        craw_fur_size = ''
        
    
        
        
    #가구 컨셉
    concept_color = color_td[1].text
    
    if re.search('전통|동양|중국|일본|한국|아시아', concept_color):
        craw_fur_concept_name = '동양적'
    elif re.search('순박|벽돌|복고|레트로|소박', concept_color):
        craw_fur_concept_name = '시골풍'
    elif re.search('워시|러스틱|브라운|카멜|월넛|금장', concept_color):
        craw_fur_concept_name = '앤틱'
    elif re.search('내츄럴|원목|내추럴|브라우니|자연', concept_color):
        craw_fur_concept_name = '내추럴'
    elif re.search('그레이|베이지|민트|블루|크림|멜란지브라운|딥블루|그린|스칸디', concept_color):
        craw_fur_concept_name = '북유럽'
    elif re.search('오크|화이트|아이보리|블랙', concept_color):
        craw_fur_concept_name = '모던'
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
    
ok = ferch_post_contents(link)
print(ok) 




















































