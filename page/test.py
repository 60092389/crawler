'''
Created on 2017. 7. 20.

@author: Bit
'''

import urllib.request
import re
from pip.utils.ui import DownloadProgressSpinner

ok = ['1','2','3']
ok2 = ['4','5','6']

print(ok+ok2)

test1 = ['1','2','3','4']
test2 = []

print(test1.__len__())



index = 0
for i in test1:
    test2.append(int(i))

print(test2)

sss = ["javascript:location.href='/category/category.casa?ctgy_code=20021'",
       "javascript:location.href='/category/category.casa?ctgy_code=20021'",
       "javascript:location.href='/category/category.casa?ctgy_code=20039'"
       ]


#c= re.compile("/category/category.casa?ctgy_code=*")
c= re.compile(r"'.*?href='(.*)'")
for ss in sss:
    print(ss)
    ok = c.search(ss)
    print(ok)



















