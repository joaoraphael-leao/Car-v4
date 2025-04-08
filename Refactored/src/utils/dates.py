def validate_date(start_date, end_date):
    """
    Validate if the start date is before the end date.
    """
    if start_date >= end_date:
        raise ValueError("Start date must be before end date.")
    return True