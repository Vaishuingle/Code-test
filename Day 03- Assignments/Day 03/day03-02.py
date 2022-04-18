#2.Write a python code Script to check whether a given key already exists in a dictionary

d={1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def is_presented(n):

    if n in d:
        print("Key is already exists")
    else:
        print("Key is not exists")

is_presented(6)
is_presented(11)