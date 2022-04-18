
def drawborder(fun):
    def helper_fun(*args):
        print("*" * 40)
        fun(*args)
        print("#" * 40)
    return helper_fun


@drawborder
def greet(msg):
    print("Welcome",msg)

@drawborder
def RSVP(msg):
    print("RSVP",msg)


greet("Vaishali Ingle")
RSVP("Python Coding")
