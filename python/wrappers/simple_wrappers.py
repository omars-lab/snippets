
def WrapperNamePlusWrapperArgsGoHere(pointful):
    def it_dont_matter_what_you_call_me_but_ill_get_called(_function):
        def the_real_function_that_runs(*args, **kargs):
            print "Wrapper: Pre"
            print "Wrapper: Args: {}".format(pointful)
            try:
                _function(*args, **kargs)
            except Exception as e:
                print "Wrapper: {}".format(str(e))
            print "Wrapper: Post"
            return "$5"
        return the_real_function_that_runs
    return it_dont_matter_what_you_call_me_but_ill_get_called


@WrapperNamePlusWrapperArgsGoHere("Im not ")
def bad_foo():
    raise Exception("gonna mess my program up.")


print bad_foo() == "$5"
print "Ill bet you $5 the lines before this is True."
print "Haha I win"
