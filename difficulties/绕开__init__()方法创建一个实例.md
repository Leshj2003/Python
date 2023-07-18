## 绕开`__init__()`方法创建一个实例

在Python中，可以通过使用类的`__new__()`方法绕过`__init__()`方法来创建类的实例。`__new__()`方法在对象实例化之前被调用，负责创建并返回类的实例。 下面是一个示例，展示如何绕过`__init__()`方法来创建类的实例： 

```python
class MyClass:    
	def __init__(self, value):       						print("Initializing...")        
		self.value = value     
	def __new__(cls, *args, **kwargs):       				print("Creating instance without calling 					__init__ method...")        
		return object.__new__(cls) 
# 创建类的实例，绕过__init__()方法 
instance = MyClass.__new__(MyClass) 				print(instance.value)  
# AttributeError: 'MyClass' object has no attribute 'value'  
```



在上面的示例中，`__new__()`方法被调用时，它返回了一个类的实例，但没有调用`__init__()`方法来初始化实例的属性。因此，在访问`instance.value`时会引发AttributeError异常，因为`value`属性没有被初始化。 需要注意的是，绕过`__init__()`方法来创建类的实例可能导致实例的属性没有被正确初始化，可能会导致程序出现错误或异常。因此，绕过`__init__()`方法应该谨慎使用，确保实例的属性被正确初始化。