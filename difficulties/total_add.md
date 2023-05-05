## 面向对象

```python
# 工资结算系统
# 导入抽象类模块
from abc import ABCMeta,abstracmethod

## 员工抽象类
class Employee(metaclass = ABCMeta):
    def __init__(self,name):
        self.name = name
        
    @abstracmethod
    def get_salary(self):
        pass
    
## 部门经理
class Manager(Employee):
    def get_salary(self):
        return 15000.0
    
# 程序员
class Programmer(Employee):
    def __init__(self,name,working_hour = 0):
        self.working_hour = working_hour
        super().__init__(name)
        
    def get_salary(self):
        return 200.0 * self.working_hour
    
# 销售员   
class Salesman(Employee):
    def __init__(self,name,sales = 0.0):
        self.sales = sales
        super().__init__(name)
        
        
    def get_salary(self):
        return 1800.0 + self.sales * 0.05
    
    
# 员工工厂
class EmployeeFactory:
    @staticmethod
    def create(emp_type,*args,**kwargs):
        all_emp_types = {'M':Manager,'P':Programmer,'S':Salesman}
        # 获取对应的员工类，cls是一个类
        cls = all_emp_types[emp_type.upper()]
        return cls(*args,**kwargs) if cls else None

    
# 主函数
def main():
    emps = [
        EmployeeFactory.create('M','曹操')，
        EmployeeFactory.create('P','荀彧',120),
        EmployeeFactory.create('P','郭嘉',85),
        EmployeeFactory.create('S','典韦',123000),
    ]
    for emp in emps:
        print(f'{emp.name}:{emp.get_salary():.2f}元')
        
        
if __name__ == '__main__':
    main()
```

* 类与类之间的关系
  * is-a关系：继承
  * has-a关系：关联 / 聚合 / 合成
  * use-a关系：依赖..
* 对象的复制（深拷贝和浅拷贝）
* 垃圾回收、循环引用和弱引用
  * 对象被创建，例如：a = 23
  * 对象被引用，例如：b = a
  * 对象被作为参数