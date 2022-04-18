lst = [4, 5, 1, 1, 2, 7, 8, 9, 2, 1, 3, 2, 3, 2, 6, 8, 7, 9, 10]

dict1 ={value:lst.count(value) for value in lst}
res = {}
for i, j in dict1.items():
    if i not in res:
        res.setdefault(i, j)
print(res)

print("-" * 40)

sample_list = [4, 5, 1, 1, 2, 7, 8, 9, 2, 1, 3, 2, 3, 2, 6, 8, 7, 9, 10]
N = int(input("Enter number: "))
count = sample_list.count(N)
print(count)
