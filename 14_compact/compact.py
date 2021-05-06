def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    copy = [el for el in lst if el]

    # for el in lst:
    #     if el:
    #         copy.append(el)
            
    return copy

print(compact([0, 1, 2, '', [], False, (), None, 'All done']))