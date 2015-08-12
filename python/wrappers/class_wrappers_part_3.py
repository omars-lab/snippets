# This wrapper takes a class, and wraps all attribute access with a print


def attibute_printer(cls):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print "Get:", name
        return orig_getattribute(self, name)
    cls.__getattribute__ = __getattribute__
    return cls


@attibute_printer
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
