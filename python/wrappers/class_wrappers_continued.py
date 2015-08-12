from functools import partial, wraps

# This wrapper takes a class, and wraps all methods within the class with the
# specified decorator.
# This only supports instance methods, not classmethods and static methods???


def printer():
    def handler(_func):
        @wraps(_func)
        def wrapper(*args, **kargs):
            print "Start {}".format(_func.__name__)
            resp = _func(*args, **kargs)
            print "End {}".format(_func.__name__)
            return resp
        return wrapper
    return handler

# NOTE: staticmethods and class methods are NOT CALLABLE


def wrap_all_methods(cls=None, wrapper=None):
    if not cls:
        return partial(wrap_all_methods, wrapper=wrapper)
    import pdb;pdb.set_trace()
    for attr, value in vars(cls).items():
        if callable(value):
            setattr(cls, attr, wrapper(value))
    return cls


@wrap_all_methods(wrapper=printer())
class X(object):

    @classmethod
    def i_wont_get_wrapped(cls):
        pass

    @staticmethod
    def neither_will_i():
        pass

    def a(self):
        return

    def b(self):
        return

x = X()

x.a()
x.b()
x.i_wont_get_wrapped()
x.neither_will_i()
