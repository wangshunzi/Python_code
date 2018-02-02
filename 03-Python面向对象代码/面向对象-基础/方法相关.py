



def eat():
    print(1)
    print(2)
    print(3)

# eat()



class Person:
    def eat2():
        print("这是一个实例方法")

    @classmethod
    def leifangfa(cls):
        print("这是一个类方法", cls)

    @staticmethod
    def jingtaifangfa():
        print("这是一个静态方法")


p = Person()
# print(p)
# p.eat2()
# Person.eat2()

# Person.leifangfa()

# Person.jingtaifangfa()
# print(p.__dict__)
#
# print(Person.__dict__)
# def run():
#     print("run")
#
#
# p.age = run
# print(p.__dict__)
# p.eat2()