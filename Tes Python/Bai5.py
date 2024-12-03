"""
5.	Một số được gọi là strong number nếu tổng giai thừa các ước của nó bằng chính nó. For example: 145 since
1! + 4! + 5! = 1 + 24 + 120 = 145
Viết chương trình python, nhập vào số n và in ra tất cả các số strong number trong đoạn 1 đến n

Input: 200
Output :1 2 145

"""

import math

def is_strong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += math.factorial(digit)
        temp //= 10
    return sum == num

n = int(input())
strong_numbers = []

for i in range(1, n + 1):
    if is_strong_number(i):
        print(i, end = ' ')
