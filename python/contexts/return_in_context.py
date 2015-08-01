# The intention of this module is to test if the __exit__ method of a
# context is called when we return a value from within the with block

# Notes on Contexts. Any class can become context based if it implements
# an __enter__ and __exit__ function. The general use is that certain
# properties are true as long as the context has entered and not exited


class Context(object):
    """
    A simple context manager that initiallizes an array, and
    prints the array when the context is left
    """
    def __init__(self):
        self.array = []

    # Called when the context is entered
    # We can rename what is returned in this function with "as"
    # with Context() as array: array.append(1)
    def __enter__(self):
        return self.array

    def __exit__(self, type, value, traceback):
        print self.array

# Testing if the exit context runs if a return
# statement is encountered within the with block
def test():
    with Context() as array:
        array.append(1)
    return None

# If the __exit__ gets called, we should see an array with [1] print.
# If not, nothing will happen
test()
