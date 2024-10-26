def get_multiplied_digits(number):
    str_number1 = str(number)
    str_number = str_number1 + "1"
    first = int(str_number[0])
    if len(str_number) > 1:
        first *= get_multiplied_digits(int(str_number[1:]))
    return first


result = get_multiplied_digits(402030)
print(result)
