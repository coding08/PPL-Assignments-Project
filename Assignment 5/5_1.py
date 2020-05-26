import sys
def f():
	try:
		fh = open(file_name, 'r')
	except:
		print('cannot open this file')
		raise
	else:
		text = fh.readlines()
		fh.close()


file_name = sys.argv[1]
text = []

try:
	f()
except IOError as e:
	print(e)

if text:
	print(text[100])
