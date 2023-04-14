# -*-  codeing = utf-8 -*-
# @Time : 2023/4/11 9:44
# @Author : LHJ青梦
# @File : demo03.py
# @Software: PyCharm


import jieba
f = open("沉默的羔羊.txt", 'r', encoding='utf-8')
ls = jieba.lcut(f.read())

#ls = f.read().split()
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1
'''
# print(type(ls))
print(ls)
print('-----------------')
# print(type(d))
print(d)
print('--------------------')
'''
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc and len(k) > 2:
        maxc = d[k]
        maxw = k
    if d[k] == maxc and len(k) > 2 and k > maxw:
        maxw = k
print(maxw)
f.close()

'''
这段代码是一个简单的文本分析程序，目的是找到一个文本中出现次数最多的词语。

具体的解释如下：

导入了 jieba 模块，用于对文本进行分词。
打开一个名为 "沉默的羔羊.txt" 的文件。
通过 jieba.lcut() 函数对文件内容进行分词，得到一个分词列表 ls。
创建一个空字典 d，用于存储每个词语出现的次数。
遍历分词列表 ls，对于每个词语 w，如果 w 已经在字典 d 中，就将其出现次数加一，否则将其添加到字典 d 中，并将其出现次数初始化为 1。
创建两个变量 maxc 和 maxw，用于记录出现次数最多的词语和该词语的出现次数。
再次遍历字典 d，对于每个词语 k，如果 k 的出现次数大于 maxc 且 k 的长度大于 2，就将 maxc 和 maxw 更新为当前的值。如果 k 的出现次数等于 maxc 且 k 的长度大于 2 且 k 的字典序比 maxw 大，就将 maxw 更新为当前的值。
输出出现次数最多的词语 maxw。
关闭文件。
'''