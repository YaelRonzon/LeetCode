import pytest
import roman as r

def test_multiples_of_five():
    test_string_1 = "V"
    test_string_2 = "L"
    test_string_3 = "D"
    result_1 = r.roman_to_int(test_string_1)
    result_2 = r.roman_to_int(test_string_2)
    result_3 = r.roman_to_int(test_string_3)
    expected_1 = 5
    expected_2 = 50
    expected_3 = 500
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3

def test_units():
    test_string_1 = "I"
    test_string_2 = "XX"
    test_string_3 = "CCC"
    test_string_4 = "MMM"
    result_1 = r.roman_to_int(test_string_1)
    result_2 = r.roman_to_int(test_string_2)
    result_3 = r.roman_to_int(test_string_3)
    result_4 = r.roman_to_int(test_string_4)
    expected_1 = 1
    expected_2 = 20
    expected_3 = 300
    expected_4 = 3000
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3
    assert result_4 == expected_4
    

def test_sum_units():
    test_string_1 = "VI"
    test_string_2 = "XVII"
    test_string_3 = "LXVIII"
    test_string_4 = "CCCLXXXVII"
    result_1 = r.roman_to_int(test_string_1)
    result_2 = r.roman_to_int(test_string_2)
    result_3 = r.roman_to_int(test_string_3)
    result_4 = r.roman_to_int(test_string_4)
    expected_1 = 6
    expected_2 = 17
    expected_3 = 68
    expected_4 = 387
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3
    assert result_4 == expected_4


def test_nine_four_numbers():
    test_string_1 = "IV" #4
    test_string_2 = "IX" #9
    test_string_3 = "XL" #40
    test_string_4 = "XC" #90
    test_string_5 = "CD" #400
    test_string_6 = "CM" #900
    test_string_7 = "CMXCIV" #994
    result_1 = r.roman_to_int(test_string_1)
    result_2 = r.roman_to_int(test_string_2)
    result_3 = r.roman_to_int(test_string_3)
    result_4 = r.roman_to_int(test_string_4)
    result_5 = r.roman_to_int(test_string_5)
    result_6 = r.roman_to_int(test_string_6)
    result_7 = r.roman_to_int(test_string_7)
    expected_1 = 4
    expected_2 = 9
    expected_3 = 40
    expected_4 = 90
    expected_5 = 400
    expected_6 = 900
    expected_7 = 994
    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3
    assert result_4 == expected_4
    assert result_5 == expected_5
    assert result_6 == expected_6
    assert result_7 == expected_7
   