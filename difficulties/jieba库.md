## `jieba`库

`jieba` 是一款强大的中文分词库，它的主要功能是将一段中文文本切分成一个一个的词语，方便进行文本处理和分析。除了分词功能，`jieba` 还提供了一些其他的功能，下面列举一些常用的功能及示例：

* 分词：将一段中文文本切分成一个一个的词语。

```python
import jieba

text = "我喜欢吃火锅和小龙虾。"
seg_list = jieba.cut(text, cut_all=False)
print("/ ".join(seg_list))
```

输出结果：

```python

我/ 喜欢/ 吃/ 火锅/ 和/ 小龙虾/ 。 
```

* 关键词提取：从一段文本中提取出关键词。

```python
import jieba.analyse

text = "我喜欢吃火锅和小龙虾。"
keywords = jieba.analyse.extract_tags(text, topK=3)
print(keywords)
```

输出结果：

```python

['火锅', '小龙虾', '喜欢'] 
```

* 添加自定义词典：添加一些自定义词语到分词库中。

```python
import jieba

text = "学习Python是非常有用的。"
jieba.add_word("Python")
seg_list = jieba.cut(text, cut_all=False)
print("/ ".join(seg_list))
```

输出结果：

```python

学习/ Python/ 是/ 非常/ 有用/ 的/ 。 
```

* 并行分词：使用多进程加速分词。

```python
import jieba
import jieba.parallel

jieba.enable_parallel(4)  # 开启并行分词模式，参数为进程数
text = "我喜欢吃火锅和小龙虾。"
seg_list = jieba.cut(text, cut_all=False)
print("/ ".join(seg_list))
jieba.disable_parallel()  # 关闭并行分词模式
```

输出结果：

```python

我/ 喜欢/ 吃/ 火锅/ 和/ 小龙虾/ 。 
```

* 分词速度对比：

```python
import time
import jieba
import jieba_fast

text = "学习Python是非常有用的。"

# jieba 分词速度测试
start = time.time()
for i in range(10000):
    jieba.lcut(text)
end = time.time()
print("jieba 分词速度：", end - start)

# jieba_fast 分词速度测试
start = time.time()
for i in range(10000):
    jieba_fast.lcut(text)
end = time.time()
print("jieba_fast 分词速度：", end - start)
```

输出结果：

```python
jieba 分词速度： 9.286266803741455
jieba_fast 分词速度： 1.5943100452423096
```

### 扩展

| 功能               | 方法                                                         | 描述                                                         |
| ------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 分词               | `jieba.cut()`<br />`jieba.lcut()`<br />`jieba.cut_for_search()`<br />`jieba.tokenize()` | 对文本进行分词，将文本按照词语单位进行划分。`cut()`和`lcut()`的区别在于返回的结果格式不同，cut()返回一个生成器，`lcut()`返回一个列表。cut_for_search()主要用于对搜索引擎和文本挖掘这类需要对结果进行进一步处理的应用场景，返回一个在基于概率图模型的基础上，利用了HMM进行了搜索的生成器。tokenize()可以获取到分词的每个单词在文本中的位置以及类型。 |
| 关键词提取         | `jieba.analyse.extract_tags()`<br />`jieba.analyse.textrank()` | 提取文本中的关键词。extract_tags()适用于快速获取文本的关键词，提供了多种关键词提取的方法，如基于TF-IDF算法、基于`TextRank`算法等等。`textrank()`则是基于Graph-based ranking model的一种算法。 |
| 词性标注           | `jieba.posseg.cut()`<br />`jieba.posseg.lcut()`              | 对分词结果中的每个词语进行词性标注，返回的结果格式为词语和词性构成的二元组。`posseg.cut()`和`posseg.lcut()`同`cut()`和`lcut()`一样，返回的是生成器和列表。 |
| 建立词典           | `jieba.load_userdict()`                                      | 自定义词典，将需要添加的词语添加到词典中，提高分词效果。词典格式为每行一个词语，另外可以在每个词语后面加上词频。 |
| 载入停用词表       | `jieba.analyse.set_stop_words()`                             | 忽略在指定词库中的一些词语，提升分词的准确率。停用词表格式为每行一个停用词。 |
| 词频统计           | `jieba.analyse.extract_tags()`<br />`jieba.analyse.textrank()` | 统计文本中每个词语出现的频率。                               |
| 新词发现           | `jieba.add_word()`                                           | 查找文本中出现频率比较高但未出现在词典中的新词，并通过add_word()方法将这些新词加入到分词词典中去。 |
| 并行分词           | `jieba.enable_parallel()`<br />`jieba.disable_parallel()`    | 多线程并行分词，提高分词效率。启用并行分词有助于提升分词效率，但也会占用一定的系统资源。 |
| 繁体中文转简体中文 | `jieba.analyse.set_stop_words()`                             | 将繁体中文文本转换为简体中文文本。                           |
| `TextRank`自动摘要 | `jieba.analyse.textrank()`                                   | 根据文本内容自动生成文章摘要。根据提取出来的关键词和权重，对文本进行重要性排序，最终生成文章摘要。 |





---

## `open()`函数

open()是Python中用来打开文件的函数，主要有以下几个参数：

1. file：要打开的文件路径（文件名与文件路径组成），必须是一个字符串类型；

2. mode：打开文件的模式，包括只读模式（'r'）、只写模式（'w'）、追加模式（'a'）等，详见下方；

3. buffering：指定缓冲的大小，一般不用设置，默认为-1，即使用系统缓冲；

4. encoding：指定文件的编码方式，例如UTF-8、GBK等，一般不用设置，默认为None；

5. errors：指定编码错误的处理方式，例如忽略错误（'ignore'）等，一般不用设置，默认为None。

打开文件后，可以使用文件对象的相关方法进行读写操作。

示例：

```python
# 打开文件，读取内容
with open('file.txt', 'r') as f:
    content = f.read()

# 打开文件，写入内容
with open('file.txt', 'w') as f:
    f.write('Hello, World!')
```

其中，'with open() as'语句为Python中的上下文管理器，可以在代码块结束后自动关闭打开的文件，以避免泄露资源或遗漏文件关闭操作。



---

## 字典的`get()`方法

在Python中，字典是一种无序且可变的数据类型，由一系列的键（key）和值（value）组成。字典的get()方法可以用来获取字典中指定键对应的值，其基本语法如下：

```python
value = dict.get(key, default=None)
```

其中，`dict`是要获取值的字典，`key`是要获取值的键，`default`是当字典中不存在这个键时，返回的默认值。如果`default`参数被忽略了，返回`None`。

示例：

```python
user_info = {'name': 'Jack', 'age': 28, 'gender': 'male'}

# 获取字典中指定键的值
name = user_info.get('name')
age = user_info.get('age')

# 当字典中不存在指定键时，返回默认值
email = user_info.get('email', 'No email address')
```

在上面的示例中，我们首先通过`get()`方法获取了字典`user_info`中的两个键的值。然后，我们给`get()`方法传了一个`default`参数，当字典中不存在`email`键时，`get()`方法返回`'No email address'`作为默认值。

需要注意的是，`dict[key]`与`dict.get(key)`这两种方式都可以用来获取字典中指定键的值，但是当字典中不存在指定键时，`dict[key]`会抛出`KeyError`的异常，而`dict.get(key)`则不会，它会返回`None`或默认值。因此，推荐使用`dict.get(key)`来获取字典中的值，特别是在不确定是否存在这个键时。