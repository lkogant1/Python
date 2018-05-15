tup1 = (10,20,30,40,50)
tup2 = ('aaa','bbb','ccc')
tup3 = ('xyz','yyy','zzz')
tup4 = (111,'kittie',20000)

print(tup1)
print(tup2)
print(tup3)
print(tup4)
#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#ACCESSING VALUES IN TUPLES
print(tup1[0])
print(tup1[2:])
print(tup1[2:4])

#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#UPDATING VALUES IN TUPLES
#NOT POSSIBLE
#TypeError: 'tuple' object does not support item assignment
tup1 = (10,20,30,40,50)
tup2 = ('aaa','bbb','ccc')
tup1[2] = 200
print(tup1)

#CONCAT TWO TUPLES
tup3 = tup1+tup2
print(tup3)
#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#DELETING TUPLE ELEMENTS
#NOT POSSIBLE TO DELETE TUPLE ELEMENTS BUT POSSIBLE TO DELETE ENTIRE TUPLE
tup1 = (10,20,30,40,50)
print(tup1)
del tup1[2]
print(tup1)
#TypeError: 'tuple' object doesn't support item deletion
#--------------------------
tup1 = (10,20,30,40,50)
del tup1
print(tup1)
#NameError: name 'tup1' is not defined
#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#OPERATORS
#len - length
#max - maximum value
#min - minimum value
#in - membership
#for - iteration

tup1 = (10,20,30,40,50)
len(tup1) #length of tuple
max(tup1) #maximum value of tuple
min(tup1) #minimum value of tuple
print(tup1+tup2) #concatenation
print(tup1*3) #repetition
10 in tup1 #membership
100 in tup1 #membership
for i in tup1: #for
	print(i)

#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#INDEXING, SLICING 
tup1 = [10,20,30,40,50]
print(tup1)
print(tup1[2])
print(tup1[-2])
print(tup1[2:])
print(tup1[2:4])

#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------
#BUILT-IN TUPLE METHODS
list1 = [1,2,3,4,5]
tup1 = tuple(list1)
print(tup1)

#--------------------------#--------------------------
#--------------------------#--------------------------
#--------------------------#--------------------------





