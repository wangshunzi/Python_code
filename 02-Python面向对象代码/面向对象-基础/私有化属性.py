#
class Animal:
    __x = 10
    def test(self):
        print(Animal.__x)
        print(self.__x)
    pass


# print(Animal.__x)
print(Animal.__dict__)
print(Animal._Animal__x)
#
# #
# class Dog(Animal):
#     def test2(self):
#         print(Dog.__x)
#         print(self.__x)
#     pass
# # #
#
# # 测试代码
# a = Animal()
# a.test()
#
# d = Dog()
# d.test2()
#
#
# print(Animal.__x)
# print(Dog.__x)
# print(a.__x)
# print(d.__x)

__all__ = ["__a"]
#
__a = 666