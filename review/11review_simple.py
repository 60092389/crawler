'''
Created on 2017. 8. 9.

@author: Bit
'''

import pymongo
import re
from konlpy.tag import Twitter
import cx_Oracle # @UnresolvedImport

#Oracle 연동
ora_dsn = cx_Oracle.makedsn('192.168.1.20', 1521, 'orcl')
ora_conn = cx_Oracle.connect('ora_user', '1234', ora_dsn)
ora_cursor = ora_conn.cursor()


#mongoDB 연동
mongo_conn = pymongo.MongoClient('192.168.1.28', 27017)
mongo_db = mongo_conn.gaduda
collection = mongo_db.rep_test

def review_summarize():
    
    results = collection.find({"fur_no" : 1})
    
    all_review_contents = ''
    
    for result in results:
        all_review_contents = all_review_contents + '\n' + result.get('contents')
    
    return all_review_contents

def keword_extractor(tagger, text):
    tokens = tagger.phrases(text)
    tokens = [ token for token in tokens if len(token) > 1]
    count_dict = [(token, text.count(token)) for token in tokens]
    ranked_words = sorted(count_dict, key = lambda x:x[1], reverse = True)[:50]
    
    return [keyword for keyword, freq in ranked_words]

if __name__ == '__main__':
    
    text = review_summarize()
    print(text)

    
    twit = Twitter()
    print(keword_extractor(twit, text))
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
            
    
    print(all_est_text)
    all_est_text_arr = re.split('/', all_est_text)
    mySet = set(all_est_text_arr)
    changed_list = list(mySet)    
    changed_list.remove('')

    print(all_est_text_arr)
    print(changed_list)






















