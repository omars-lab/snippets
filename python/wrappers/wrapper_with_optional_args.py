import unittest
from functools import partial, wraps


def wrapper_with_optional_args(func=None, **optional_kargs):
    # If no function is passed, meaning we call the decorator with optional
    # params, return the same function still as a callable but with the
    # specified arg
    if not func:
        return partial(wrapper_with_optional_args, **optional_kargs)

    @wraps(func)
    def wrapper(*args, **kargs):
            print "Optional wrapper Args: {}".format(optional_kargs)
            func(*args, **kargs)
            return optional_kargs
    return wrapper


@wrapper_with_optional_args(hi="hi", bobby="bobby")
def test_1():
    pass


@wrapper_with_optional_args
def test_2():
    pass


class Tester(unittest.TestCase):

    def test_1_order_res(self):
        self.assertEqual(
            test_1(),
            {"hi": "hi", "bobby": "bobby"}
        )
        self.assertEqual(test_2(), {})

if __name__ == "__main__":
    unittest.main()
