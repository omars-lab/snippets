import unittest


expressions = {
    "gten": lambda x: x > 10,
    "cube": lambda y: y**3,
    "add": lambda x, y: x + y if (x is not None and y is not None) else (
                                  x if y is None else y),
    "reduce": lambda x, y: "{} {}".format(str(x), str(y)),
}


def lten(x):
    return x < 10


class Tester(unittest.TestCase):
    def test_functional_programming(self):
        self.assertEqual(
            filter(lten, range(2, 25)),
            range(2, 10)
        )
        self.assertEqual(
            filter(expressions["gten"], range(2, 25)),
            range(11, 25)
        )
        self.assertEqual(
            map(expressions["cube"], [1, 2, 3]),
            [1, 8, 27]
        )
        self.assertEqual(
            map(expressions["add"], [2, 3, 4], [2, 3, 4]),
            [4, 6, 8]
        )
        self.assertEqual(
            reduce(expressions["reduce"], range(1, 4)),
            "1 2 3"
        )

    def test_more_functional_programming(self):
        stuff = [(x, y, z)
                 for x in [1, 2, 3]
                 for y in [3, 1, 4]
                 for z in range(2, 100)
                 if x != y and z % 25 == 0]
        sum_map = reduce(lambda x, y: x+y,
                         map(lambda x: x[0]+x[1]+x[2], stuff))

        col1 = [x for x, y, z in stuff]
        col2 = [y for x, y, z in stuff]
        col3 = [z for x, y, z in stuff]
        sum_reduce = (reduce(lambda x, y: x+y, col1)
                      + reduce(lambda x, y: x+y, col2)
                      + reduce(lambda x, y: x+y, col3))

        self.assertEqual(sum_map, sum_reduce)

if __name__ == "__main__":
    unittest.main()
