# The intention of this module is to show how to suppress an exception
# that gets thrown inside a context (By returning True if the exception type
# is to be suppressed)


class Suppressor(object):
    """
    A simple context manager that suppresses exceptions
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if not type:
            return
        # This will suppress any exception of type instance that can be
        # initiallized wit no variables
        if isinstance(type(), Exception):
            "The exception was suppressed"
            return True

        # This will suppress exception of type Exception
        if type == Exception:
            "The exception was suppressed"
            return True
try:
    with Suppressor() as context:
        raise Exception()
except Exception as e:
    print "This never runs, the exception gets surpressed."
