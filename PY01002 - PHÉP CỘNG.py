"""
Cho một phép toán có dạng a + b = c với a,b,c chỉ là các số nguyên dương có một chữ số.

Hãy kiểm tra xem phép toán đó có đúng hay không.

Input

Chỉ có một dòng ghi ra phép toán (gồm đúng 9 ký tự)

Ouput

Ghi ra YES nếu phép toán đó đúng. Ghi ra NO nếu sai.
"""
'2 + 3 = 5'
n = input()
sum = 0
# print(n[-1])
a = int(n[0])
b = int(n[4])

sum = a + b
if sum == int(n[-1]):
    print('YES')
else: print('NO')