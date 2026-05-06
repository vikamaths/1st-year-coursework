def int_number(entry_current, meaning):
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
    try:
        value = float(entry_current.get())
        return value
    except:
        return "Заполните все поля числами"
    
    
def check_bounds(current_min, current_max, meaning_min, meaning_max):
    if current_min < current_max:
        return True
    else:
        return f"{meaning_min} должен быть меньше, чем {meaning_max}"