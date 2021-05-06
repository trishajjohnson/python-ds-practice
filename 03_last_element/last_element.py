def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    if len(lst) is 0:
        return None
    else:
        return lst[-1]

# print(last_element([1, 2, 3, 4]))
# print(last_element([1, 2, 3]))
# print(last_element([1, 2, 3, 5, 9, 23]))
# print(last_element([]))