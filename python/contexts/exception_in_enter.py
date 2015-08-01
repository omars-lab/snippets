# The intention of this module is to see if __exit__ is called if an
# exception is thrown in enter.


class BadContext(object):
    """
    A simple context manager that throws an exception in enter
    """
    def __init__(self):
        self.array = []

    def __enter__(self):
        raise Exception("Like whatever")

    def __exit__(self, type, value, traceback):
        print "The __exit__ gets called"
        if type == Exception:
            return True

try:
    with BadContext():
        print "Never Gets Run"
except Exception as e:
    "The __exit__ never gets called"
