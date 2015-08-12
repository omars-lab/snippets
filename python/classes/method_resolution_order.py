import unittest

"""
Refer to the following links:
https://www.python.org/download/releases/2.3/mro/

"""


class A(object):
    var = "A"


class B(object):
    var = "B"


class C(A, B):
    var = "C"


class D(B, A):
    var = "D"


class One(B):
    var = "One"


class E(One, D):
    pass


class Tester(unittest.TestCase):

    def test_1_order_res(self):

        self.assertEqual(
            One.mro(),
            [One, B, object]
        )

        self.assertEqual(
            A.mro(),
            [A, object]
        )

        self.assertEqual(
            B.mro(),
            [B, object]
        )

        self.assertEqual(
            C.mro(),
            [C, A, B, object]
        )

        self.assertEqual(
            D.mro(),
            [D, B, A, object]
        )

        self.assertEqual(
            E.mro(),
            [E, One, D, B, A, object]
        )

    def test_2_read_only_mro(self):
        before = E.mro()
        E.mro()[0:2] = [x for x in reversed(E.mro()[0:2])],
        after = E.mro()
        # The MRO array is ready only thus, this does nothing:
        self.assertEqual(before, after)

    def test_3_changing_the_mro_by_chaging_basses(self):

        self.assertEqual(E.mro(), [E, One, D, B, A, object])
        self.assertEqual(E.var, "One")

        # But changing a classes basses changes the mro
        # (The bases are the direct mixins to the class)
        before = E.__bases__
        E.__bases__ = tuple(y for y in reversed([x for x in E.__bases__]))
        after = E.__bases__
        self.assertNotEqual(before, after)

        self.assertEqual(E.mro(), [E, D, One, B, A, object])
        self.assertEqual(E.var, "D")

    def test_ambiguous_mro(self):
        # The order of method resolution is ambiguous.
        with self.assertRaises(TypeError):
            type("BADCLASS", (C, D), {})

if __name__ == "__main__":
    unittest.main()
