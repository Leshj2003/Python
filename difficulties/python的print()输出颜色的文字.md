## python的print()输出颜色的文字

在 Python 中，可以使用 ANSI 转义序列来在 print() 函数中输出带有颜色的文字。ANSI 转义序列是一系列字符，用于控制终端输出的格式和颜色。

下面是一个例子，演示如何使用 ANSI 转义序列在 print() 函数中输出红色文字：

```python
print('\033[91m' + 'Hello, world!' + '\033[0m')
```

在上面的代码中，'\033[91m' 表示设置输出颜色为红色，'\033[0m' 表示重置输出颜色为默认值。

如果希望输出不同颜色的文字，可以根据需要修改 ANSI 转义序列中的颜色代码。下面是一些常用的颜色代码：

- 红色：'\033[91m'
- 绿色：'\033[92m'
- 黄色：'\033[93m'
- 蓝色：'\033[94m'
- 紫色：'\033[95m'
- 青色：'\033[96m'

注意，在 Windows 系统下，ANSI 转义序列可能无法正常工作，需要使用第三方库来实现类似的功能。



### 第三方库

Python 中可以使用第三方库 colorama 来实现输出颜色的文字，它可以在 Windows、Linux 和 macOS 等平台上正常工作。

安装 colorama：

```python
pip install colorama
```

使用 colorama：

```python
from colorama import init, Fore, Back, Style

# 初始化 colorama
init()

# 输出红色文字
print(Fore.RED + 'Hello, world!' + Fore.RESET)

# 输出带有背景色的文字
print(Back.GREEN + 'Hello, world!' + Back.RESET)

# 输出加粗的文字
print(Style.BRIGHT + 'Hello, world!' + Style.RESET_ALL)
```

在上面的代码中，我们先使用 init() 函数初始化 colorama，然后使用 Fore、Back 和 Style 等类来设置输出的前景色、背景色和其他样式。

注意，在使用完 colorama 后，需要使用 Fore.RESET、Back.RESET 和 Style.RESET_ALL 等方法来将输出样式重置为默认值，否则后续的输出可能会继续受到影响。