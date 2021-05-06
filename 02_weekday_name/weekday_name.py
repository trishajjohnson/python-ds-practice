def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    weekdays = {
        1: 'Sunday', 
        2: 'Monday', 
        3: 'Tuesday', 
        4: 'Wednesday', 
        5: 'Thursday', 
        6: 'Friday', 
        7: 'Saturday'
    }
    if day_of_week < 1 or day_of_week > 7:
        return None
    else:
        return weekdays[day_of_week]

    # DAYS = [
    #     "Sunday",
    #     "Monday",
    #     "Tuesday",
    #     "Wednesday",
    #     "Thursday",
    #     "Friday",
    #     "Saturday",
    # ]

    # if day_of_week < 1 or day_of_week > 7:
    #     return None

    # return DAYS[day_of_week - 1]