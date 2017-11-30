
class Person:
    # def run(self):
    #     print(self)
    @classmethod
    def leifangfa(cls, a):
        print("这是一个类方法", cls, a)


Person.leifangfa(123)

p = Person()
p.leifangfa(666)


func = Person.leifangfa
func(111)

# 装饰器的作用: 在保证原本函数不改变的前提下, 直接给这个函数增加一些功能
class A(Person):
    pass
A.leifangfa(0)