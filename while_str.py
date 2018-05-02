#strong number or not
#sum of each digit factorial is equal to given number
n = int(input("enter #: "))
t = n
s = 0
while(n>0):
	d = n%10
	f = 1
	i = 1
	while(i<=d):
		f = f*i
		i = i+1
	s = s+f
	n = int(n/10)

if(s == t):
	print("strong #")
else:
	print("not a strong #")