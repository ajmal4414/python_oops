

#user built decorators
def outer_fun(func):
    def inner(x,y):
        if (x<y):
            x,y = x,y
        return func(x,y)
    return inner

@outer_fun
def divide(x,y):
    print(x/y)

divide(2,4)