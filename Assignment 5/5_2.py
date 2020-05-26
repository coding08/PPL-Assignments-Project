def ask():
  while True:
    try:
      r = input("Enter a number\n")
      n = int(r)
    except:
      print('Please try again!\n')
      continue
    else:
      break
    finally:
      print('Finally : I will always run!')
  print('Your number squared is: ')
  print(n**2)
ask()