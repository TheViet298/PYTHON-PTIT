"""
Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1. Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

Input

Dòng đầu ghi số bộ test, không quá 10.

Dòng thứ 2 ghi số N (1 < N < 10000)

Output

Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.
"""
from math import gcd

# Hàm kiểm tra số nguyên tố
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

# Hàm tính K
def count_coprime(N):
    count = 0
    for x in range(1, N):
        if gcd(x, N) == 1: #Cùng là nguyên  tố
            count += 1
    return count

# Đọc input
for t in range(int(input())):
    N = int(input())
    K = count_coprime(N)  
    if is_prime(K):  
        print("YES")
    else:
        print("NO")

