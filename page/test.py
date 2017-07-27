'''
Created on 2017. 7. 20.

@author: Bit
'''

import urllib.request
import re
from pip.utils.ui import DownloadProgressSpinner
from collections import OrderedDict

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
    
    
    
ddd = ['1','2','3','4','5','6','7','21','31','40','41','42','41','42','41','42']
ddd_int = []

for i in ddd:
    ddd_int.append(int(i))

mySet = set(ddd_int)
changed_list = list(mySet)



print(sorted(changed_list))



craw_fur_size = []
size_split = ['103','200','400']


if len(size_split)>=3:
    for i in (0,1,2):
        craw_fur_size.append(size_split[i])
elif len(size_split)==2:
    for i in(0,1):
        craw_fur_size.append(size_split[i])
else:
    craw_fur_size = ''

print(craw_fur_size)


#p = '★포토후기이벤트★ 가구야 772 큰서랍형 슈퍼싱글침대 (매트리스 택1)'
#p = '★SALE★콤비 전신거울 화장대 의자 14종'
#p = '★BEST모음전★ [FM디자인] 홈데코 코마 서랍 3종1택'
p = '[최저가보장] ★세트구매시방수커버증정 컬러★ [okok] 원목침대 SS/Q 12종모음 (포토후기 공기청정기증정)'
#p = '한샘 아임 침대 SS 서랍형 (컬러 2종/택1, 매트별도)'

p = re.sub('\[\w*\]', '', p, 1)
p = re.sub('★\w*★', '' ,p)
p = re.sub('★\w* \w*★', '' ,p)
p = re.sub('^ *', '', p)
print(p)











