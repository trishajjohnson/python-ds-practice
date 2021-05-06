def counter(num):
    counts = {}

    for n in num:
        counts[n] = counts.get(n, 0) + 1
    
    return counts

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)

    return counter(num1) == counter(num2)

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211)) 