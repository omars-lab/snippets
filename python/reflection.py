import unittest


class Callable(object):
    x = "x"*5

    def __call__(self):
        print "Hell yea im callable."


def callme():
    print "And so am I."


class Tester(unittest.TestCase):

    def test_callable(self):
        self.assertEqual(callable(Callable()), True)
        self.assertEqual(callable(callme), True)

    def test_reflection(self):
        obj = Callable()
        self.assertEqual(hasattr(obj, 'x'), True)
        self.assertEqual(getattr(obj, 'x'), "x"*5)

if __name__ == "__main__":
    unittest.main()
