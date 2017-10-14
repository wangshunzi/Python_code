

# 给发说说函数增加一些额外的功能,
# 1. 函数名字不能发生改变
# 2. 函数体内部的代码不能发生改变


def check(func):
    print("xxx")
    def inner():
        print("登录验证操作....")
        func()
    return inner

@check
def fss():
    print("发说说")

# fss = check(fss)




# fss()