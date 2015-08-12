import unittest


class Ten(object):
    x = "x"*10
    y = "y"*10
    z = "z"*10


class Five(Ten):
    x = "x"*5
    y = "y"*5
    z = "z"*5


class One(Five):
    # x = 1
    # y = 1
    # z = 1

    def __init__(self):
        self.x = "x"
        self.y = "y"
        self.z = "z"


class Tester(unittest.TestCase):

    def test_variable_order(self):
        obj = One()

        # First is instance Variables.
        self.assertEqual(getattr(obj, 'x'), "x")
        del obj.x

        # Then its class variables or parent class variables
        self.assertEqual(getattr(obj, 'x'), "x"*5)

        # Note that if the class attributes chance, and instance vars arent
        # being used, then they will change too.
        setattr(Five, 'x', "apple")
        self.assertEqual(getattr(obj, 'x'), "apple")

if __name__ == "__main__":
    unittest.main()
