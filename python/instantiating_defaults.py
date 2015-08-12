import unittest


def fun(a, l=[]):
    l.append(a)  # mutables are passed by reference
    return l


def fun1(a, l=[]):
    l.append(a)  # mutables are passed by reference
    # print l
    x = l
    del l
    return x


def fun2(a, l=3):
    yield l
    l = a  # makes a copy of l and sets it to a
    yield l


class Tester(unittest.TestCase):

    # @unittest.SkipTest
    def test_fun(self):
        self.assertEquals(
            fun(1),
            [1]
        )
        # The above is fairly straight forward.
        self.assertEquals(
            fun(2),
            [1, 2]
        )
        # This is a bit tricky. The statement is true beacuse the default
        # element is shared accross all instances of the method, thus when
        # fun(1) ran, it appended 1 to the array. When fun(2) ran, the default
        # was not re-instantiated. Instead, it used the previous instance

    # @unittest.SkipTest
    def test_fun1(self):
        self.assertEquals(
            fun1(1),
            [1]
        )
        # The above is fairly straight forward.
        self.assertEquals(
            fun1(2),
            [1, 2]
        )
        # Even though we delete l in fun1, we see the same behavior. It seams
        # to be that something external to the function is responsible for
        # supplying the default value of l to the function. And once it creates
        # the default value for a function, it holds onto it.

    # @unittest.SkipTest
    def test_fun2(self):
        gen = fun2(1)
        self.assertEquals(
            (gen.next(), gen.next()),
            (3, 1)
        )
        # The above is fairly straight forward. l = 3, then we set l to 1, and
        # return it as well. It is important to note that at this point,
        # following the previous example, since we set l to 1, that the next
        # time we invoke the funtion, we will get l as 1, ....................

        gen = fun2(2)
        self.assertNotEqual(
            (gen.next(), gen.next()),
            (1, 2)
        )

        gen = fun2(3)
        self.assertEqual(
            (gen.next(), gen.next()),
            (3, 3)
        )
        # But thats not the case. L still is 3. Why? Because l is passed as any
        # other variable in python. When it is a primitive, we are passed a
        # copy, but when we are passed an object, we are given a reference.
        # Thus we must be careful passing objects as default values to methods.

if __name__ == "__main__":
    unittest.main()
