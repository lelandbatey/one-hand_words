One-handed Words
================


I've always been curious what words I could type using only my left or right hands. It'd be nice to be to have passwords I could lazily type using only one hand, or using only one sequence of letters. This program lets you find words you can type on one hand.


Usage
-----

There's two ways to invoke this program:

### 1. Specify Explicit Arguments

You can specify which side/keyboard format to check against and the dictionary file to use with the following flags:

	--side
		Specify which format/side of the keyboard to check against. For example, you could type "left" or "right" for the appropriate side on the QWERTY keyboard. The list of all valid values is:

			left
			right
			l
			r
			dr
			dl
			dvorak_left
			dvorak_right
			cl
			cr
			colemak_left
			colemak_right

	--dict
		Specify the file containing the list of words to compare against.

Here are some examples:

	./one-hand_words.py --side left --dict dict.txt


### 2. Implicit Arguments; Dictionary and Keys

You can specify the dictionary file and a list of characters to allow in words. The first argument must be the location of the wordlist, and the second argument must be a list of characters to allow words to be composed of.

Examples:

	./one-hand_words.py dict.txt qwerasdf


