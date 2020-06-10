'''
	EduMedM
	edumedm@gmail.com
	Start: 04-23-2020
	Finished project: 06-09-2020
'''
import sys
from os import system, name
from random import randint, choice
from time import sleep
from math import ceil

#------------ global scope ------------#

#open the topics and help_messages files to store them in arrays
try:
	with open("topics.txt") as t:
		topics = t.read().split()
except FileNotFoundError:
	print("\n\n\tERROR\n\ttopics.txt not Found")
	sys.exit()

try:
	with open("help_messages.txt") as f:
		help_messages = f.read().split('-')
except FileNotFoundError:
	print("\n\n\tERROR\n\thelp_messages.txt not Found")
	sys.exit()

topics_index = 0
help_count = 0


HANGMAN = ['''
                   [=]----[=]
                    |      |
                           |
                           |
                           |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                           |
                           |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                   /       |
                           |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                   /|      |
                           |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                   /|\     |
                           |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                   /|\     |
                   /       |
                           |
                        [=====]''','''
                   [=]----[=]
                    |      |
                    O      |
                   /|\     |
                   / \     |
                           |
                        [=====]''']
  
#------------ functions ------------#

def clear():

	if (name == 'nt'): #for Windows
		_ = system('cls')

	else:              #for Linux or Mac (name is 'posix')
		 _ = system('clear')

def menu():

	while True:

		global topics

		topics.sort()

		print("\n\n\tEnter an option (enter the name or the number): ")
		print("\n\t1.- Play.")
		print("\n\t2.- Add words to a topic.")
		print("\n\t3.- Add a new topic.")
		print("\n\t4.- Display topic words.")
		print("\n\t5.- Exit.")

		option = input("\n\tOption: ").lower()

		if (option.startswith('p') or option == '1'):
			return chooseATopic()

		elif(option.startswith('add w') or option == '2'):
			addNewWordsToATopic()

		elif(option.startswith('add a n') or option.startswith('add n') or option == '3'):
			addTopic()

		elif(option.startswith('d') or option == '4'):
			displayTopicWords()

		elif(option.startswith('e') or option == '5'):
			clear()
			sys.exit()

		else:
			print("\n\n\tChoose a correct option. ",end='')
			sleep(1)
			
		clear()

def chooseATopic():

	global topics_index

	while True:

		clear()
		print("\n\n\tEnter an option (enter the name or the number): ")

		print("\n\t 1 .- Random")

		for i,element in enumerate(topics):
			print("\n\t",i+2,".-",element)

		file_name = input("\n\n\t--->  ").lower()

		if(file_name == 'random' or file_name == '1'):
			file_name = choice(topics)

		elif(file_name in '1234567890' or file_name not in topics):

			try:
				file_name = topics[int(file_name)-2]

			except:
				print("\n\n\t404-NOT-FOUND")
				input("\n\n\tPress Enter to continue...")

		if(file_name in topics):

			with open(file_name + ".txt",'r') as f:

				words = f.read().split()
			topics_index = topics.index(file_name)

			return words

def addWords(file_name):

	cont = 0

	try:
		with open(file_name + ".txt",'a+') as f:

			n = int(input("\n\tHow many words do you want to enter?: "))

			#loop to keep function until the user enters 'exit' or 'n' words
			while True:
							
				clear()
								
				for i in range(n):

					f.seek(0)
					words = f.read().split()

					print("\n\tEnter \"exit\" to return to the menu.")
					print("\n\t",cont+1,".- ",end='')
							
					entered_word = input().lower()

					if(entered_word != 'exit'):
										
						if(' ' not in entered_word):
											
							if(entered_word in words):
								print("\n\tThe word entered already exists")
								input("\n\n\tPress Enter to continue...")
								clear()
											
							else:
								f.seek(0)
								f.write(entered_word)
								print(end=' ',file=f)
								cont+=1
										
						else:
							print("\n\tEnter only one word")
							input("\n\n\tPress Enter to continue...")
									
					else: break

					if(cont == n): break
									
					clear()
								
				if(entered_word == 'exit' or cont == n): break

	except:
		print("\n\n\tERROR")
		input("\n\n\tPress Enter to continue...")

def addNewWordsToATopic():

	clear()

	print("\n\n\tSelect a topic: ")
	print("\n\tEnter \"exit\" to return to the menu.")

	for element in topics:
		print("\n\t",element)

	file_name = input("\n\n\t--->  ").lower()

	if(file_name != 'exit'):
		if(file_name in topics):

			addWords(file_name)

		else:
			print("\n\n\t404-NOT-FOUND")
			input("\n\n\tPress Enter to continue...")

	else: pass

