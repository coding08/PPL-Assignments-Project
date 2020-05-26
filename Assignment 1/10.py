
print("Enter the first number and the common ratio")
a = int(input("First number: "))
r = int(input("Common ratio: "))
c = 1
l = []
print("The first 10 numbers of GS are:")
while c < 10:
	l.append(a * (r**(c-1)))
	c += 1
print(l)	
