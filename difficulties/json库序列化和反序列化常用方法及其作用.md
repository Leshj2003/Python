## json库序列化和反序列化常用方法及其作用

"json.dumps()"和"json.loads()"是序列化和反序列化的常用方法。下面是修正后的介绍及代码示例：

1. `json.dumps(obj)`：将Python对象序列化为JSON格式的字符串。

   - 作用：将Python中的字典、列表等对象序列化为符合JSON格式的字符串，方便进行数据传输或存储。

   - 示例：

     ```python
     import json
     
     data = {'name': 'John', 'age': 30, 'city': 'New York'}
     json_str = json.dumps(data)
     print(json_str)
     # 输出：{"name": "John", "age": 30, "city": "New York"}
     ```

     

2. `json.loads(json_str)`：将JSON格式的字符串反序列化为Python对象。

   - 作用：将JSON格式的字符串解析为Python中的字典、列表等对象。

   - 示例：

     ```python
     import json
     
     json_str = '{"name": "John", "age": 30, "city": "New York"}'
     data = json.loads(json_str)
     print(data['name'])
     # 输出：John
     ```

     

3. `json.dump(obj, file)`：将Python对象序列化为JSON格式并写入文件对象。

   - 作用：将Python中的字典、列表等对象序列化为JSON格式，并写入到文件中。

   - 示例：

     ```python
     import json
     
     data = {'name': 'John', 'age': 30, 'city': 'New York'}
     with open('data.json', 'w') as file:
         json.dump(data, file)
     ```

     

4. `json.load(file)`：从文件对象中读取JSON格式数据并反序列化为Python对象。

   - 作用：从文件中读取JSON格式的数据，并将其反序列化为Python中的字典、列表等对象。

   - 示例：

     ```python
     import json
     
     with open('data.json', 'r') as file:
         data = json.load(file)
     print(data['name'])
     # 输出：John
     ```

     

这些方法提供了方便且灵活的序列化和反序列化JSON数据的方式，无论是将Python对象序列化为JSON格式，还是将JSON格式反序列化为Python对象，都可以借助这些方法进行处理。

---

### dumps()和dump()的区别

1. `dumps()`方法：

   - `dumps()`方法将Python对象序列化为JSON格式的字符串。

   - 序列化后的数据以字符串的形式保存在内存中，可以通过变量进行访问和处理。

   - 最常见的用途是将Python对象转换为可传输或存储的JSON字符串，例如通过网络传输或在文件中保存。

   - 示例：

     ```python
     import json
     
     data = {'name': 'John', 'age': 30, 'city': 'New York'}
     json_str = json.dumps(data)
     print(json_str)
     ```

     

2. `dump()`方法：

   - `dump()`方法将Python对象序列化为JSON格式并写入文件对象。

   - 序列化后的数据直接写入文件对象，无需将数据保存在内存中。

   - 可以将Python对象直接写入文件，适用于大型数据集或需要持久化存储的情况。

   - 示例：

     ```python
     import json
     
     data = {'name': 'John', 'age': 30, 'city': 'New York'}
     with open('data.json', 'w') as file:
         json.dump(data, file)
     ```

     

总结：

- 使用`dumps()`将数据序列化为字符串，适用于将数据传输或以字符串形式存储。
- 使用`dump()`将数据序列化为JSON并写入文件对象，适用于直接将数据写入文件或处理大型数据集。

---

### loads()和load()的区别

1. `loads()`方法：

   - `loads()`方法将JSON格式的字符串反序列化为Python对象。

   - 可以从内存中的字符串中解析JSON数据，并将其转换为对应的Python数据类型，如字典、列表等。

   - 最常见的用途是将从网络或其他数据源获取的JSON字符串转换为可操作的Python对象。

   - 示例：

     ```python
     import json
     
     json_str = '{"name": "John", "age": 30, "city": "New York"}'
     data = json.loads(json_str)
     print(data['name'])
     ```

     

2. `load()`方法：

   - `load()`方法从文件对象中读取JSON格式数据并反序列化为Python对象。

   - 可以从文件中加载JSON数据，并将其解析为对应的Python数据类型。

   - 适用于从文件中读取JSON数据进行处理，特别适合处理大型数据集。

   - 示例：

     ```python
     import json
     
     with open('data.json', 'r') as file:
         data = json.load(file)
     print(data['name'])
     ```

     

总结：

- 使用`loads()`可以将JSON字符串反序列化为Python对象，适用于处理内存中的JSON数据。
- 使用`load()`可以从文件中读取JSON数据并反序列化为Python对象，适用于处理存储在文件中的JSON数据。