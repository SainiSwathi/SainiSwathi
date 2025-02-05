#1.Write a python program and calculate the mean of the below dictionary.
#test_dict={"A":6,"B":9,"C":5,"D":7,"E":4}
#Output:6.2

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
sum_values = sum(test_dict.values())
mean_value = sum_values / len(test_dict)
print("Mean:", round(mean_value, 1))
