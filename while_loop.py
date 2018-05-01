#loops
#infinite loop: condition always true

while(1<5):
	print("One")


#infinite loop: i value is always 1 and thus the expression always holds true
i=1
while(i<5):
	print(i)

#print 1,2,3,4 => 4 numbers
i=1
while(i<5):
	print(i)
	i=i+1

#prints 0,1,2,3,4 => 5 numbers
i=0
while(i<5):
	print(i)
	i=i+1

#prints 0,1,2,3,4,5 => 6 numbers
i=0
while(i<=5):
	print(i)
	i=i+1

#prints 1,2,3,4,5 => 5 numbers
i=1
while(i<=5):
	print(i)
	i=i+1

#i=i+1 is a common statement 
# i value does n't increment
# i value remains 1 and the expression always holds true, as a result the loop runs infinitely
i=1
while(i<=5):
	print(i)
i=i+1


