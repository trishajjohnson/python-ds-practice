def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    # my solution
    sum = 0

    if isinstance(end, int) and end > len(nums) or end == None:
        for i in range(start, len(nums)):
            sum += nums[i]
        
    else:
        for i in range(start, end + 1):
            sum += nums[i]

    return sum

    # Springboard solution 
    # if end is None:
    #     end = len(nums)

    # return sum(nums[start:end + 1])
    
print(sum_range([1, 2, 3, 4]))
print(sum_range([1, 2, 3, 4], 1))
print(sum_range([1, 2, 3, 4], end=2))
print(sum_range([1, 2, 3, 4], 1, 3))
print(sum_range([1, 2, 3, 4], 1, 99))