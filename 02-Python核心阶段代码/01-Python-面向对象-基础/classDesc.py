
class Person:
    """
    关于这个类的描述, 类的作用, 类的构造函数等等; 类属性的描述
    Attributes:
        count: int 代表是人的个数
    """
    # 这个表示, 是人的个数
    count = 1

    def run(self, distance, step):
        """
        这个方法的作用效果
        :param distance: 参数的含义, 参数的类型int, 是否有默认值
        :param step:
        :return: 返回的结果的含义(时间), 返回数据的类型int
        """
        print("人在跑")
        return distance / step
    def __init__(self):
        self.__name = "sz"

# help(Person)

def xxx():
    """
    这是一个xxx函数, 有xxx作用
    :return:
    """
    print("xxx")




