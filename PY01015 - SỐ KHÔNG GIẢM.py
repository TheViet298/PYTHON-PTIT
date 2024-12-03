
for i in range(int(input())):

    n = input()
    check = True
    for i in range(len(n) -1):
        if n[i] > n[i + 1]:
            check = False
            break
    if check:
        print("YES")
    else: print("NO")