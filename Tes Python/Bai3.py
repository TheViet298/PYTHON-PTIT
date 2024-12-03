"""
3.	Viết chương trình python kiểm tra xem số nhập vào có bằng tổng của 2 số nguyên tố hay ko? Nếu có thì in kết quả ra ngoài màn hình
Input: 16
OUTPUT:
16 = 3 + 13
16 = 5 + 11

"""
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input())
primes = []
for i in range(2, n):
    if is_prime(i):
        #print(i)
        primes.append(i)

check = False
#Duyệt sâu
for i in range(len(primes)):
    for j in range(i, len(primes)):
        if primes[i] + primes[j] == n:
            print(f"{n} = {primes[i]} + {primes[j]}")