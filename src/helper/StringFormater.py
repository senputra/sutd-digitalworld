def force_double_digit(value) -> str:
    if len(str(value)) < 2:
        return "0{}".format(value)
    else:
        return value
