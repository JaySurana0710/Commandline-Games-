from random import randint
import os
import time
options=['ROCK','PAPER','SCISSOR','LIZARD',"SPOCK"]

while True:
	computer=randint(0,4)
	player=int(input('1.ROCK\n2.PAPER\n3.SCISSOR\n4.LIZARD\n5.SPOCK\n'))-1
	
	
	if options[player]==options[computer]:
		print('TIE')
	elif options[player]=='ROCK':
		if options[computer]=='SCISSOR':	print('YOU WIN: ',options[player],' SMASHES ',options[computer])
		elif options[computer]=='LIZARD':	print('YOU WIN: ',options[player],' CRUSHES ',options[computer])
		elif options[computer]=='SPOCK':	print('COMPUTER WINS: ', options[computer],' VAPOURIZES ',oprions[player])
		else:	print('COMPUTER WINS: ',options[computer],' COVERS ',options[player])
	elif options[player]=='PAPER':
		if options[computer]=='ROCK':	print('YOU WIN: ',options[player],' COVERS ',options[computer])
		elif options[computer]=='SPOCK':	print('YOU WIN: ',options[player],' DISPROVES ',options[player])	
		elif options[computer]=='LIZARD':	print('COMPUTER WINS: ',options[computer], ' EATS ',options[player])
		else:	print('COMPUTER WINS: ',options[computer],' CUTS ',options[player])
	elif options[player]=='SCISSOR':
		if options[computer]=='PAPER':	print('YOU WIN: ',options[player],' CUTS ',options[computer])
		elif options[computer]=='SPOCK':	print('COMPUTER WINS: ',options[computer],' SMASHES ',options[player])
		elif options[computer]=='LIZARD':	print('YOU WIN: ',options[player],' DECAPITATE ',options[computer])
		else:	print('COMPUTER WINS: ',options[computer],' SMASHES ',options[player])
	elif options[player]=='LIZARD':
		if options[computer]=='PAPER':	print('YOU WIN: ',options[player],' EATS ',options[computer])
		elif options[computer]=='SPOCK':	print('YOU WIN: ',options[player],' POISONS ',options[computer])
		elif options[computer]=='SCISSOR':	print('COMPUTER WINS: ',options[computer],' DECAPITATE ',options[player])
		else:	print('COMPUTER WINS: ',options[computer],' CRUSHES ',options[player])
	elif options[player]=='SPOCK':	
		if options[computer]=='ROCK':	print('YOU WIN: ',options[player],' VAPOURISES ',options[computer])
		elif options[computer]=='SCISSOR':	print('YOU WIN: ',options[player],' SMASHES ',options[computer])
		elif options[computer]=='LIZARD':	print('COMPUTER WINS: ',options[computer],' POISONS ',options[player])
		else:	print('COMPUTER WINS: ',options[computer],' DISPROVES ',options[player])
	else: 
		print('WRONG OPTION')
		continue
			
	time.sleep(2)
	os.system('cls')

	if player=='f':	break