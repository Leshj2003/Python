## Python数据类型（三）列表s[m:n]的取值

**5.5** **列表****s[m:n]****的取值**

Python的列表s[m:n]取值方式是从左往右

m是列表元素的索引值，从0开始

n是列表元素索引值减1

m始终比n小

注意：m、n既可以是正数，零，也可以是负数。

 

简便记忆法：

从列表s的第m个元素开始，取出来n-m个元素。

 

**试验1**

有一个列表s=['a','b','c','d','e','f']

尝试着心算以下的值是多少，然后和Python运行的进行比较

s[0]

s[-2]

s[5]

s[0:5]

s[1:5]

s[-5:-1]

图解如下：

![img](https://img-blog.csdnimg.cn/20200131100346216.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l0eV83,size_16,color_FFFFFF,t_70)

 

如果m缺失，变成s[:n]，表示从最左边的元素开始，一直取到索引值为n-1的元素

如果n缺失，变成s[m:]，表示从索引值为m的元素开始，一直取到最右边的元素

如果m和n都缺失，变成s[:]，表示取列表的所有元素

 

**试验2**

有一个列表s=['a','b','c','d','e','f']

尝试着心算以下的值是多少，然后和Python运行的结果进行比较

s[2:]

s[:2]

s[-2:]

s[:-2]

s[:]

图解如下：

![img](D:\Desktop\python\images\watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3l0eV83,size_16,color_FFFFFF,t_70)