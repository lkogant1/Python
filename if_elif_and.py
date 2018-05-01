#three numbers distinct
#vs
#numbers not distinct
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a>b and a>c):
	print("a is greater than b and c")
elif(b>a and b>c):
	print("b is greater than a and c")
elif(c>a and c>b):
	print("c is greater than a and b")
else:
	print("some values are equal")

'''
cases
30 20 10 -> case 1 -> if
10 30 20 -> case 2 -> elif
10 20 30 -> case 3 -> elif

30 30 10 -> else
30 10 30 -> else
10 30 30 -> else
30 30 30 -> else 

'''
