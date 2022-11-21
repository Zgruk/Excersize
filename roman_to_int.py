def romanToInt():
    """
    Функция переводит число, написанное римскими цифрами,
    в число, написанное арабскими.
    Римские цифры чувствительны к регистру --> вводить большими
    английскими буквами.
    """
    number = str(input('Пожалуйста введите число римскими цифрами: \n'))
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
    number = number.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
    print(sum(map(lambda x: roman_to_integer[x], number)))

romanToInt()
