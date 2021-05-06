def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap_phrase = ''

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            letter = letter.swapcase()
            swap_phrase += letter
        else:
            swap_phrase += letter

    return swap_phrase

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A'))
print(flip_case('aAAAhhh', 'A'))
print(flip_case('Aaaahhh', 'h'))
