def calculate_floor(string: str):
    string_upper = string.upper()
    u = string_upper.count("U")
    d = string_upper.count("D")
    return u - d



