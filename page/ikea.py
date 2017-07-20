'''
Created on 2017. 7. 17.

@author: dslc
'''

import urllib.request
from bs4 import BeautifulSoup
import re
from pickle import NONE

###########거실##########
#소파
#target_url = 'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/'
#TV/멀티미디어가구
#target_url = 'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10475/'
#책장
#target_url = 'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10382/'
#선반유닛
#http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/11465/
#수납장, 장식장
#http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10410/
#거실장/찬장/콘솔테이블
#http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/30454/
#테이블
#http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10705/


###########홈오피스############
#책상
#target_url = 'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/20649/'
#사무용의자
#http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/20652/
#수납장
#http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/10385/
#서랍유닛
#http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/10711/

############침실###########
#침대
#target_url = 'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/16284/'
#싱글침대
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/16285/
#간이침대
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/19037/
#수납형침대
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/25205/
#2층침대
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/19039/
#서랍장
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/10451/
#침대협탁
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/20656-2/
#화장대
#http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/20657/


target_url = ['http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/39130/', 
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10475/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10382/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/11465/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10410/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/30454/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/living_room/10705/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/20649/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/20652/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/10385/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/10385/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/workspaces/10711/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/16284/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/16285/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/19037/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/25205/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/19039/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/10451/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/20656-2/',
              'http://www.ikea.com/kr/ko/catalog/categories/departments/bedroom/20657/'          
              ]

basic_url = 'http://www.ikea.com'


def fetch_post_list(URL):
   real_URL = URL
   res = urllib.request.urlopen(real_URL)
   html = res.read()
   
   soup = BeautifulSoup(html, 'html.parser')
   div = soup.find('div', class_='productLists')
   div_link_list = div.find_all('div', class_='threeColumn product ')
   
   links = []
   links = [basic_url + ab.find('a', class_='productLink')['href'] for ab in div_link_list]
   
   
   return links;



#result = fetch_post_list()
#print(result)


