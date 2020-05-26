import math

def find_sum(num):
	l = []
	i = 2
	s = 0
	while (i <= math.sqrt(num)):
		if (num % i == 0):
			if (num / i == i):
				s += i
			else:
				s += i
				s += num / i
		i += 1
	return s + 1
	
	
l = []
i = 2
c = 0
while (c != 10):
	s = find_sum(i)
	ns = find_sum(s)
		
	if (ns == i):
		if (i != s):
			l.append((i, int(s)))
			c += 1
	i += 1
	for k in l:
		if (i == k[0]) or (i == k[1]):
			i += 1
for pair in l:
	print (pair)


