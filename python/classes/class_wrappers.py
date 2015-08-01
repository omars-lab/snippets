

def printer():
    class Wrapper(object):
        '''
        Object wrapper class.
        This a wrapper for objects. It is initialiesed with the object to wrap
        and then proxies the unhandled getattribute methods to it.
        Other classes are to inherit from it.
        '''

        def __new__(wrapper, cls):
            print "in new"
            print wrapper
            print cls
            return object.__new__(cls)

        def __init__(self, *args):
            print "Args: {}".format(args)

    return Wrapper


@printer()
class x():
    pass

a = x(1, 2, 3)
