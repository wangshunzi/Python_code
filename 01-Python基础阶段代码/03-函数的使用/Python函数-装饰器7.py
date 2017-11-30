
def getzsq(char):
    def zsq(func):
        def inner():
            print(char * 30)
            func()

        return inner
    return zsq




# def zsqe(func):
#     def inner():
#         print("=" * 30)
#         func()
#     return inner
#
# def zsqs(func):
#     def inner():
#         print("*" * 30)
#         func()
#     return inner

@getzsq("*") # f1 = zsq(f1)
def f1():
    print("666")


f1()