# _*_ encoding:utf-8 _*_
# 1. 定义一个类
# class Person:
#     pass
#
# # 2. 根据类， 创建一个对象
# p1 = Person()
# p2 = Person()
#
# p1.age = 18
# p2.address = "上海"
#
# print(p1.address)

# 3. 给p对象， 增加一些属性
# p.age = 18
# p.height = 180
# p.age = 123
# # 4. 验证是否有添加成功
# print(p.age)
# # print(p.__dict__)

# print(p.sex)

# p.pets = ["小花", "小黑"]
# print(p.pets, id(p.pets))
#
# p.pets.append("小黄")
#
# print(p.pets, id(p.pets))

# num = 10
# del num
# print(num)
# p.age = 18
# del p.age
# print(p.age)


# ----------------------------类属性的操作--------------------------------------


# class Money:
#     pass

# one = Money()
# one.age = 10
# one.age = 18


# Money.count = 1
# Money.age = 18
# Money.num = 666

# print(Money.count)
# print(Money.__dict__)
#
# class Test:
#     sex = "男"

# class Money:
#     age = 18
#     count = 1
#     num = 666
#
# one = Money()

# del Money.age
# del one.age
# print(Money.age)
# print(one.age)
# print(Money.age)
# print(Money.age)
# one.age = 19
# print(one.__dict__)
# print(Money.age)

# one.xxx = 999
# print(one.xxx)

# Money.age = 22
# print(Money.age)

# print(Money.age)
# print(Money.count)
# print(Money.num)
# print(Money.__dict__)



# one = Money()
# one.sex = "女"
#
# one.__class__ = Test
# print(one.__class__)
#
#
# # print(one.age)
# print(one.sex)
# # print(one.count)
# # print(one.num)

#
# class Money:
#     age = 18
#     name = "sz"

# Money.__dict__ = {"sex": "男"}
# Money.__dict__["age"] = 20
# print(Money.age)
# print(Money.__dict__)

# one = Money()
# two = Money()
#
# print(one.age)
# print(two.age)
#
# Money.age = 20
#
# print(one.age)
# print(two.age)

# #
# # one.age = 19
# # print(one.__dict__)
#
# one.__dict__ = {"name": "Sz", "age": 18}
#
# one.__dict__["age"] = 999
# print(one.age)

# class Person:
#     age = 10
#     pass
#
# # Person.age = 19
# # Person.age = 11
# # del Person.age
# # Person.age
#
#
#
#
# p = Person()
#
# p.age += 5
# # p.age = p.age + 5
# # p.age = 15
#
# # 这行代码会不会报错？
#
# # 如果不会报错
# print(Person.age)
# print(p.age)
#
# # p.age = 11
# # p.age = 18
# # del p.age
# # p.age


class Person:
    # @classmethod
    def test():
        print("xxx")
    __slots__ = ["age"]
    pass

p1 = Person()
p1.age = 1
# p1.num = 2

print(p1.age)
# print(p1.num)
p2 = Person()
p2.age = 9
# p2.b = 6

Person.test()
# t = Person.test
# t(123)
