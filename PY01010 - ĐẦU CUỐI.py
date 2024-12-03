"""
Viết chương trình kiểm tra xem số nguyên dương N có thỏa mãn tính chất: nếu ta lấy hai chữ số đầu và hai chữ số cuối của nó thì sẽ tạo ra số có hai chữ số giống nhau hay không?

Input

Dòng đầu ghi số số test (không quá 20). Mỗi test là 1 số nguyên dương N có ít nhất 4 chữ số, nhưng không quá 18 chữ số.

Output

Ghi ra YES hoặc NO
"""
#1234512
for t in range(int(input())):
    N = input()
    # print(N[:2])
    # print(N[-2:])
    if N[:2] == N[-2:]: print("YES")
    else: print("NO")