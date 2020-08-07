# 7. Reverse Integer
# Given a 32-bit signed integer, reverse digits of an integer.

def reverse_integer(num):
    num = str(num)
    res = int(num[::-1]) if num[0] != "-" else int("-" + num[1::][::-1])
    return res if res <= 2147483647 and res >= -2147483648 else 0


# Before refactor:
# def reverse_integer(num):
#     num = str(num)
#     sign = ""
#     if num[0] == "-":
#         sign = "-"
#         num = num[1::]
#     res = int(sign+num[::-1])
#     if res <= 2147483647 and res >= -2147483648:
#         return res
#     else:
#         return 0

# First Refactor:
# def reverse_integer(num):
#     num = str(num)
#     sign = ""
#     if num[0] == "-":
#         sign = "-"
#         num = num[1::]
#     res = int(sign+num[::-1])
#     return res if res <= 2147483647 and res >= -2147483648 else 0





