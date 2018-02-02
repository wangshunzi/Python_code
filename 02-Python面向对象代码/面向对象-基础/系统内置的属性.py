
class Person:
    """
    这是一个人, 类
    """
    age = 19
    def __init__(self):
        self.name = "sz"

    def run(self):
        print("run")


# __dict__ : 类的属性
# __bases__ : 类的所有父类构成元组
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块


print(Person.__dict__)
print(Person.__bases__)
print(Person.__doc__)
# help(Person)
print(Person.__name__)
print(Person.__module__)

p = Person()
print(p.__class__)


