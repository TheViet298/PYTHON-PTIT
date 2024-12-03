
import math

'Ví dụ a = 42, b = 28, ước số chung lớn nhất = 14. Tổng chữ số của ước số chung là 1+4=5 là một số nguyên tố.'
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n*0.5), n-1):
        if n % i == 0:
            return False
    return True

for i in range(int(input())):
    a, b = map(int, input().split())

    Gcd_ab = math.gcd(a, b)
    # print(Gcd_ab)
    sum = 0

    for i in str(Gcd_ab):
        # print(i)
        sum += int(i)
    if is_prime(sum):
        print("YES")
    else:
        print("NO")