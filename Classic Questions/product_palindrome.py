
def palindrome():
    p_list = []
    ij_list = []

    for i in range(100, 1000):
        for j in range(100, 1000):
            p = i * j
            p_list.append(p)
            p = str(p)
            ij_list.append((i, j))
            for n in range(len(p) // 2):
                if p[n] != p[len(p) - n - 1]:
                    p_list.pop()
                    ij_list.pop()
                    break
    m = max(p_list)
    print(m)
    for (x, y) in ij_list:
        if x * y == m:
            print((x, y))


print(palindrome())
