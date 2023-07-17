## python列表（list）中的del，remove，和pop的区别

* 先谈pop和remove



```undefined
a = [1,2,3,4]
```

![\color{red}{pop}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bpop%7D)

> pop 接受的是元素的下标，在原列表中弹出这个元素，并返回
>  也就是说:
>
> > ```undefined
> > test_one = a.pop(1)
> > ```
> >
> > #### 结果为：
> >
> > 
> >
> > ```undefined
> > test_one = 2
> > a = [1,3,4]
> > ```

![\color{red}{remove}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bremove%7D)

> remove接受的是列表中的数，在原列表从左到右删除第一次出现的这个数，返回值为None
>  也就是说:
>
> > ```csharp
> > a=[1,2,1,3]
> > test_one = a.remove(1)
> > ```
> >
> > #### 结果为：
> >
> > 
> >
> > ```python
> > test_one = None
> > a = [2,1,3]
> > ```

![\color{red}{del}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bdel%7D)

> > ```python
> > a=[1,2,1,3]
> > del a[1]
> > ```
> >
> > #### 结果为：
> >
> > 
> >
> > ```undefined
> > a = [1,1,3]                                                                 
> > ```

- del 是一个**语句**，它直接销毁a[1]这个对象
- del可以作用在任何对象上，不单单是列表里的某一个元素，比如del a,那么a这个列表就没有了
- del 的速度更快，**原因如下**

> ###### 在使用del时：python的内部调用是**直接调用字节码**，因为它是一个**语句**，
>
> ![img](https:////upload-images.jianshu.io/upload_images/7230999-7c52fdd11a925e71.png?imageMogr2/auto-orient/strip|imageView2/2/w/420/format/webp)
>
> del字节码.png

> 而使用remove，或者pop时，调用的是**函数**
>
> ![img](https:////upload-images.jianshu.io/upload_images/7230999-63831987be4f6c80.png?imageMogr2/auto-orient/strip|imageView2/2/w/398/format/webp)
>
> remove字节码.png

调用字节码的时间肯定比调用函数的快

* 总结：![\color{red}{remove}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bremove%7D)和![\color{red}{pop}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bpop%7D) 视情况使用，![\color{red}{del}](https://math.jianshu.com/math?formula=%5Ccolor%7Bred%7D%7Bdel%7D)操作要比前两个快