#4.Write a python program to get the key, value and item in a dictionary.
#Input: input_dict={1:10,2:20,3:None,4:40,5:None,6:60}


input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}

keys = input_dict.keys()
print("Keys:", keys)

values = input_dict.values()
print("Values:", values)

items = input_dict.items()
print("Items:", items)

for key, value in input_dict.items():
    print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
for key, value in input_dict.items():
    if value is not None:
        print(f"Key: {key}, Value: {value}, Item: ({key}, {value})")
