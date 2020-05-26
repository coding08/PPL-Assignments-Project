import random
while (1):
    ch = input("Enter 'r' to roll dice or anything else to quit: ")
    if ch == 'r':
        t = random.choice([1, 2, 3, 4, 5, 6])
        print('The dice shows number - {}'.format(t))
    else:
        break
