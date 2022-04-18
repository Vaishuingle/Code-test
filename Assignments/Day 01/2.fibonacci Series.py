# def fibonacci (n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(8))

nterms = int(input("enter the sum of terms: "))
n1, n2 = 0, 1
count = 0
if nterms == 1:
    print(n1)
else:
    print("Fibonacci series: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2

        n1 = n2
        n2 = nth
        count += 1
