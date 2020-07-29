Day7 
Assignment 1:
list1= {21:"ftp",22:"ssh",23:"telnet",80:"http"}
print(list1)
port1= list1.keys()
print(port1)
port2= list1.values()
print(port2)
res= (dict(zip(port2,port1)))
print(res)


 assignment 2:
list2= []
list1= [(1,2),(3,4),(5,6),(4,5)]
print(list1)
for each in list1:
  list2.append(each[0]+each[1])
print(list2)

Assignment 3:

list1= [(1,2,3),[1,2,0],['a','hit','less']]
print(list1)
list2= []
for each in list1:
    list2.append(each[0])
    list2.append(each[1])
    list2.append(each[2])
print(list2)
list2.remove(0)
print(list2)
  
