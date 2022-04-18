
# Write a python program to count number of lists in  a list of lists.


lst=[[5, 6, 7],[1,2,3],[8,9,0],[4, 4, 4],[0, 1, 2]]
count=0
for i in lst:
    type(i)==type([])
    count+=1
print(count)

print("-" * 40)

def list_count(lst):
    return len(lst)
print(list_count(lst))