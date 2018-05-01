#if elif loop
#find if any two values are equal
#use logical operator "or"
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if(a==b or b==c or c==a):
	print("any two values are equal")
else:
	print("none of the values are equal")