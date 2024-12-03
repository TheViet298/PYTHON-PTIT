"""
4.	Viết chương trình python chuyển đổi một số cơ số 8 sang cơ số 10: 
Input:745
Output :485

7*8^0
4*8^1
5*8^2

"""

import math
def Oct2Dec(a):
    p = 0
    decNum = 0
    while(a > 0):
        decNum += (a%10) * math.pow(8, p)
        a //= 10
        p += 1
    return int(decNum)

n = int(input())
print(Oct2Dec(n))