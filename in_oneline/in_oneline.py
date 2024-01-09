input_string = input()
print([input_string[i] if (ord(input_string[i]) - 97) % 2 == 0 else input_string[i].upper() for i in
       range(len(input_string))].sort(
    reverse=True))
