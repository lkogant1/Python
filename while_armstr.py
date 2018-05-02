#armstrong number or not
#sum of each digit cubes is equal to the given number
#eg: 153
x
n = int(input("number: "))
t = n
s = 0
while(n>0):
	d = n%10
	s = s+(d*d*d)
	n = int(n/10)
if(s == t):
	print("Armstrong number")
else:
	print("Not an Armstrong number")