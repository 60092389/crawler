'''
Created on 2017. 7. 20.

@author: Bit
'''

import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import mongoConnect

conn = mongoConnect.collection


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
    for i in range(3,5):
        total_links.append(closet_links[i])
    for i in range(9,12):
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
    
    #print(num_split)
    
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
    #URL = post_link
    #res = urllib.request.urlopen(URL)
    #html  = res.read()
    
    driver.get(post_link)
    
    
    html = driver.page_source
    
    soup = BeautifulSoup(html, 'html.parser')
    
    detail_div = soup.find('div', class_='detail_wrap')
    
    
    craw_fur_name =''
    craw_fur_item_no = ''
    craw_fur_brand = ''
    craw_fur_price = ''
    craw_fur_room_kind_name = ''
    craw_fur_kind_name = ''
    craw_fur_brand_site = post_link
    craw_fur_img = ''
    craw_fur_size = []
    craw_fur_concept_name = ''
    
    
    #가구 이름
    detail_tit = detail_div.find('div', class_='detail_tit')
    
    fur_title = detail_tit.find('h2').text
    fur_title = re.sub('\[\w*\]', '', fur_title, 1)
    fur_title = re.sub('★\w*★', '' ,fur_title)
    fur_title = re.sub('★\w* \w*★', '' ,fur_title)
    fur_title = re.sub('^ *', '', fur_title)
    
    craw_fur_name = fur_title
        
    
    #가구 브랜드
    try:
        brand_tit = detail_tit.find('a', class_='select').text
        craw_fur_brand = brand_tit
        #print(brand_tit)
    except:
        brand_table = detail_div.find('table', class_='detail_info_base')
        brand_table_td = brand_table.find('td').text
        craw_fur_brand = brand_table_td
        #print(brand_table_td)
    
    #가구 가격
    try:
        price_div = detail_div.find('div', class_='detatil_opt_info_left')
        price_div_ul = price_div.find_all('ul', class_='opt_list')
        price_ul = price_div_ul[0]
        price_li = price_ul.find('li')
        price = price_li.find('div').text
        
        price_num_list = re.findall('\d+', price)
        
        for num in price_num_list:
            craw_fur_price = craw_fur_price + num
        
        #print(craw_fur_price)
    except:
        craw_fur_price = ''
        
    
    #가구 이미지
    thum_div = detail_div.find('div',class_='detatil_opt_thum')
    craw_fur_img = thum_div.find('img')['src']
    
    #방 종류
    location_div = soup.find('div', class_='location')
    location_ul = location_div.find('ul')
    location_li = location_ul.find_all('li')
    room = location_li[1].find('a').text
    
    if re.search('디자인', room):
        craw_fur_room_kind_name = '홈오피스'
    elif re.search('침대', room):
        craw_fur_room_kind_name = '침실'
    elif re.search('옷장', room):
        craw_fur_room_kind_name = '침실'
    elif re.search('거실|소파', room):
        craw_fur_room_kind_name = '거실'
    elif re.search('책상', room):
        craw_fur_room_kind_name = '홈오피스'
    
    #print(room)
    
    #가구 종류
    fur_kind = location_li[19].find('a').text
    
    if re.search('침실|침대', fur_kind):
        if re.search('침대|bed|베드', craw_fur_name):
            craw_fur_kind_name = '침대'
        if re.search('커튼', craw_fur_name):
            craw_fur_kind_name = ''
    elif re.search('화장대|스툴|거울', fur_kind):       
        if re.search('의자|스툴', craw_fur_name):
            craw_fur_kind_name = '의자'
        elif re.search('화장|콘솔', craw_fur_name):
            craw_fur_kind_name = '화장대'
        elif re.search('서랍', craw_fur_name):
            craw_fur_kind_name = '서랍'    
        elif re.search('선반', craw_fur_name):
            craw_fur_kind_name = '장식장'
    elif re.search('서랍장', fur_kind) and re.search('옷장', fur_kind) and re.search('협탁', fur_kind):
        if re.search('테이블|협탁', craw_fur_name):
            craw_fur_kind_name = '테이블'
        elif re.search('옷장|드레스', craw_fur_name):
            craw_fur_kind_name = '옷장'
        elif re.search('수납', craw_fur_name):
            craw_fur_kind_name = '수납장'
        elif re.search('서랍', craw_fur_name):
            craw_fur_kind_name = '서랍'
    elif re.search('옷장|', fur_kind):
        craw_fur_kind_name = '옷장'
    elif re.search('서랍장', fur_kind):
        craw_fur_kind_name = '서랍'
    elif re.search('수납장|원목가구', fur_kind):
        craw_fur_kind_name = '수납장'
    elif re.search('소파', fur_kind):
        craw_fur_kind_name = '소파'
        if re.search('스툴|스톨|암체어', craw_fur_name):
            craw_fur_kind_name = '의자'
        elif re.search('헤드', craw_fur_name):
            craw_fur_kind_name = ''
    elif re.search('거실장', fur_kind):
        craw_fur_kind_name = '장식장'
    elif re.search('거실테이블', fur_kind):
        craw_fur_kind_name = '테이블'
    elif re.search('사이드|무빙테이블', fur_kind):
        craw_fur_kind_name = '테이블'
    elif re.search('책장', fur_kind):
        if re.search('책장', craw_fur_name):
            craw_fur_kind_name = '책장'
        elif re.search('선반장', craw_fur_name):
            craw_fur_kind_name = '장식장'
        else:
            craw_fur_kind_name = ''
    elif re.search('책상', fur_kind):
        if re.search('보드|매트|패드|뚜껑|박스', craw_fur_name):
            craw_fur_kind_name = ''
        elif re.search('책상|데스크|desk|Desk', craw_fur_name):
            craw_fur_kind_name = '책상'
        elif re.search('테이블', craw_fur_name):
            craw_fur_kind_name = '테이블'
    elif re.search('의자', craw_fur_name):
        if re.search('받침', craw_fur_name):
            craw_fur_kind_name = ''
        else:
            craw_fur_kind_name = '의자'
    elif re.search('선반', fur_kind) and re.search('수납', fur_kind):
        if re.search('서랍', craw_fur_name):
            craw_fur_kind_name = '서랍'
        elif re.search('수납', craw_fur_name):
            craw_fur_kind_name = '수납장'
        elif re.search('선반', craw_fur_name):
            craw_fur_kind_name = '장식장'
        else:
            craw_fur_kind_name = ''      
    else:
        craw_fur_kind_name = ''
        
    
    
    
    detail_info_table_list = detail_div.find_all('table', class_='detail_info_base')
    #print(detail_info_table_list)
    detail_info_table = detail_info_table_list[1]
        
    
    #사이즈
    try:
        detail_info_tr = detail_info_table.find_all('tr')
        size_info_tr = detail_info_tr[1]
        size_info_td = size_info_tr.find_all('td')
        size_info = size_info_td[0].text
        #print(size_info)
        
        if re.search('상세', size_info):
            craw_fur_size = ''
        
        size =''
        if re.search('cm|CM|Cm|\.', size_info):
            size_info = re.sub('\d,\d', '', size_info)
            if re.search('l', size_info):
                size_split = re.split('l', size_info)
                size = size_split[0]
            elif re.search('ㅣ', size_info):
                size_split = re.split('ㅣ', size_info)
                size = size_split[0]
                if re.search(',', size):
                    size_split = re.split(',', size)
                    size = size_split[0]
            elif re.search(',', size_info):
                size_split = re.split(',', size_info)
                size = size_split[0]    
            elif re.search('\|', size_info):
                size_split = re.split('\|', size_info)
                size = size_split[0]
            elif re.search('/', size_info):
                size_split = re.split('/', size_info)
                size = size_split[0]
            else:
                size = size_info
        
            size = re.sub('\.\d', '' , size)
            size = re.sub('\~\d+', '' ,size)
            size = re.sub('\/\d+', '', size)
    
            size_num = re.findall('\d+', size)
            if size_num == []:
                size = size_split[1]
                size = re.sub('\.\d', '' , size)
                size = re.sub('\~\d+', '' ,size)
                size = re.sub('\/\d+', '', size)
    
            size_num = re.findall('\d+', size)
            for i in range(0,len(size_num)):
                size_num[i] = size_num[i]+'0'
    
            if len(size_num) >=3:
                for i in range(0,3):
                    craw_fur_size.append(size_num[i])
            elif len(size_num) <3:
                for i in range(0,len(size_num)):
                    craw_fur_size.append(size_num[i])
    
         
        elif re.search('mm|MM', size_info):
            
            size_info = re.sub('\d,\d', '', size_info)
            if re.search('l', size_info):
                size_split = re.split('l', size_info)
                size = size_split[0]              
            elif re.search('ㅣ', size_info):        
                size_split = re.split('ㅣ', size_info)
                size = size_split[0]
                if re.search(',', size):
                    size_split = re.split(',', size)
                    size = size_split[0]
            elif re.search(',', size_info):
                size_split = re.split(',', size_info)
                size = size_split[0]    
            elif re.search('\|', size_info):
                size_split = re.split('\|', size_info)
                size = size_split[0]
            elif re.search('/', size_info):
                size_split = re.split('/', size_info)
                size = size_split[0]
            else:
                size = size_info
        
            size = re.sub('\.\d', '' , size)
            size = re.sub('\~\d+', '' ,size)
            size = re.sub('\/\d+', '', size)
    
            size_num = re.findall('\d+', size)
            
            if size_num == []:
                size = size_split[1]
                size = re.sub('\.\d', '' , size)
                size = re.sub('\~\d+', '' ,size)
                size = re.sub('\/\d+', '', size)

    
            if len(size_num) >=3:
                for i in range(0,3):
                    craw_fur_size.append(size_num[i])
            elif len(size_num) <3:
                for i in range(0,len(size_num)):
                    craw_fur_size.append(size_num[i])
                    
    
        elif re.search('상세', size_info):
            craw_fur_size = ''
        else:
            size_info = re.sub('\d,\d', '', size_info)
            size = size_info
            size_num = re.findall('\d+', size)
            
            
            
            if len(size_num) >=3:
                for i in range(0,3):
                    if re.search('침대', craw_fur_name) and len(size_num[1])==3:
                        craw_fur_size.append(size_num[i]+'0')
                    else:
                        craw_fur_size.append(size_num[i])          
            elif len(size_num) <3:
                for i in range(0,len(size_num)):
                    if re.search('침대', craw_fur_name) and len(size_num[1])==3:
                        craw_fur_size.append(size_num[i]+'0')
                    else:
                        craw_fur_size.append(size_num[i])  

        
        #print(craw_fur_size)
        
    except: 
        craw_fur_size = ''
    
    
    
    #컨셉
    color_info_tr = detail_info_tr[0]
    color_info_td = color_info_tr.find_all('td')
    color_info = color_info_td[0].text
    #print(color_info)
    
    if re.search('동양|일본|한국|중국|전통', color_info):
        craw_fur_concept_name = '동양적'
    elif re.search('시골|러스틱|거친', color_info):
        craw_fur_concept_name = '시골풍'
    elif re.search('메이플|내추럴|내츄럴|월넛|괴목', color_info):
        craw_fur_concept_name = '내추럴'
    elif re.search('레트로|빈티지|앤틱|엔틱|브라운', color_info):
        craw_fur_concept_name = '앤틱'
    elif re.search('코튼|블루|그레이|민트|오렌지|레드|그린|인디고|핑크|유럽|아메', color_info):
        craw_fur_concept_name = '북유럽'
    elif re.search('화이트|블랙|모던', color_info):
        craw_fur_concept_name = '모던'
    else:
        craw_fur_concept_name = '모던'
        if re.search('가구야|폴앤코코', craw_fur_brand):
            craw_fur_concept_name = '내추럴'
        elif re.search('파로마|에인하우스|채우리', craw_fur_brand):
            craw_fur_concept_name = '모던'
        elif re.search('룸앤홈|웨스트프롬', craw_fur_brand):
            craw_fur_concept_name = '북유럽'
        elif re.search('유캐슬|바네스데코', craw_fur_brand):
            craw_fur_concept_name = '앤틱'
    
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

#b= 'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=319577&categoryPagelist=1'

"""
links = ['http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=290349&categoryPagelist=4',
         'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=198145&categoryPagelist=2',
         'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=249788&categoryPagelist=3',
         'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=378928&categoryPagelist=2',
         'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=213665&categoryPagelist=2',
         'http://mall.hanssem.com/goods/goodsDetailMall.do?gdsNo=244750'
         ]
"""

fur_room_kind_link = fetch_room_kind_link()
#link = fetch_fur_link('http://mall.hanssem.com/category/goHsmMctgy.do?ctgrNo=6998&categoryall=M6998')
#print(link)

count = 0;

for fur_kind_link in fur_room_kind_link:
    fur_link = fetch_fur_link(fur_kind_link)
    for post_link in fur_link:
        try:
            contents = fetch_post_contents(post_link)
            if re.search('소파|침대|책상|옷장|받침대|수납장|장식장|테이블|책장|의자|서랍|화장대', contents.get('craw_fur_kind_name')):
                conn.insert(contents)
                print(contents)
                count = count+1
                print(count)
        except:
            print('컨텐츠 에러')
            continue
        
print(count)

"""
for link in links:
    a = fetch_post_contents(link)
    print(a)
"""





    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    