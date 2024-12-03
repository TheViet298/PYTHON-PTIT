a = set()
max_val = int(1e18)

for i in range(65):
    n2 = 1 << i
    if n2 > max_val: break
    for j in range(40):
        n3 = 3**j
        if n2 * n3 > max_val: break
        for k in range(28):
            n5 = 5**k
            if n2 * n3 * n5 > max_val: break
            a.add(n2 * n3 * n5)

a = sorted(a)

def bs(l, r, v):
    if l > r: return 'Not in sequence'
    mid = (l + r) >> 1
    if a[mid] == v: return mid + 1
    if a[mid] < v: return bs(mid + 1, r, v)
    return bs(l, mid - 1, v)

for t in range(int(input())):
    print(bs(0, len(a) - 1, int(input())))
