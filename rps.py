from random import randint
import os
import time
options=['ROCK','PAPER','SCISSOR']



while True:
	computer=randint(0,2)
	player=int(input('1.ROCK\n2.PAPER\n3.SCISSOR\n'))-1
	if options[player]==options[computer]:
		print('TIE')
	elif options[player]=='ROCK':
		if options[computer]=='SCISSOR':	print('YOU WIN: ',options[player],' SMASHES ',options[computer])
		else:	print('COMPUTER WINS: ',options[computer],' COVERS ',options[player])
	elif options[player]=='PAPER':
		if options[computer]=='ROCK':	print('YOU WIN: ',options[player],' COVERS ',options[computer])
		else:	print('COMPUTER WINS: ',options[computer],' CUTS ',options[player])
	elif options[player]=='SCISSOR':
		if options[computer]=='PAPER':	print('YOU WIN: ',options[player],' CUTS ',options[computer])
		else:	print('COMPUTER WINS: ',options[computer],' SMASHES ',options[player])
	time.sleep(2)
	os.system('cls')
	if player=='f':	break