'''
Created on 2017. 8. 1.

@author: Bit
'''

#-*-coding:utf-8-*-

import cx_Oracle  # @UnresolvedImport
import os
import re


#text1 = re.sub("\x", "\%", text)

#print(text1)

dsn = cx_Oracle.makedsn('192.168.1.20', 1521, 'orcl')
conn = cx_Oracle.connect('ora_user', '1234', dsn)

cursor = conn.cursor()
"""
query = 'select fur_name from furniture where fur_no = '
fur_no = '3'




cursor.execute(query+fur_no)   
fur_name = ''
for result in cursor:
    fur_name = result[0]
    """
    
    
real_fur_no = 0
def getFurInfo():
    cursor.execute('select fur_no, fur_url from furniture')

    fur_no_arr = []
    fur_url_arr = []
    for kk in cursor:
        fur_no = kk[0]
        fur_url = kk[1]
        fur_url = re.sub('\n', '', fur_url)
        fur_no_arr.append(fur_no)
        fur_url_arr.append(fur_url)
    
    
    #print(fur_no_arr)
    #print(fur_url_arr)
    
    return{
            'fur_no_arr' : fur_no_arr,
            'fur_url_arr' : fur_url_arr
        }



result = getFurInfo()

print(result.get('fur_no_arr')[0])
print(result.get('fur_url_arr')[0])

a = result.get('fur_no_arr')
b = result.get('fur_url_arr')
for i in range(0,len(a)):
    real_fur_no = a[i]
    real_fur_url = b[i]
    
    print(real_fur_no)
    print(real_fur_url)


#insert
#statement = 'insert into furniture_simple_review(fur_simple_review_no, fur_no, fur_simple_review_content) values (seq_fur_simple_review.nextval,:2,:3)'

#cursor.execute(statement, (1, '만족합니다'))

#conn.commit()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    