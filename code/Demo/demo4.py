# -*-  codeing = utf-8 -*-
# @Time : 2023/1/3 17:22
# @Author : LHJ青梦
# @File : demo4.py
# @Software: PyCharm
'''
for i in range(5):
    print(i)
'''
'''
for i in range(0, 10, 3):#从0开始到10，步进值增3
    print(i)
'''
'''
for i in range(-10, -100, -30):
    print(i)
'''
'''
name = "guangzhou"
for x in name:
    print(x, end="\t")
'''
'''
这个比较重要
a = ["aa", "bb", "cc", "dd"]
for i in range(len(a)):
    print(i, a[i])
'''
'''
i = 0
while i < 5:
    print("now is %d"%(i+1))
    print("i=%d"%i)
    i += 1
'''

#1-100求和
'''
i = 1
sum = 0
while i <= 100:
    i += 1 
    sum = sum + i
print(sum)
'''
'''
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum +counter
    counter += 1
print("和为%d"%sum)
'''
'''
count = 0
while count < 5:
    print(count, "小于5")
    count +=1
else:
    print(count,"大于或等于5")
'''
'''
i = 0
while i < 10:
    i = i+1
    print("-"*30)
    if i==5:
        break#结束整个循环
        #continue  结束本次循环
    print(i)
'''
#九九乘法表
#    方法一

'''
print('打印乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (j, i, i * j), end='\t')
    print('')

#方法二
print('打印乘法表')
i = 1
while i <= 9:
    j = 1
    while (j <= i):
        print(f'{i}*{j}={i * j}', end='\t')
        j += 1
    print('')
    i += 1


#方法三
print("打印九九乘法表：")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()
'''





