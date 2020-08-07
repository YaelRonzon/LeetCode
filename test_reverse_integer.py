import pytest
import reverse_integer as ri

# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.
# Test

def test_reverse_integer_positive():
    """Simple test with a positive number inside the range."""
    test_num = 123
    expected = 321
    result = ri.reverse_integer(test_num)
    assert result == expected

def test_reverse_integer_with_negative():
    """Simple test with a negative inside the range."""
    test_num = -123
    expected = -321
    result = ri.reverse_integer(test_num)
    assert result == expected

def test_reverse_integer_overflows_positive():
    """Simple test with a positive number outside the range."""
    test_num = 8463847412
    # 32 bit range: -2,147,483,648 to +2,147,483,647
    result = ri.reverse_integer(test_num)
    expected = 0
    assert result == expected

def test_reverse_integer_overflows_negative():
    """Simple test with a negative number outside the range."""
    test_num = -9463847412
    expected = 0
    result = ri.reverse_integer(test_num)
    assert result == expected
   