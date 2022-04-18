

# Write a python program to find common items from two lists.


lst = [9, 8, 7, 6, 5]
lst1 = [7, 4]

commn= set(lst).intersection(set(lst1))
print(commn)