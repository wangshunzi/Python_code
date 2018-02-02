

class Person:
    @staticmethod
    def jingtai():
        print("这是一个静态方法")


Person.jingtai()
p = Person()
p.jingtai()

func = Person.jingtai
func()