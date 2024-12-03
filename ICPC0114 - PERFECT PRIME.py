"""
Một số nguyên dương N được gọi là Perfect Prime nếu N là số nguyên tố; đảo ngược các chữ số của N cũng là một số nguyên tố; tổng các chữ số của N là một số nguyên tố và mỗi chữ số của N cũng là một số nguyên tố. Cho số nguyên dương N, hãy kiểm tra N có phải là Perfect Prime hay không? Đưa ra “Yes” nếu N là Perfect Prime, ngược lại đưa ra “No”.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤107;
Output:

Đưa ra kết quả mỗi test theo từng dòng.
"""

# Hàm kiểm tra số nguyên tố
def prime(N):
    if N < 2:  
        return False
    for i in range(2, int(N**0.5) + 1): 
        if N % i == 0:
            return False
    return True

# Hàm kiểm tra Perfect Prime
def is_perfect_prime(N):

    if not prime(N):
        return False
    
    # Kiểm tra số đảo ngược của N là số nguyên tố
    reversed_N = int(str(N)[::-1])
    if not prime(reversed_N):
        return False

    # Kiểm tra tổng các chữ số của N là số nguyên tố
    digit_sum = sum(int(digit) for digit in str(N))
    if not prime(digit_sum):
        return False

    # Kiểm tra từng chữ số của N là số nguyên tố
    for digit in str(N):
        if not prime(int(digit)):
            return False

    return True

# Đọc số lượng bộ test
T = int(input())

for _ in range(T):
    N = int(input()) 
    if is_perfect_prime(N):
        print("Yes")
    else:
        print("No")

        