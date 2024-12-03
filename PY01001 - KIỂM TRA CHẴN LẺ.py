"""
Cho một số nguyên dương N không quá 5 chữ số, hãy kiểm tra và in ra số đó chẵn hay lẻ. Nếu chẵn ghi ra chữ CHAN, nếu ngược lại ghi ra chữ LE.

Input

Chỉ có một dòng ghi số N

Output

Ghi ra kết quả trên một dòng.
"""

N = input()
# print(N[-1])
if N[-1] in ('0', '2', '4', '6', '8'):
    print("CHAN")
else:
    print("LE")