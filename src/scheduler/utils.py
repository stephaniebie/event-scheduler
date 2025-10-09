def create_datetime_tuple(date: str, time: str):
    """
    Creates a datetime tuple of integers in the form (year, month, day, hour, minute)

    Parameters
    ----------
    date: str
        A date string of the form YYYY-MM
    time: str
        A time string of the form HH:MM
    """
    # NOTE: Uses strict string splicing which assumes no errors with date and time inputs
    #       If time permits, update this to catch possible invalid types or string formats
    return tuple(int(d) for d in [date[:4], date[5:7], date[8:], time[:2], time[3:]])
