'''
Created on 2017. 8. 3.

@author: Bit
'''

import os

a='정말 마음에 쏙 들어요!'

print(os.getcwd())

#os.chdir("C:\\Users\Bit\git\crawler")
print(os.getcwd())

#os.mkdir("C:\\Users\Bit\git\crawler\\txtfile")

os.chdir("C:\\Users\Bit\git\crawler\\txtfile")

print(os.getcwd())

f = open('이가구제품평.txt','w')
f.write(a)
f.close()