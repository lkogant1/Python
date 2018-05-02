#reverse number
n = int(input("enter number: "))
r = 0
while(n>0):
	d = n%10
	r = r*10+d
	n = int(n/10)
print("reverse", r)