def fetch_post_contents(link):
    basic_url = 'http://www.ikea.com'
    URL = link
    res = urllib.request.urlopen(URL)
    html = res.read()
    soup = BeautifulSoup(html, 'html.parser')
    content_div = soup.find('div', id='main')
    
    #기본정보 div
    basic_info_div = content_div.find('div', id='pipContainer')
    
    #상세정보 div
    detail_info_div = soup.find('div', id='productInfo1')
    
    #제품이름
    craw_fur_name_basic = basic_info_div.find('div', id='name').text + '/' + basic_info_div.find('div', id='type').text
    craw_fur_name = re.sub('\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t','',craw_fur_name_basic)
    craw_fur_name = re.sub('\t\t\t\t\t\r\n\t\t\t\t\t\n\n','',craw_fur_name)
    craw_fur_name = re.sub('\r\n\t\t\t\t\t\r\n\t\t\t\t','',craw_fur_name)
    craw_fur_name = re.sub('\r\n\t\t\t\t\t\t', '', craw_fur_name)
    
    #제품번호
    craw_fur_item_no = basic_info_div.find('div', id='itemNumber').text
    
    #브랜드
    craw_fur_brand = 'IKEA'
   
    #\749,000에서 숫자만
    craw_fur_price_list = re.findall("\d+", basic_info_div.find('span', id='price1').text)
    craw_fur_price = ''
    for price in craw_fur_price_list:
        craw_fur_price = craw_fur_price + price 
    
    #방종류    
    room_kind = basic_info_div.find('ul', id='breadCrumbs')
    room_kind_basic = room_kind.find_all('li')
    craw_fur_room_kind_name = room_kind_basic[2].text
    craw_fur_room_kind_name = re.sub('\n', '', craw_fur_room_kind_name)
    craw_fur_room_kind_name = re.sub(' ', '', craw_fur_room_kind_name)
    
    #가구종류
    craw_fur_kind_name = basic_info_div.find('div', id='type').text
    if re.search('소파', craw_fur_kind_name):
        craw_fur_kind_name = '소파'
    elif re.search('침대', craw_fur_kind_name) or re.search('베드', craw_fur_kind_name):
        craw_fur_kind_name = '침대'
    elif re.search('책상', craw_fur_kind_name) or re.search('워크', craw_fur_kind_name):
        craw_fur_kind_name = '책상'
    elif re.search('옷장', craw_fur_kind_name) or re.search('리넨', craw_fur_kind_name):
        craw_fur_kind_name = '옷장'
    elif re.search('화장대', craw_fur_kind_name):
        craw_fur_kind_name = '화장대'
    elif re.search('스탠드', craw_fur_kind_name):
        craw_fur_kind_name = '받침대'
    elif re.search('수납', craw_fur_kind_name):
        craw_fur_kind_name = '수납장'
    elif re.search('장식장', craw_fur_kind_name):
        craw_fur_kind_name = '장식장'
    elif re.search('테이블', craw_fur_kind_name) or re.search('협탁', craw_fur_kind_name):
        craw_fur_kind_name = '테이블'
    elif re.search('책장', craw_fur_kind_name):
        craw_fur_kind_name = '책장'
    elif re.search('의자', craw_fur_kind_name):
        craw_fur_kind_name = '의자'
    elif re.search('서랍', craw_fur_kind_name):
        craw_fur_kind_name = '서랍'

    
    
    #해당가구 웹주소    
    craw_fur_brand_site = URL
    
    
    #가구 이미지
    craw_fur_img = basic_url + basic_info_div.find('img', id='productImg')['src']

    
    #가구 사이즈
    craw_fur_size = ''
    try:
        craw_fur_size = detail_info_div.find('div', id='metric').text
        craw_fur_size = re.sub('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t   \t    ','', craw_fur_size)
        craw_fur_size = re.sub("등쿠션포함", '높이', craw_fur_size)
        craw_fur_size = re.sub('[()H]', '', craw_fur_size)
        craw_fur_size = re.sub('\W깊이\W', '깊이', craw_fur_size)


              
        craw_fur_size = re.split('cm', craw_fur_size)
        
        try:
            for i in (0,1,2):
                #print(craw_fur_size[i])
                
            
                if re.search('폭', craw_fur_size[i]):
                    width = re.search('\d+', craw_fur_size[i]).group()+'0'
                    #print(width)
                elif re.search('깊이', craw_fur_size[i]) or re.search('길이', craw_fur_size[i]):
                    depth = re.search('\d+', craw_fur_size[i]).group()+'0'
                    #print(depth)
                elif re.search('높이', craw_fur_size[i]):
                    height = re.search('\d+', craw_fur_size[i]).group()+'0'
                    #print(height)
            
            craw_fur_size = [width,depth,height]
        except IndexError:
            craw_fur_size = ''
        except UnboundLocalError:
            craw_fur_size = ''
        
        
    except AttributeError:
        craw_fur_size = ''
    
        
    #가구 컨셉
    craw_fur_concept_name = ''
    add_info = detail_info_div.find('div', id='custBenefit').text
    #print(add_info)
    
    try:
    
        if re.search('한옥|일본|흙|민예|비백|고택|좌식|곡선|동양|오리엔탈|중국|한국|korea|chin|japan', add_info):
            craw_fur_concept_name = '동양적'
        elif re.search('거친|거칠|순박|벽돌|러스틱|rust|brick|구식|레트로|retro|복고|소박', add_info):
            craw_fur_concept_name = '시골풍'
        elif re.search('앤틱|엔틱|antic|고급|빈티지|골동|멋|은은|영국|미국|고귀|기품|고혹|아메리칸|american', add_info):
            craw_fur_concept_name = '앤틱'
        elif re.search('화사|패브릭|밝|간결|북유럽|기하학|원색|개성|스칸디나비아|scand|fabric', add_info):
            craw_fur_concept_name = '북유럽'
        elif re.search('결|자연|나무색|직물|투박|편안|내추럴|내츄럴|따뜻|천연|클래식|classic|natural'):
            craw_fur_concept_name = '내추럴'
        elif re.search('독창|크림|현대|심플|단순|세련|시크|도시|모노|깔끔|모던|트랜디|화이트|깨끗', add_info):
            craw_fur_concept_name = '모던'
        else:
            craw_fur_concept_name = '모던'
    except TypeError:
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
            
i = 0
for URL in target_url:
    links = fetch_post_list(URL)
    for link in links:
        result = fetch_post_contents(link)
        
        if re.search('소파|침대|책상|옷장|받침대|수납장|장식장|테이블|책장|의자|서랍|화장대', result.get('craw_fur_kind_name')):
            i=i+1
            print(result)
        

print(i)
"""
links = fetch_post_list()
for link in links:
    result = fetch_post_contents(link)
        
    print(result)
"""

























