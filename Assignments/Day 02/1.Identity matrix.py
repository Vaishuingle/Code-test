n = int(input("Enter a Number : "))
matrix = [list(range(1 + n * i, 1 + n * (i+1))) for i in range(n)]
print ("The matrix of {} * {} : ".format(n, n))
for m in matrix:
    print(m)
