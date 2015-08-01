import unittest


class Tester(unittest.TestCase):

    def test_list_comprehension(self):
        a = [(x, y)
             for x in [1, 2, 3]
             for y in [3, 1, 4]
             if x != y]

        b = []
        for x in [1, 2, 3]:
            for y in [3, 1, 4]:
                if x != y:
                    b.append((x, y))

        self.assertEqual(a, b)

    def test_dict_comprehension(self):
        _dict = {x: x**2 for x in (2, 4, 6)}
        self.assertEqual(
            _dict,
            {2: 4, 4: 16, 6: 36}
        )
        _dict = {k: v for k, v in [(2, 1), (4, 2), (6, 3)]}
        self.assertEqual(
            _dict,
            dict([(2, 1), (4, 2), (6, 3)])
        )
        _dict = {k: v for k, v in _dict.items()}
        self.assertEqual(
            _dict,
            dict([(2, 1), (4, 2), (6, 3)])
        )
        _dict = dict([(x, x) for x in 'abcabcaaadrr' if x not in 'abc'])
        self.assertEqual(
            _dict,
            {'d': 'd', 'r': 'r'}
        )
if __name__ == "__main__":
    unittest.main()