def addTopic():

	clear()

	global topics
	flag = True

	while flag:

		print("\n\n\tTopics already exist: ")
		for element in topics:
			print("\n\t",element)

		print("\n\n\tEnter the new topic name: ")
		print("\n\tEnter \"exit\" to return to the menu.")
		file_name = input("\n\n\t--->  ").lower()

		clear()

		if(file_name != 'exit'):

			if(file_name not in topics):

				if(' ' not in file_name):

					try:

						addWords(file_name)

						with open("topics.txt",'a+') as f:

							print(file_name,end=' ',file=f)
							f.seek(0)
							topics = f.read().split()

						flag = False

					except:

						print("\n\n\tERROR")
						input("\n\n\tPress Enter to continue...")
						break

				else:
					print("\n\tEnter only one word")
					input("\n\n\tPress Enter to continue...")

			else:
				print("\n\tThe topic entered already exists")
				input("\n\n\tPress Enter to continue...")
				clear()

		else: break

def displayTopicWords():

	clear()
	print("\n\n\tSelect a topic: ")
	print("\n\tEnter \"exit\" to return to the menu.")

	for element in topics:
		print("\n\t",element)

	file_name = input("\n\n\t--->  ").lower()

	clear()

	if(file_name != 'exit'):

		if(file_name in topics):

			print("\n\n\t",file_name.upper(),"\n")

			with open(file_name + ".txt",'r') as f:
				
				words_display = f.read().split()
				words_display.sort()
				
			for element in words_display:
				print("\t",element)

			input("\n\n\tPress Enter to continue...")

		else:
			print("\n\n\t404-NOT-FOUND")
			input("\n\n\tPress Enter to continue...")

	else: pass

def getRandomWord(words_list):

	return choice(words_list)

def display(missed_letters, blanks):

	print("\n\n\t   ***** HANGMAN /",topics[topics_index].upper(), "*****\n\n")

	print(HANGMAN[len(missed_letters)])
	print("\n\n")
	print("\t\t",end='')

	for item in blanks:
		print(item, end=' ')

	print("\n\n\t\tMissed words: ", end=' ')

	for item in missed_letters:
		print(item, end=' ')

	print("\n\n\t\tEnter 'help' if you want a random letter.")
	print('\n\t\tEnter a letter: ',end='')

def getUserLetter(entered_letters, word, display, *args):
	
	while(True):

		#display() is inside getUserLetter() to clear the error text in each iteration.
		display(*args)

		guess_letter = input().lower()

		if(guess_letter == 'help'):
			print("\n\t\t",choice(help_messages))
			sleep(2.3)
			return helpRadomLetter(entered_letters, word)

		else:

			if(len(guess_letter) != 1):
				print("\n\t\tEnter a sigle letter: ", end='')
				sleep(0.8)

			elif(guess_letter not in 'abcdefghijklmnopqrstuvwxyz'):
				clear()

			elif(guess_letter in entered_letters):
				print("\n\t\tEnter a letter that has not yet been entered: ", end='')
				sleep(1)

			else: return guess_letter

		clear()

def helpRadomLetter(entered_letters, word):

	help_letter = ''
	leftover_letters = []
	global help_count

	for l in word:
		if ((l not in entered_letters) and (l not in leftover_letters)):

			leftover_letters.append(l)

	help_letter = choice(leftover_letters)

	help_count += 1

	return help_letter

def playAgain():

	print("\n\n\t\tDo you want to play again?:  ",end='')

	return input().lower().startswith('y')

def main():

	clear()

	while(True):

		global help_count
		help_count = 0
		word = getRandomWord(menu())
		blanks = '_' * len(word)
		missed_letters = []
		correct_letters = []
		clear()

		while(len(missed_letters) < 6):

			letter = getUserLetter(correct_letters + missed_letters, word, display, missed_letters, blanks)

			if(letter in(word)):
				
				correct_letters.append(letter)

				for i in range(len(word)):
					if(word[i] == letter):
						blanks = blanks[:i] + letter + blanks[i+1:]

			else: missed_letters.append(letter)

			clear()

			if(blanks == word):

				print("\n\t\t",word.center(24))

				if(help_count == 0):
					print("\n\n\t\tWell done, you won!")

				elif(help_count == len(correct_letters)):
					print("\n\n\t\tYou did nothing...")

				elif(help_count < ceil(len(word)/2)):
					print("\n\n\t\tWell done! You won, but with a little help.")

				elif(help_count >= ceil(len(word)/2)):
					print("\n\n\t\tYou did it, but with a lot of help.")

				break

			elif(len(missed_letters) == 6):
				print(HANGMAN[6])
				print("\n\n\t\tYou lost!!!")
				print("\n\t\tThe word was: ",word)
				break

		if(not(playAgain())): exit()

		else: clear()

main()