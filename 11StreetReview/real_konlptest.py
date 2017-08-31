'''
Created on 2017. 8. 8.

@author: Bit
'''


import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from time import sleep
import pymongo
from selenium.common.exceptions import NoSuchElementException
import os
import cx_Oracle  # @UnresolvedImport
from konlpy.tag import Twitter

#몽고디비 접속
conn = pymongo.MongoClient('192.168.1.28', 27017)
db = conn.gaduda
collection = db.rep_test

#오라클 접속
ora_dsn = cx_Oracle.makedsn('192.168.1.20', 1521, 'orcl')
ora_conn = cx_Oracle.connect('ora_user', '1234', ora_dsn)
ora_cursor = ora_conn.cursor()

#driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver')
driver = webdriver.PhantomJS(executable_path=r'C:\phantomjs-2.1.1-windows\bin\phantomjs')

#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1322253347&trTypeCd=20&trCtgrNo=585021&lCtgrNo=1001364&mCtgrNo=1002273'
#site= 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=96531135&trTypeCd=20&trCtgrNo=1002273'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1183869688&trTypeCd=21&trCtgrNo=1009053'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1367968916&trTypeCd=20&trCtgrNo=1002276'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1335741053&trTypeCd=21&trCtgrNo=1002276'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1319927303&trTypeCd=20&trCtgrNo=1002276'

"""
site_arr = ['http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1319927303&trTypeCd=20&trCtgrNo=1002276',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=247446895&trTypeCd=20&trCtgrNo=1002278',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=59339435&trTypeCd=20&trCtgrNo=1002278',
            'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=121939108&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=80528149&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=711796698&trTypeCd=20&trCtgrNo=1002280',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=54588902&trTypeCd=20&trCtgrNo=1002279',
            'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=700206758&trTypeCd=21&trCtgrNo=1002279',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1319927303&trTypeCd=20&trCtgrNo=1002276',
            'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=34417429&trTypeCd=21&trCtgrNo=1002207'
            ]
"""

#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=34417429&trTypeCd=21&trCtgrNo=1002207'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1524266195&trTypeCd=20&trCtgrNo=1002208'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=33157060&trTypeCd=21&trCtgrNo=1002208'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1190396400&trTypeCd=20&trCtgrNo=1002208'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=316632855&trTypeCd=20&trCtgrNo=1002206'
#site = 'http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1217769555&trTypeCd=21&trCtgrNo=1002206'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=79272748&trTypeCd=20&trCtgrNo=1002206'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=43095680&trTypeCd=20&trCtgrNo=1002209'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=1150272583&trTypeCd=21&trCtgrNo=1002209'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=10627073&trTypeCd=21&trCtgrNo=1002215'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=168660845&trTypeCd=20&trCtgrNo=1002209'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=166459065&trTypeCd=21&trCtgrNo=1002214'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=727410637&trTypeCd=20&trCtgrNo=1002214'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=526535472&trTypeCd=21&trCtgrNo=1002214'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=443023762&trTypeCd=20&trCtgrNo=1002213'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=31738170&trTypeCd=21&trCtgrNo=1002213'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=45764635&trTypeCd=20&trCtgrNo=1002213'
#site = 'http://www.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=240435243&trTypeCd=20&trCtgrNo=1002215'

#fur_no = 1

def getFurInfo():
    ora_cursor.execute('select fur_no, fur_url from furniture where fur_no = 181 order by fur_no asc')
    fur_no_arr = []
    fur_url_arr = []
    for ora_cursor_value in ora_cursor:
        fur_no = ora_cursor_value[0]
        fur_url = ora_cursor_value[1]
        fur_url = re.sub('\n', '', fur_url)
        fur_no_arr.append(fur_no)
        fur_url_arr.append(fur_url)

    
    return{
            'fur_no_arr' : fur_no_arr,
            'fur_url_arr' : fur_url_arr
        }


def review_fetch(site):
    #driver.refresh()
    driver.get(site)
    driver.implicitly_wait(1)
    try:
        driver.switch_to_frame('ifrmReview')
        driver.implicitly_wait(1)
        text = driver.find_element_by_class_name('review_list').text
    except:
        try:
            driver.switch_to_frame('ifrmReview')
            driver.implicitly_wait(1)
            text = driver.find_element_by_class_name('review_list').text
        except:
            driver.switch_to_frame('ifrmReview')
            driver.implicitly_wait(1)
            text = driver.find_element_by_class_name('review_list').text
    

    #contents = driver.find_elements_by_class_name('summ_conts')
    
    all_review_contents = ''
    all_pages_nums_text = []
    page_nums_arr = []
    click_count = 1
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
            click_count = click_count + 1
            print("click_count : " ,click_count)
            if click_count == 7:
                break
            print('페이지수 세는 다음페이지 클릭')
        except:
            print('익셉트문')
            break  
        
    #print('와일문나옴')
    #print(all_pages_nums_text)
    #print(len(all_pages_nums_text))

    #print('드라이버부르기 전')
    #driver.refresh()
    driver.get(site)
    #print('드라이버 바로 부름')
    driver.implicitly_wait(2)
    #print('드라이버 부름 2')
    sleep(1)
    #print('드라이버 부름 3')
    driver.switch_to_frame('ifrmReview')
    #page_num_div = driver.find_element_by_class_name('s_paging_v2')
    #test = page_num_div.find_element_by_partial_link_text('3')
    #print('아아아')
    #print(test.text)
    

    
    
    for i in all_pages_nums_text:
        driver.implicitly_wait(2)
        #print(i)
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
            #print('리뷰욥 : ',all_review_contents)
            #collection.insert({'fur_no':fur_no, 'fur_name':'에스엔가구 모던 3단 협탁', 'contents':contents[j].text })
            
        if int(i)%10 == 0:
            try:
                next_click = driver.find_element_by_class_name('next')
                next_click.click()
                driver.implicitly_wait(3)
                sleep(1)
                print('리뷰 모으는 다음페이지 클릭')
            except:
                print('다음페이지 없음')
                break
        #if all_pages_nums_text == '60':
        #    break
            
            #all_reivew_contents = all_reivew_contents +'\n' + contents.text
            #print(contents.text)
            
    #print(all_review_contents)
  
    return {
        'fur_est_contents' : all_review_contents
        }



