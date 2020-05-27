'''
	EduMedM
	Start: 23-04-2020

'''

from os import system, name

from random import randint, choice

from time import sleep

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
  

words = {'animals':'''caterpillar butterfly grasshopper mantis scorpion beetle ant 
		mosquito spider fly bee wasp eagle owl pigeon canary parrot chicken 
		pelican duck penguin flamingo fish swordfish shark cobra alligator 
		turtle iguana lizard salamander frog koala armadillo kangaroo bat rat
		mouse squirrel rabbit hippopotamus llama rhino elephant zebra pony horse
		sheep donkey giraffe cow camel leopard tiger lion cat kitten fox whale
		otter seal lobster crab dolphin monkey gorilla orangutan panda bear polarbear 
		grizzlybeardog wolf hyena'''.split(),
		'food':'''broccoli lettuce spinach celery beans corn asparagus 
		cabbage tomato cucumber eggplant pepper potato garlic pumpkin zucchini mushrooms
		onion carrot beet grapes apple coconut pineapple mango papaya orange grapefruit
		lemon lime strawberry raspberries blueberries blackberries pear cherries banana
		watermelon peanut almond avocado peach beef steak pork sausage bacon ham eggs
		mustard hotdog hamburger spaghetti salad butter cookie taco biscuit pizza toast
		coffee icecream chocolat cake'''.split()}

def clear():

	if (name == 'nt'): #for windows
		_ = system('cls')

	else:              #for Linux or Mac (name is 'posix')
		 _ = system('clear')

def chooseATopic():

	print("\n\n\tEnter an option (enter the name or number): ")
	print("\t\n\t1.- Random Topic.")
	print("\t\n\t2.- Animals.")
	print("\t\n\t3.- Food.")

	option = input("\n\tOption: ").lower()

	if (option.startswith('r') or option == '1'):
		return choice(['animals','food'])

	elif(option.startswith('a') or option == '2'):
		return 'animals'

	elif(option.startswith('f') or option == '3'):
		return 'food'

	else:
		print("\n\n\tChoose a correct option. ",end='')
		sleep(1)
		clear()

def getRandomWord(words_key):
	
	word_list = words[words_key]
	word_index = randint(0, len(word_list) - 1)

	return word_list[word_index]

def display(mw,bk,word):
	
	if (word in words['animals']):
		print("\n\n\t***** HANGMAN / Animals *****\n\n")
	elif(word in words['food']):
		print("\n\n\t***** HANGMAN / Food *****\n\n")

	print(HANGMAN[len(mw)])
	print("\n\n")
	print("\t\t",end='')

	for item in bk:
		print(item, end=' ')

	print("\n\n\t\tMissed words: ", end=' ')

	for item in mw:
		print(item, end=' ')

	print('\n\n\t\tEnter a letter: ',end='')

def getUserLetter(entered_letters):
	
	while(True):

		guess_letter = input()
		guess_letter = guess_letter.lower()

		if(len(guess_letter) != 1):
			print("\n\t\tEnter a sigle letter: ", end='')

		elif(guess_letter not in 'abcdefghijklmnopqrstuvwxyz'):
			print("\n\t\tEnter a letter: ", end='')

		elif(guess_letter in entered_letters):
			print("\n\t\tEnter a letter that has not yet been entered: ", end='')

		else:
			return guess_letter

def playAgain():
	
	print("\n\n\t\tDo you want to play again?:  ",end='')

	return input().lower().startswith('y')

#------------ main ------------#

def main():
	clear()

	while(True):
		word = getRandomWord(chooseATopic())
		blanks = '_' * len(word)
		missed_letter = []
		correct_letter = []
		clear()

		while(len(missed_letter) < 6):

			display(missed_letter, blanks, word)
			letter = getUserLetter(correct_letter + missed_letter)

			if(letter in(word)):
				
				correct_letter.append(letter)

				for i in range(len(word)):
					if(word[i] == letter):
						blanks = blanks[:i] + letter + blanks[i+1:]

			else:
				missed_letter.append(letter)

			clear()

			if(blanks == word):
				print("\n\t\t",word)
				print("\n\n\t\tYou have won!!!")
				break

			elif(len(missed_letter) == 6):
				print(HANGMAN[6])
				print("\n\n\t\tYou lost!!!")
				print("\n\t\tThe word was: ",word)
				break

		if(not(playAgain())):
			break

		else:
			clear()

main()

