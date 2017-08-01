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


"""
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
"""

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


#o = '몸통 : 너비 59.8/79.8 x 깊이 39.6 x 높이 216cm l 인서트 화장거울 : 너비 57/77 x 깊이 10 x 높이 53cm(거울 : 너비 53/58 x 높이 39/52cm)'
#o = '옷장: 너비 80 x 깊이 60 x 높이 194cm ㅣ 드레스룸: 너비 40 x 깊이 40 x 높이 194cm'
#o = '너비 120~240 x 깊이 39.6 x 높이 216cm'
#o = '너비 178.5cm x 깊이 41.5cm x 높이118cm'
#o = '350(W)x295(D)x2050(H) ±30 /최소필요벽사이즈 550(W)*2100(H)'
#o = '침대: 침대프레임_너비 118.6 x 깊이 208.6 x 높이 75cm, 하부서랍_ 너비 99 x 깊이 51.5 x 높이 19.3cmㅣ 매트리스:사일런나잇 독립_너비 110 x 깊이 200 x 높이 22.5cm, 사일런나잇 라텍스탑_너비 110 x 깊이 200 x 높이 24cm, 컴포트아이 에코_너비 110 x 깊이 200 x 높이 22.5cm, 컴포트아이 라텍스탑_너비 110 x 깊이 200 x 높이 25cm'
#o = '몸통: 너비 79.8 x 깊이 39.6 x 높이 194cm(내부깊이 : 37.5cm),인서트 화장거울 : 너비 77 x 깊이 10 x 높이 53cm(거울 : 너비 58 x 높이 52cm)'
#o= '몸체 : 너비 73 x 깊이 75 x 높이 98cm, 발받침 : 46 x 40 x 48cm'
#o= 'W1440 x D770 x H770 mm (±2%)2%)'
o = '1,2번 - 콘솔:900*400*1240/ 스툴:300*300*358 3번 - 950*400*1380(mm) [±5%]'

size_info = o

#print(o2)
"""
if re.search('l', o2):
    a = re.split('l', o2)
    
    print(a)
elif re.search('', o2):
    #a = re.split('|', o2)
    print(o2)

if re.search('ㅣ', o):
    a = re.split('ㅣ', o)
    print(a)
" ㅍ_size = []
size =''
if re.search('cm|CM|Cm', size_info):
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
    
    for i in range(0,len(size_num)):
        size_num[i] = size_num[i]+'0'
    
    if len(size_num) >=3:
        for i in range(0,3):
            craw_fur_size.append(size_num[i])
    elif len(size_num) <3:
        for i in range(0,len(size_num)):
            craw_fur_size.append(size_num[i])
    
         
elif re.search('mm|MM|', size_info):
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
    
    if len(size_num) >=3:
        for i in range(0,3):
            craw_fur_size.append(size_num[i])
    elif len(size_num) <3:
        for i in range(0,len(size_num)):
            craw_fur_size.append(size_num[i])
       
elif re.search('상세', size_info):
    craw_fur_size = ''
else:
    size = size_info
    size_num = re.findall('\d+', size)
    
    if len(size_num) >=3:
        for i in range(0,3):
            craw_fur_size.append(size_num[i])
    elif len(size_num) <3:
        for i in range(0,len(size_num)):
            craw_fur_size.append(size_num[i])

        
print(craw_fur_size)
"""

k = '상품 상세설명 참조'
i = []
if re.search('상세', k):
    i = '후'
print(i)


w = '폴앤코'
if re.search('가구야|폴앤코코', w):
    print(w)




















