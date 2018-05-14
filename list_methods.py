list1 = [1,2,3,4,5]
list2 = ["red","blue","green"]
list3 = ['a','e','i','o','u']
list4 = [1,'a','blue']

print(list1)
print(list2)
print(list3)
print(list4)
#--------------------------------
#UPDATING LISTS
list1 = [1,2,3,4,5]
print(list1)
print(list1[2]) #print an element from list
print(list1[-2])
list1[2] = 300 #update element in a list
list1[-2] = 400
print(list1)
#--------------------------------
#DELETING LIST OR ELEMENTS IN A LIST
list1 = [1,2,3,4,5]
print(list1)
del list1[2]
print(list1)
del list1[-2]
print(list1)
del list1
print(list1)
#--------------------------------
#OPERATORS
#len - length
#+ - concatenation
#* - repeat
#in - membership
#for - iteration
#LENGTH
list1 = [1,2,3,4,5]
print(len(list1))

#CONCATENATION
list1 = [1,2,3,4,5]
print(list1)
list2 = list1+[11,12,13,14,15]
print(list2)

#REPEAT
list2 = list1*3
print(list2)

#IN
print(3 in list1)
#TRUE
print(30 in list1)
#FALSE

#FOR
for i in list1:
	print(i)
#--------------------------------
INDEXING, SLICING AND MATRICES
#INDEXING
list1 = [1,2,3,4,5]
print(list1(1))
print(list1(-2))

#SLICING
list1[2:]
list1[2:4]

#--------------------------------
#BUILTIN LIST FUNCTIONS AND METHODS
#len(list)
#max(list)
#min(list)
#list(seq) #converts tuple to list
list1 = [1,2,3,4,5]
list2 = ["zzz","aaa","yyy","wxz"]
len(list1)
max(list1)
min(list1)
max(list2) #alphabetical order
min(list2) #alphabetical order


tuple1 = (0,1,2,3,4)
list(tuple1)
#--------------------------------
#LIST METHODS
#list.append(object): appends at the end of list
list1 = [1,2,3,4,5]
list1.append(100)
print(list1)
#-------------
#list.insert(index, object)
list1 = [1,2,3,4,5]
list1.insert(0,300)
print(list1)
#-------------
#list.extend(obj)
list1 = [1,2,3,4,5]
list2 = [60,70,80,90]
list1.extend(list2)
print(list1)
#concatenation: similar to list.extend(obj)
list2 = list1+[11,12,13,14,15]
#-------------
#list.pop(index) #removes last element
list1 = [1,2,3,4,5]
list1.pop() #removes last element by default
print(list1)

list1.pop(3) #removes element at index 3
print(list1)
#-------------
#list.remove(object)
list1 = [10,20,30,40,50]
list1.remove(20) #deletes specific value
#-------------
#list.reverse()
list1 = [10,20,30,40,50]
list1.reverse()
print(list1)
#-------------
list1 = [20,50,30,10,40]
list1.sort()
print(list1)
#--------------------------------



















