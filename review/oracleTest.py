'''
Created on 2017. 8. 1.

@author: Bit
'''

#-*-coding:utf-8-*-

import cx_Oracle  # @UnresolvedImport
import os
import re

text = '잉글랜더베니스가죽침대'.encode('euc-kr')

print(text)


#text1 = re.sub("\x", "\%", text)

#print(text1)

dsn = cx_Oracle.makedsn('192.168.1.20', 1521, 'orcl')
conn = cx_Oracle.connect('ora_user', '1234', dsn)

cursor = conn.cursor()

query = 'select fur_name from furniture where fur_no = '
fur_no = '3'


cursor.execute(query+fur_no)   
fur_name = ''
for result in cursor:
    fur_name = result[0]
    
cursor.execute('select * from furniture')
for kk in cursor:
    print(kk)
    