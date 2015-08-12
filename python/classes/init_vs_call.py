# making a class callable:


class a(object):

    def __init__(self, a):
        print "__init__"
        self.a = a

    def __call__(self, *args):
        print "__call__"
        self.a = args[0]


# Based on this code, when we call a, the __init__ function gets called. My guess
# is that we dont have an instance initiallzed, then when we have an instance,
# we can call it

# Initallizing an obj
apple = a("Hello")

# Calling an obj
apple("Hi")


# What will this do? :
# @a
# def fuu(*args):
#     print args

# fuu("hi")
