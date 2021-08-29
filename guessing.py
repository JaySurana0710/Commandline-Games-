import os
import random
import time

while True:
	os.system('cls')
	number=random.randint(1,9)
	tries=3
	name=input('Hi! Whats your name?')
	print('Hi ',name,'This is a guessing game! ')
	while True:
		os.system('cls')
		if tries==0:
			print('You had three chances')
			time.sleep(1)
			break
		entered_number=int(input('Enter a number between 1 to 9\n'))
		if entered_number-number>0:
			print('Your guess is High')
			time.sleep(1)
			tries-=1
			continue
		elif entered_number-number<0:
			print('Your guess is Low')
			time.sleep(1)
			tries-=1
			continue
		elif entered_number==number:
			print('You guessed it!')
			break
		
		

	choice=input('Play again? press y\n')
	if choice=='y' or choice=='Y':
		continue
	else:
		print('Bye!')
		break