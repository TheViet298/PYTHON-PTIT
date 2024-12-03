"""
Cho số nguyên dương không quá 9 chữ số. Hãy làm tròn số N theo quy tắc sau:

Nếu N>10, làm tròn đến số hàng chục gần nhất
Sau đó nếu kết quả lớn hơn 100 thì làm tròn đến số hàng trăm gần nhất
Sau đó nếu kết quả lớn hơn 1000 thì làm trong đến số hàng nghìn gần nhất
Cứ tiếp tục như vậy …
Chú ý: Giá trị 5 sẽ được làm tròn lên.

Input

Dòng đầu ghi số bộ test (không quá 100)

Mỗi bộ test ghi số N trên một dòng (N nguyên dương và không quá 9 chữ số)

Output

Với mỗi test, ghi ra kết quả làm tròn tương ứng trên một dòng.
"""

# Làm tròn từ hàng chục -> trăm -> nghìn    

for t in range(int(input())):

    N = int(input())

    round_level = 10
    while N > round_level:
        # Làm tròn ở cấp bậc hiện tại
        N = ((N + round_level // 2) // round_level) * round_level
        # Tăng cấp bậc
        round_level *= 10
    print(N)