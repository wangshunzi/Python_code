

def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        func(*args, **kwargs)
    return inner


@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)

@zsq
def pnum2(num):
    print(num)


pnum(123, 222, num3=666)
pnum2(999)





