# Write a python code to remove duplicates (values) from dictionary

dic1={'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50, 'E': 50, 'F': 60}

temp=[]
res = dict()
for i, j in dic1.items():
    if j not in temp:
        temp.append(j)
        res[i]=j
print(res)