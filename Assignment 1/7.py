
st = int(input("Enter the start range: "))
end = int(input("Enter the end range: "))
l = []
for i in range(st, end):
	s = 0
	t = i
	while t > 0:
		r = t % 10
		s += r**3
		t = t // 10
	if (s == i):
		l.append(i)
print (l)
