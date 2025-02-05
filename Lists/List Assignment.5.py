#5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] 

#Traverse the said list in reverse order: 

#black 

#white 

#green

#red

original_list = ['red', 'green', 'white', 'black']
for i in range(len(original_list) - 1, -1, -1):
    print(f"Index: {i}, Element: {original_list[i]}")
    print("\nTraverse the said list in reverse order:")
for element in reversed(original_list):
    print(element)
