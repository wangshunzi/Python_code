
class Person(object):
    pass


print(Person.__bases__)

# Python2.x 如果定义一个类, 没有显示的继承自object , 那么这个类就是一个经典类
# 必须显示的继承自, object, 它才是一个新式类


# Python3.x , 如果直接定义一个类, 会隐式的继承object, 默认情况下, 就已经是一个新式类