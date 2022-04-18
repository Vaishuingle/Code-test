#write a python script to generate and print a dictionary that contains a number (between 1 and n) in the form of (x, x*x).

n=int(input("Enter the max number :"))
lst=[]
d={}
for i in range(1,n+1):
    lst.append(i)
    for k in range(len(lst)):
        d.setdefault(lst[k],lst[k]**2)
print(d)