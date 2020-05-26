import math

def find_factors(num):
	l = []
	i = 1
	while i <= math.sqrt(num):
		if num % i == 0:
			if num / i == i:
				l.append(i)
			else:
				l.append(i)
				l.append(num / i)
		i += 1
	return l
	

i = 1
c = 0
while c != 10:
	s = 0
	l = find_factors(i)
	for k in l:
		s += 1.0 / k
			
	res = len(l) / s
	if round(res, 6).is_integer():
		print (i)
		c += 1
	i += 1
