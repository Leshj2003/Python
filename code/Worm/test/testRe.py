# -*-  codeing = utf-8 -*-
# @Time : 2023/1/26 18:43
# @Author : LHJ青梦
# @File : testRe.py
# @Software: PyCharm

#正则表达式：字符串模式（判断字符串是否符合一定的标准）

import re
#创建模式对象

pat = re.compile("AA")      #此处的AA是正则表达式，用来验证其他的字符串

# m = pat.search("CBA")      #search字符串被校验的内容


# m = pat.search("ABCAA")
# 左闭右开，三到五
# 而且只能找到第一个


# m = pat.search("AABBCCAA")

#
# m = re.search("asd", "Aasd")
# print(m)
#
# print(re.findall("a", "ASdzadAzza"))        #前面字符串是规则，后面的是被校验的字符串


# print(re.findall("[A-Z]", "ASdzadAzza"))

# print(re.findall("[A-Z]+", "ASdzadAzzaHJL"))


#sub

print(re.sub("a", "A", "abcdcasd"))     #找到a用A替换，但第三个字符串中查找

#建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"AABD\'"
print(a)








