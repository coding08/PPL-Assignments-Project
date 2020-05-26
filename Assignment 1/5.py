book = {i for i in range(1,26)}

def missing_pages(t):
  return book - t

  t = set()
t = {1,3,4,5,6,7,11,14,24,21,12,18}
print(missing_pages(t))
