import unittest


def pass_by_reference(l):
    l.append(1)
    return


def pass_by_value(l):
    l = 2
    return


class Tester(unittest.TestCase):

    def test_reference(self):
        r = []
        pass_by_reference(r)
        pass_by_reference(r)
        pass_by_reference(r)
        pass_by_reference(r)
        pass_by_reference(r)
        self.assertEqual(r, [1, 1, 1, 1, 1])

    def test_value(self):
        a = 1
        pass_by_value(a)
        pass_by_value(a)
        pass_by_value(a)
        self.assertEqual(a, 1)

if __name__ == "__main__":
    unittest.main()
