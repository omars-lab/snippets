def max_length(x, y):
    """
    This function can be passed to a reduce to determine the maximum length of
    a list within a list of lists.
    """
    if type(x) == list and type(y) == list:
        return max(len(x), len(y))
    elif type(x) == list and type(y) == int:
        return max(len(x), y)
    elif type(x) == int and type(y) == list:
        return max(x, len(y))
    elif type(x) == int and type(y) == int:
        return max(x, y)

    if type(x) != int or type(x) != list:
        raise TypeError("Invalid type: " + str(type(x)))

    if type(y) != int or type(y) != list:
        raise TypeError("Invalid type: " + str(type(x)))
