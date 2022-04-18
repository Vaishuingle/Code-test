first = 1
last = 500
while first <= last:
    res = 0
    temp = first
    noofdigit = 0

    while temp > 0:
        temp = int(temp/10)
        noofdigit =noofdigit + 1
        num = first
    while num > 0:
        rem = num % 10
        pow = 1
        i = 0
        while i < noofdigit:
            pow = pow * rem
            i = i + 1
        res = res + pow
        num = int(num/10)
    if res == first:
            print(res)
    first = first + 1