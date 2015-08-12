import unittest


class Callable(object):
    def __call__(self):
        print "Hell yea im callable."


def callme():
    print "And so am I."


class Decorator(object):
    def __init__(self, statement):
        self.stmt = statement

    def __call__(self, _function):
        def decorator(*args, **kargs):
            print
            print "Bet you didnt see that comming"
            _function(*args, **kargs)
            print "Huh huh"
            print
            return self.stmt
        return decorator


class Tester(unittest.TestCase):

    def test_callable(self):
        self.assertEqual(callable(Callable()), True)
        self.assertEqual(callable(callme), True)

    def test_class_decorator(self):
        statement = "I like apple pie"

        @Decorator("I like apple pie")
        def it_dont_matter():
            return None

        self.assertEqual(it_dont_matter(), statement)

if __name__ == "__main__":
    unittest.main()
