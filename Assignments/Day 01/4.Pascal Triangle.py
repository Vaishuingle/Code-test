
n = 6
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")

    m = 1
    for j in range(1, i+1):
        print(m, ' ', sep=' ', end=' ')
        m = m * ( i - j) // j
    print()