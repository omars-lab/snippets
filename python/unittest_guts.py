import unittest


class it_dont_matter_what_you_call_me(unittest.TestCase):
    """This is a docstirng attr """

    def test_this_will_run(self):
        print "printing: 1"

    @unittest.SkipTest
    def test_this_will_run_as_well(self):
        print "printing: 2"

    # for unittest main to run your method, it must begin with the
    # word "test"
    def this_will_not_run(self):
        print "printing: I will not run, therefore i will never print"

    # for unittest main to run your method, it must begin with the
    # word "test"
    def TEST_is_it_case_sensitive(self):
        print "printing: I dont know, lets find out"
        print "printing: Turns out its case sensitive, so i wont run"

    @unittest.SkipTest
    def this_will_not_run_as_well(self):
        print "printing: I will not run either"


# if __name__ == "__main__":
#     unittest.main()

if __name__ == "__main__":
    for k, val in globals().items():
        # print k, val
        if isinstance(val, unittest.TestCase.__class__):
            print("printing attributes for class: ",
                  it_dont_matter_what_you_call_me)
            for attrib_name, attrib_val in val.__dict__.items():
                if callable(attrib_val):
                    if attrib_name.startswith("test"):
                        print "\t", attrib_name, " = ", attrib_val
