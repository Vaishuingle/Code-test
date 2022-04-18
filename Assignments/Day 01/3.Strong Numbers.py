
n = int(input("Enter the number: "))
strong = n
sum = 0
while(n>0):
    r = n % 10
    fact = 1
    for i in range(1, r+1):
        fact = fact * i
        sum = sum + fact
        n = n // 10
if(strong==sum):
    print("Strong Number")
else:
    print("Not a Strong Number")





print("-" * 40)

factorial = [1, 1, 2, 6, 24, 120,
             720, 5040, 40320, 362880]


def isStrong(N):

    num = str(N)

    sum = 0
    for i in range(len(num)):
        sum += factorial[ord(num[i]) -
                         ord('0')]

    if sum == N:
        return True
    else:
        return False
def printStrongNumbers(N):

    for i in range(1, N + 1):

        if (isStrong(i)):
            print(i, end=" ")

if __name__ == "__main__":

    N = 2000
    printStrongNumbers(N)