def keword_extractor(tagger, text):
    tokens = tagger.phrases(text)

    tokens = [ token for token in tokens if len(token) > 1]

    count_dict = [(token, text.count(token)) for token in tokens]

    ranked_words = sorted(count_dict, key = lambda x:x[1], reverse = True)[:50]

    
    return [keyword for keyword, freq in ranked_words]

if __name__ == '__main__':
    
    furInfo_result = getFurInfo()
    
    furInfo_arr_size = len(furInfo_result.get('fur_no_arr'))
    fur_no_arr = furInfo_result.get('fur_no_arr')
    fur_url_arr = furInfo_result.get('fur_url_arr')
    
    failed_fur_no = []
        
    for i in range(0,furInfo_arr_size):
        content = ''
        try:
            fur_no = fur_no_arr[i]
            site = fur_url_arr[i]
            
            print(fur_no)
            print(site)
            
            result = review_fetch(site)



            content = result.get('fur_est_contents')
            #print('컨텐츠 : ' ,content)

                
            text = content
    
            twit = Twitter()
            #print(keword_extractor(twit, text))
            review_text_arr = keword_extractor(twit, text)
            all_est_text = ''
            for review_text in review_text_arr:
                if re.search("깔끔", review_text):
                    all_est_text = all_est_text + '/' + '깔끔합니다'
            
                if re.search("만족|마음", review_text):
                    all_est_text = all_est_text + '/' + '만족합니다'
            
                if re.search("가격대|저렴", review_text):
                    all_est_text = all_est_text + '/' + '가성비 좋네요'
    
                if re.search("이쁘|이쁨", review_text):
                    all_est_text = all_est_text + '/' + '이뻐요'
            
                if re.search('디자인', review_text):
                    all_est_text = all_est_text + '/' + '디자인이 마음에 들어요'

                if re.search('강추|최고', review_text):
                    all_est_text = all_est_text + '/' + '강추합니다'
            
                if re.search('고급', review_text):
                    all_est_text = all_est_text + '/' + '고급집니다'
            
                if re.search('쿠션감', review_text):
                    all_est_text = all_est_text + '/' + '쿠션감이 좋아요'
            
                if re.search('냄새', review_text):
                    all_est_text = all_est_text + '/' + '약간의 냄새가 나요'
            
                if re.search('색상|색깔', review_text):
                    all_est_text = all_est_text + '/' + '색상이 이뻐요'
        
                if re.search('분위기', review_text):
                    all_est_text = all_est_text + '/' + '분위기 있어요'
            
                if re.search('아이|아기', review_text):
                    all_est_text = all_est_text + '/' + '아이방에 두기 좋아요'
            
                if re.search('기능', review_text):
                    all_est_text = all_est_text + '/' + '기능이 좋아요'
            
                if re.search('편안', review_text):
                    all_est_text = all_est_text + '/' + '편안해요'
            
                if re.search('고급', review_text):
                    all_est_text = all_est_text + '/' + '고급져요'
            
                if re.search('소리|소음|삐그덕', review_text):
                    all_est_text = all_est_text + '/' + '약간의 소리가 나요'
        
            
            all_est_text_arr = re.split('/', all_est_text)
            mySet = set(all_est_text_arr)
            changed_list = list(mySet)    
            changed_list.remove('')

            print(all_est_text_arr)
            print(changed_list)
    
            for i in range(0, len(changed_list)):
                #statement = 'insert into furniture_simple_review(fur_simple_review_no, fur_no, fur_simple_review_content) values (seq_fur_simple_review.nextval,:2,:3)'
            
                statement = 'insert into furniture_simple_review(fur_simple_review_no, fur_no, fur_simple_review_content) values (seq_fur_simple_review.nextval,:2,:3)'
	        
                ora_cursor.execute(statement, (fur_no, changed_list[i]))

            ora_conn.commit()
            print(fur_no)
            print('commit')

        except:
            failed_fur_no.append(fur_no)
            print('커밋 실패 : ' ,failed_fur_no)
    
    
    