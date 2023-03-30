# -*-  codeing = utf-8 -*-
# @Time : 2023/1/13 21:31
# @Author : LHJ青梦
# @File : testUrllib.py
# @Software: PyCharm

import urllib.request
#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))      #read()查看内容--网页源码，decode()默认编码解析形式


#获取一个post请求
'''
import urllib.parse     #解析器
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")        #data封装的信息,字节封装进去
response = urllib.request.urlopen("http://httpbin.org/post",data=data)      #模拟真实网页访问，常用登录
print(response.read().decode("utf-8"))
'''

#更健壮,超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)     #timeout响应时间
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://www.baidu.com")
# #status状态码，200正常访问 getheaders()请求响应头
# print(response.status)
# print(response.getheader("Server"))        #参数是是拿到具体的值,getheader


# url = "https://www.douban.com"
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# #把请求网址封装
# headers = {
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
# }
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))



url = "https://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
}
req = urllib.request.Request(url=url, headers=headers )
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))















