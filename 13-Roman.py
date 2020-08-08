
# Given a roman numeral, convert it to an integer.
# This version allows to add more numerals to the dictionary.

def roman_to_int(roman_num):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000     
    }
    roman_num = roman_num[::-1]
    counter = 0
    start = roman[roman_num[0]]
    list_of_nums = []
    for i in roman_num:
        if roman[i] == start:
            counter += roman[i]
        else:
            if counter:
                list_of_nums.append(counter)
                counter = 0
            list_of_nums.append(roman[i])
            start = roman[i]
    if counter:
        list_of_nums.append(counter)
        counter = 0
    total = 0
    for i in list_of_nums:
        if i >= counter:
            total += i
        else:
            total -= i
        counter = i
        print(counter)
    return total
