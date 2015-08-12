import unittest


a = set('aaaaabbcdrr')
b = set('aaaaclmz')


class Tester(unittest.TestCase):

    def test_subtract(self):
        self.assertEqual(
            a - b,
            set(['b', 'd', 'r'])
        )

    def test_or(self):
        self.assertEqual(
            a | b,
            set(['a', 'b', 'c', 'd', 'l', 'm', 'r', 'z'])
        )

    def test_and(self):
        self.assertEqual(
            a & b,
            set(['a', 'c'])
        )

    def test_xor(self):
        self.assertEqual(
            a ^ b,
            set(['b', 'd', 'l', 'm', 'r', 'z'])
        )

    def test_xor_full(self):
        self.assertEqual(
            (a | b) - (a & b),
            set(['b', 'd', 'l', 'm', 'r', 'z'])
        )

if __name__ == "__main__":
    unittest.main()
