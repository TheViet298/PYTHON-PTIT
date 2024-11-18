
"""
Input:

Dòng đầu chứa số nguyên dương n là số lời chúc Tí ghi được;

n dòng tiếp theo, mỗi dòng chứa một xâu ký tự S là một lời chúc.

n, S thỏa mãn ràng buộc: 1 ≤ n ≤ 10^4; Các lời chúc S có độ dài không quá 30 ký tự gồm các chữ cái la tinh IN HOA ‘A’…’Z’ và dấu cách.

Output:

Một số nguyên dương duy nhất là số lời chúc khác nhau.
"""
# Đọc số nguyên dương n
n = int(input().strip())

unique_set = set()

# Đọc n lời chúc và thêm vào tập hợp
for _ in range(n):
    greeting = input().strip()
    unique_set.add(greeting)

# In ra số lượng lời chúc khác nhau
print(len(unique_set))
