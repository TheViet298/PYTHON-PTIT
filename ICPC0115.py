"""
Một số nguyên dương N được gọi là số Krish nếu tổng giai thừa các chữ số của N bằng chính nó. Ví dụ N = 145 = 1! + 4! + 5! = 145 là một số Krish. Cho số nguyên dương N, hãy kiểm tra N có phải là một số Krish hay không? Đưa ra “Yes” nếu N là một số Krish, ngược lại đưa ra “No”.

Input:

Dòng đầu tiên đưa vào T là số lượng bộ test.
Những dòng tiếp theo, mỗi dòng đưa vào một test. Mỗi test là một số nguyên dương N.
T, N thỏa mãn ràng buộc : 1≤T≤100; 1≤N ≤108;
Output:

Đưa ra kết quả mỗi test theo từng dòng.
"""
#Hàm giai thừa
def Factorial(n):
    if n == 0: return 1
    return n * Factorial(n - 1)

for T in range(int(input())):
    # Nhập chuỗi N
    N = input()
    # Tách số
    digits = [int(digit) for digit in N]
    # print(digits)
    res = 0
    for i in range(len(digits)):
        res += Factorial(digits[i])
    if res == int(N): print("YES")
    else: print("NO")
    # print(res)

