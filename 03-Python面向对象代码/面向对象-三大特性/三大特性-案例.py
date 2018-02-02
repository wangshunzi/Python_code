# 定义三个类, 小狗, 小猫, 人
# 小狗: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 看家(格式: 名字是xx, 年龄xx岁的小狗在xx)
# 小猫: 姓名, 年龄(默认1岁);        吃饭, 玩, 睡觉, 捉老鼠(格式: 名字是xx, 年龄xx岁的小猫在xx)
# 人:   姓名, 年龄(默认1岁), 宠物;  吃饭, 玩, 睡觉(格式: 名字是xx, 年龄xx岁的人在xx)
#                           养宠物(让所有的宠物吃饭, 玩, 睡觉),
#                           让宠物工作(让所有的宠物根据自己的职责开始工作)

class Animal:
    def __init__(self, name, age=1):
        self.name = name
        self.age = age

    def eat(self):
        print("%s在吃饭" % self)

    def play(self):
        print("%s在玩" % self)

    def sleep(self):
        print("%s在睡觉" % self)

class Person(Animal):
    # 在创建一个小狗实例的时候, 给它设置几个属性
    def __init__(self, name, pets, age=1):
        super(Person, self).__init__(name, age)
        self.pets = pets

    def yang_pets(self):
        for pet in self.pets:
            pet.eat()
            pet.play()
            pet.sleep()

    def make_pets_work(self):
        for pet in self.pets:
            pet.work()
            # if isinstance(pet, Dog):
            #     pet.watch()
            # elif isinstance(pet, Cat):
            #     pet.catch()

    def __str__(self):
        return "名字是{}, 年龄{}岁的人".format(self.name, self.age)
# p = Person("sz", [1, 2], 18)
# print(p.__dict__)
class Cat(Animal):

    def work(self):
        print("%s在捉老鼠" % self)

    def __str__(self):
        return "名字是{}, 年龄{}岁的小猫".format(self.name, self.age)

class Dog(Animal):
    def work(self):
        print("%s在看家" % self)

    def __str__(self):
        return "名字是{}, 年龄{}岁的小狗".format(self.name, self.age)

d = Dog("小黑", 18)
c = Cat("小红", 2)
p = Person("sz", [d, c], 18)
p.yang_pets()
p.make_pets_work()
# -----------------------------------------代码3-------------------------------------------------
#
# class Person:
#     # 在创建一个小狗实例的时候, 给它设置几个属性
#
#     def __init__(self, name, pets, age=1):
#         self.name = name
#         self.age = age
#         self.pets = pets
#
#     def eat(self):
#         print("%s在吃饭" % self)
#
#     def play(self):
#         print("%s在玩" % self)
#
#     def sleep(self):
#         print("%s在睡觉" % self)
#
#     def yangPets(self):
#         for pet in self.pets:
#             pet.eat()
#             pet.play()
#             pet.sleep()
#
#     def make_pets_work(self):
#         for pet in self.pets:
#             pet.work()
#             # if isinstance(pet, Dog):
#             #     pet.watch()
#             # elif isinstance(pet, Cat):
#             #     pet.catch()
#
#     def __str__(self):
#         return "名字是{}, 年龄{}岁的人".format(self.name, self.age)
#
# class Cat:
#     # 在创建一个小狗实例的时候, 给它设置几个属性
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s在吃饭" % self)
#
#     def play(self):
#         print("%s在玩" % self)
#
#     def sleep(self):
#         print("%s在睡觉" % self)
#
#     def work(self):
#         print("%s在捉老鼠" % self)
#
#     def __str__(self):
#         return "名字是{}, 年龄{}岁的小猫".format(self.name, self.age)
#
# class Dog:
#     # 在创建一个小狗实例的时候, 给它设置几个属性
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s在吃饭" % self)
#
#     def play(self):
#         print("%s在玩" % self)
#
#     def sleep(self):
#         print("%s在睡觉" % self)
#
#     def work(self):
#         print("%s在看家" % self)
#
#     def __str__(self):
#         return "名字是{}, 年龄{}岁的小狗".format(self.name, self.age)
#
# d = Dog("小黑", 18)
# c = Cat("小红", 2)
# p = Person("sz", [d, c], 18)
# p.yangPets()
# p.make_pets_work()







# -----------------------------------------代码2-------------------------------------------------
# class Dog:
#     # 在创建一个小狗实例的时候, 给它设置几个属性
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s在吃饭" % self)
#
#     def play(self):
#         print("%s在玩" % self)
#
#     def sleep(self):
#         print("%s在睡觉" % self)
#
#     def watch(self):
#         print("%s在看家" % self)
#
#     def __str__(self):
#         return "名字是{}, 年龄{}岁的小狗".format(self.name, self.age)
#
# d = Dog("小黑", 18)
# d.address = "xxx"
# d.eat()
# d.play()


# -----------------------------------------代码1-------------------------------------------------
# class Dog:
#     # 在创建一个小狗实例的时候, 给它设置几个属性
#     def __init__(self, name, age=1):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("名字是{}, 年龄{}岁的小狗在吃饭".format(self.name, self.age))
#
#     def play(self):
#         print("名字是{}, 年龄{}岁的小狗在玩".format(self.name, self.age))
#
#     def sleep(self):
#         print("名字是{}, 年龄{}岁的小狗在睡觉".format(self.name, self.age))
#
#     def watch(self):
#         print("名字是{}, 年龄{}岁的小狗在看家".format(self.name, self.age))
#
#
# d = Dog("小黑", 18)
# d.eat()
