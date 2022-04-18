def nozero(fun):
    def Helper(x,y):
        if x==0 or y==0:
            print("Operation denied with zero")
        else:
            print(fun(x,y))
    return Helper(0,4)

@nozero
def div(x,y):
   return x/y

@nozero
def mul(x,y):
   return x*y

@nozero
def add(x,y):
   return x+y
@nozero
def sub(x,y):
   return x-y