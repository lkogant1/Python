#bubble_sort
a = [34,56,12,77,11,66]
for i in (range(len(a)-1)):
	for j in (range(len(a)-1-i)):
		if(a[j]>a[j+1]):
			t = a[j]
			a[j] = a[j+1];
			a[j+1] = t;
			
print(a)
