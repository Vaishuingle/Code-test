
# Write a code to get the key of a minimum value from a dictionary.


dic1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 4: 40}
key_value = min(dic1, key=dic1.get)
print(f"minimum key_value is:{key_value}")


print("-" * 40)

test_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 4: 40 }
print(min(test_dict, key = test_dict.get))