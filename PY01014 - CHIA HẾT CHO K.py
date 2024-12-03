"""
Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:

a + b ≤ N
a + b chia hết cho K
Input

Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).

Output

Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.

Nếu không tìm được số nào in ra -1
"""
'10 6 40'
'b = 2 8 14 20 26'

a, k, n = [int(x) for x in input().split()]

arr = []
for i in range(0,n+1,k):
    if i > a:
        arr.append(str(i-a))
# print(arr)
if arr == []:
    print(-1)
else:
    print(' '.join(arr))