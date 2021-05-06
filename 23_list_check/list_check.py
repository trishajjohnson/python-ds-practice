def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    for el in lst:
        if type(el) is not list:
            return False

    return True

# print(list_check([[1], [2, 3]]))
# print(list_check([[1], "nope"]))