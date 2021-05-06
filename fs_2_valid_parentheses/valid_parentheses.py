def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    parens_dict = {}

    for ch in parens:
        if parens_dict[ch]:
            parens_dict[ch] += 1
        else:
            parens_dict[ch] = 1
    
    if parens_dict['('] == parens_dict[')']:
        return True
    else:
        return False