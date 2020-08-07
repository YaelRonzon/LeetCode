import pytest
import TwoSum as ts

def test_TwoSumv1_simple():
    test_nums = [2, 7, 11, 15]
    test_target = 9
    expected = [0, 1]
    result = ts.two_sum(test_nums, test_target)
    assert expected == result

def test_TwoSumv2_simple():
    test_nums = [2, 7, 11, 15]
    test_target = 9
    expected = [0, 1]
    result = ts.two_sum_v2(test_nums, test_target)
    assert expected == result

def test_TwoSumV2_number_equal_half():
    test_nums = [4, 6, 2, 3]
    test_target = 8
    expected = [1, 2]
    result = ts.two_sum_v2(test_nums, test_target)
    assert expected == result

# nums = [2, 7, 11, 15] 
# target = 9
# expected = [0, 1]
