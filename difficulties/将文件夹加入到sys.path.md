## 将文件夹加入到sys.path

sys.path是一个包含了Python解释器将搜索模块的目录列表。当Python解释器在导入模块时，它会按照sys.path列表中的顺序搜索模块。sys.path通常包含了当前目录，Python标准库的安装目录以及其他自定义目录。可以通过修改sys.path来添加或删除搜索路径。

---



要将文件夹添加到sys.path，可以使用以下方法： 

1. 使用sys.path.append()方法添加文件夹路径： 

```python 
import sys 
sys.path.append('/path/to/folder')
```

2. 使用PYTHONPATH环境变量添加文件夹路径： 在终端中执行以下命令（Windows系统）：

    ```bash
    set PYTHONPATH=%PYTHONPATH%;/path/to/folder
    ```

    或者在终端中执行以下命令（Linux/Mac系统）： 

   ```bash 
   export PYTHONPATH=$PYTHONPATH:/path/to/folder
   ```

    注意，在这两种方法中，`/path/to/folder`应该替换为你要添加的文件夹的实际路径。