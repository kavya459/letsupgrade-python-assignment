Assignment-1 [0,1,2,10,5,6,2,0,1,3,0,5,6,0,4] sort increasing order but all  zeros should be at right side
list1= [0,1,2,10,5,6,2,0,1,3,0,5,6,0,4]
print(list1)
list1.sort()
print(list1)
for each in range(4)
  list1.append[0]
list1.remove(0)


   
Assignment -2: merge two sorted list but only use one loop
list1= [10,20,40,60,70,80]
list2= [5,15,25,35,45,60]
print(list1)
print(list2)
list3= list1+list2
print(list3)
length= len(list3)
print(length)
for j in range(11):
  if list3[j] > list3[j+1]:
    temp= list3
    list3[j+1]= list3[j]
    list3[j]= temp
    j= j+1
  j= j+1
print(list3)
  
 