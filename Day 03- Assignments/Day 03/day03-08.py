#Remove all the occurrences of a specific item from a list


item=[1, 2, 3, 4, 6, 7, 2, 1, 5, 6, 7, 8, 9, 10]
occurance=2
print("Remove all the occurrences of a specific item from a list")
for i in item:
    if i!=occurance:
        print(i)
