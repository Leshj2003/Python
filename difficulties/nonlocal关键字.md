## nonlocal关键字

nonlocal是Python中的一个关键字，用于在函数内部声明一个变量为函数外部的变量。当在函数内部需要访问函数外部的变量时，如果该变量不是全局变量，而是在外部函数中定义的局部变量，则需要在内部函数中使用nonlocal关键字来声明该变量。

例如：

```python
def outer():
    x = 0
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()

outer()  # 输出1
```

在上面的例子中，inner函数访问了outer函数中定义的变量x，并使用nonlocal关键字声明了x是外部函数的局部变量。这样，在inner函数中对x的修改会影响到outer函数中的x变量。