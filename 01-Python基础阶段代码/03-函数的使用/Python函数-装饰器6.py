

def zsq(func):
    def inner(*args, **kwargs):
        print("_" * 30)
        # print(args, kwargs)
        res = func(*args, **kwargs)
        return res
    return inner


@zsq
def pnum(num, num2, num3):
    print(num, num2, num3)
    return num + num2 + num3


@zsq
def pnum2(num):
    print(num)



res1 = pnum(123, 222, num3=666)
res2 = pnum2(999)


print(res1, res2)



