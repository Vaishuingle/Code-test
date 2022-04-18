
def logBeforeAfter(fun):
    def helper(*args, **kwargs):
        print(f"Logged in successfully......")
        fun(*args , **kwargs)
        print(f"logged out successfully......")
        print("-" * 40)

    return helper


@logBeforeAfter
def fun(x, y):
    print("fun", x, y)

@logBeforeAfter
def fun1(*args):
    print("fun1", args)


@logBeforeAfter
def fun2(**kwargs):
    print("fun2", kwargs)

@logBeforeAfter
def fun3(*args, **kwargs):
    print("fun3", args, kwargs)

fun(1, 2)
fun1("Vaishali" , "Ingle")
fun2(python ="coding")
fun3("Vaishali" ,python ="coding")