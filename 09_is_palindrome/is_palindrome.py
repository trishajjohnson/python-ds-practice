def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    word = phrase.replace(' ', '').lower()
    if word == word[::-1]:
        return True
    else:
        return False

# print(is_palindrome("Noon"))
# print(is_palindrome("taco cat"))
# print(is_palindrome("robert"))
# print(is_palindrome("Hannah"))