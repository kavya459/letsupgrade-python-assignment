Day6 assignment
Assignment 1:
list1= [1,2,3,4,5]
list2= ["a","b","c","d","e"]
len1= min(len(list1),len(list2))
dict1= {}
print(type(dict1))
dict1= {list1[each]:list2[each] for each in range(4)}
print(dict1,type(dict1))