#nested if
name=input("name: ")
python=int(input("python score: "))
java=int(input("java score: "))
c=int(input("c score: "))

total = python+java+c
avg = total/3

if(python>=50 and java>=50 and c>=50):
	
	result="Pass"
	if(avg>=90):
		grade="A"
	elif(avg>=80):
		grade="B"
	elif(avg>=70):
		grade="C"
	elif(avg>=60):
		grade="D"
	elif(avg>=50):
		grade="E"
		
else:
	result="Fail"
print("Name:", name)
print("Total:", total)
print("Avg: ", avg)
print("Result: ",result)
print("Grade: ",grade)

'''
if(python>=50 and java>=50 and c>=50):
	result="Pass"
	if(avg>=50 and avg<=59):
		grade="E"
	elif(avg>=60 and avg<=69):
		grade="D"
	elif(avg>=70 and avg<=79):
		grade="C"
	elif(avg>=80 and avg<=89):
		grade="B"
	elif(avg>=90 and avg<=100):
		grade="A"
else:
	result="Fail"

print("Name: ", name)
print("Total: ", total)
print("Avg: ", avg)
print("Result: ",result)
print("Grade: ",grade)

'''



