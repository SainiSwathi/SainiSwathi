#1. Write a python program to get only unique items from two sets
#Input:
#Set1=(10,20,30,40,50)
#Set2=(30,40,50,60,70)
#Output=(70,40,10,50,20,60,30)

Set1={10,20,30,40,50}
Set2={30,40,50,60,70}
unique_items = Set1.union(Set2)
print(unique_items)
