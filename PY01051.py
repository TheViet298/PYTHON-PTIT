
def reverse_n(num):
    reversed_n = int(str(num)[::-1])
    if not (reversed_n):
        return 'NO'
    return 'YES'

for t in range(int(input())):

    n = input()
    res = " "
    if reverse_n(n):
        for i in n:
            res += int(i)
    print(res)