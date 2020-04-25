'''
	EduMedM
	23-04-2020

'''

from os import system, name

from random import randint

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
  

words = '''caterpillar butterfly grasshopper mantis scorpion beetle ant 
		mosquito spider fly bee wasp eagle owl pigeon canary parrot chicken 
		pelican duck penguin flamingo fish swordfish shark cobra alligator 
		turtle iguana lizard salamander frog koala armadillo kangaroo bat rat
		mouse squirrel rabbit hippopotamus llama rhino elephant zebra pony horse
		sheep donkey giraffe cow camel leopard tiger lion cat kitten fox whale
		otter seal lobster crab dolphin monkey gorilla orangutan panda bear polarbear 
		grizzlybeardog wolf hyena broccoli lettuce spinach celery beans corn asparagus 
		cabbage tomato cucumber eggplant pepper potato garlic pumpkin zucchini mushrooms
		onion carrot beet grapes apple coconut pineapple mango papaya orange grapefruit
		lemon lime strawberry raspberries blueberries blackberries pear cherries banana
		watermelon peanut almond avocado peach beef steak pork sausage bacon ham eggs
		mustard hotdog hamburger spaghetti salad butter cookie taco biscuit pizza toast
		coffee icecream chocolat cake'''.split()

def clear():

	if (name == 'nt'): #for windows
		_ = system('cls')

	else:              #for Linux
		 _ = system('clear')


def getRandomWord(wordlist):
	
	word_index = randint(0, len(words) - 1)

	return wordlist[word_index]

def display(mw,bk):
	
	print("\n\n\t***** HANGEDMAN / Food & Animals *****\n\n")
	print(HANGEDMAN[len(mw)])
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

def listToString(s):
	
	string = ''

	for element in s:
		string += element

	return string

#------------ main ------------#

keep_playing = True
attempts = 6

clear()

while(keep_playing):
	word = getRandomWord(words)
	blanks = '_' * len(word)
	missed_letter = []
	correct_letter = []

	word = list(word)
	blanks = list(blanks)

	while(len(missed_letter) < attempts):

		display(missed_letter, blanks)
		letter = getUserLetter(correct_letter + missed_letter)


		if(letter in(word)):
			
			correct_letter.append(letter)

			for i in range(len(word)):
				if(word[i] == letter):
					blanks[i] = word[i]

		else:
			missed_letter.append(letter)

		clear()

		if(blanks == word):
			print("\n\t\t",listToString(word))
			print("\n\n\t\tYou have won!!!")
			break

		elif(len(missed_letter) == attempts):
			print("\n\n\t\tYou lost!!!")
			print("\n\t\tThe word was: ",listToString(word))
			break

	if(not(playAgain())):
		break

	else:
		clear()

