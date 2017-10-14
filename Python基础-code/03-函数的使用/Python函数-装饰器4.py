

def zhuangshiqi_line(func):
    def inner():
        print("---------------------------")
        func()
    return inner


def zhuangshiqi_star(func):
    def inner():
        print("*" * 30)
        func()
    return inner

@zhuangshiqi_line # == print_content = zhuangshiqi_line(print_content)
@zhuangshiqi_star # == print_content =  zhuangshiqi_star(print_content)

# print("---------------------------")
# print("*" * 30)
# print("社会我顺哥, 人狠话不多")
def print_content():
    print("社会我顺哥, 人狠话不多")



print_content()