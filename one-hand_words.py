#! /bin/env python
from __future__ import print_function
import argparse
import sys

side = ""
dict_file = ""

# Letters easily typable using just the left hand on a QWERTY keyboard
qwerty_left_letters  = set('asdfgqwertzxcvb')
# Letters easily typable using right hand on QWERTY keyboard
qwerty_right_letters = set('hjklyuiopbnm')

# Letters easily typable with one hand using DVORAK
dvorak_left_letters  = set('aoeuipyqjk')
# NOTE: because the right hand side of the DVORAK layout doesn't have any
# vowels, there are no words that can be created with it. However, I'm still
# including this for completeness sake
dvorak_right_letters = set('dhtnsfgcrlxbmwvz')

# COLEMAK one hand keys
colemak_left_letters  = set('qwfpgarstdzxcv')
colemak_right_letters = set('hneioluykm')

# Maps potential strings to either the left or right hand letters.
letter_map = {
	"left"         : qwerty_left_letters,
	'right'        : qwerty_right_letters,
	'l'            : qwerty_left_letters,
	'r'            : qwerty_right_letters,
	'dr'           : dvorak_right_letters,
	'dl'           : dvorak_left_letters,
	'dvorak_left'  : dvorak_left_letters,
	'dvorak_right' : dvorak_right_letters,
	'cl'           : colemak_left_letters,
	'cr'           : colemak_right_letters,
	'colemak_left' : colemak_left_letters,
	'colemak_right': colemak_right_letters
}


parser = argparse.ArgumentParser('Finds words you can type with one hand.')
parser.add_argument('--side', help='Which side to use. Defaults to left hand qwerty.', required=False)
parser.add_argument('--dict', help='Location of file with words to check', required=False)
# parser.add_argument('dict', nargs='?')
# parser.add_argument('side', nargs='?')
args, unknown = parser.parse_known_args()

if not (args.side and args.dict):
	if len(sys.argv) < 2:
		print("Did not provide enough arguments.")
		exit()

	dict_file = sys.argv[1]
	side = set(sys.argv[2])
elif args.side and args.dict:
	dict_file = args.dict
	side = letter_map[args.side]
else:
	print("Did not provide enough arguments, or provided them in incorrect order.")
	exit()




# The list of english words
wordList = open(dict_file,'r').read().split()

# Given a list of potential words, and set of allowable letters, returns list
# of words that are composed only of allowable letters
def filter_words(wordList, acceptable_letters):
	outList = []

	for word in wordList:
		word = word.translate(None, "'")
		if not set(word).difference(acceptable_letters):
			outList.append(word)

	return outList


if __name__ == '__main__':
	for word in filter_words(wordList, side):
		if len(word) > 4:
			print(word)

