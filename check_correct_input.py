"""Module for checking inputs.

Contains:
    int_number() - the function for checking int numbers
    float_number() - the function for checking float numbers
    check_bounds() - the function for checking numbers' bounds

Author: Viktoria Chelpykh
Date: 2026-05-06
"""


def int_number(entry_current, meaning):
    """The function for checking int numbers.
    
    The function check numbers on thier values. 
    If it is width or height it should be more than 99
    and should be int. If it is number of iterations
    it should be positive and int. If it is color
    it should be in range (0, 255) and int.

    Args:
        entry_current (ctk.CtkEntry): the entry where threre is a number which user entered
        meaning (str): The value of current entry

    Returns:
        - int: If input is correct, returns a number which user entered
        - str: If input is uncorrect, returns an error message
    """
    try:
        value_string = entry_current.get()
        value_int = int(value_string)
        value_float = float(value_string)
        if meaning == "width" or meaning == "height":
            if value_int >= 100 and value_int == value_float:
                return value_int
            else:
                return f"Значение {meaning} должно быть целое и не меньше 100"
        elif meaning == "number":
            if value_int > 0 and value_int == value_float:
                return value_int
            else:
                return f"Значение {meaning} должно быть целое положительное"
        elif meaning in ("RED", "GREEN", "BLUE"):
            if 0 <= value_int <= 255 and value_int == value_float:
                return value_int
            else:
                return f"Значение {meaning} должно быть целое от 0 до 255"
    except:
        return "Заполните все поля числами"


def float_number(entry_current):
    """The function for checking float numbers.

    Args:
        entry_current (ctk.CtkEntry): the entry where threre is a number which user entered

    Returns:
        - float: If input is correct, returns a number which user entered
        - str: If input is uncorrect, returns an error message
    """
    try:
        value = float(entry_current.get())
        return value
    except:
        return "Заполните все поля числами"
    
    
def check_bounds(current_min, current_max, meaning_min, meaning_max):
    """The function for checking numbers' bounds.

    Args:
        current_min (float): probable minimum
        current_min (float): probable maximum
        meaning_min (str): value of probable minimum
        meaning_max (str): value of probable maximum

    Returns:
        - bull: If input is correct, returns True
        - str: If input is uncorrect, returns an error message
    """
    if current_min < current_max:
        return True
    else:
        return f"{meaning_min} должен быть меньше, чем {meaning_max}"