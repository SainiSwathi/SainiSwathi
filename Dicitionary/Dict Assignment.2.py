#2.Write a python script to concatenate the following dictinories to create a new one.
#Sample Dictionary:
#dic1={1:10,2:20}
#dic2={3:30,4:40}
#dic3={5:50,6:60}
#Expected Result:{1:10,2:20,3:30,4:40,5:50,6:60}


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {**dic1, **dic2, **dic3}
print("New Dictionary:", new_dict)
