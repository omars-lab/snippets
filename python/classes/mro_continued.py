import unittest

O = object


class F(O):
    pass


class E(O):
    pass


class D(O):
    pass


class C(D, F):
    pass


class B(D, E):
    pass


class A(B, C):
    pass


class Tester(unittest.TestCase):

    def test_order_res(self):
        self.assertEqual(F.mro(), [F, O])
        self.assertEqual(E.mro(), [E, O])
        self.assertEqual(D.mro(), [D, O])
        self.assertEqual(C.mro(), [C, D, F, O])
        self.assertEqual(B.mro(), [B, D, E, O])
        self.assertEqual(A.mro(), [A, B, C, D, E, F, O])

    # def test_read_only_mro(self):
    #     before = E.mro()
    #     E.mro()[0:2] = [x for x in reversed(E.mro()[0:2])],
    #     after = E.mro()
    #     # The MRO array is ready only thus, this does nothing:
    #     self.assertEqual(before, after)

    # def test_changing_the_mro_by_chaging_basses(self):
    #     self.assertEqual(
    #         E.mro(),
    #         [E, One, D, B, A, object]
    #     )
    #     # But changing a classes basses changes the mro (The bases are the
    #     # direct mixins to the class)
    #     before = E.__bases__
    #     E.__bases__ = tuple(y for y in reversed([x for x in E.__bases__]))
    #     after = E.__bases__
    #     # Make MRO for D [B, D, A, object]

    #     import pdb;pdb.set_trace()
    #     self.assertEqual(
    #         D().var,
    #         "B"
    #     )

    # def test_ambiguous_mro(self):
    #     # The order of method resolution is ambiguous.
    #     self.assertRaises(Exception, type("BADCLASS", (C, D), {}))

if __name__ == "__main__":
    unittest.main()
