# Flowchart for planning hangman:

Get word from list of words
	Create dictionary with one list of letters in the word, one list of underscores per letter
	Create underscores one per letter in word
	

Get variable from input for a letter

for each letter in dictionary(word):
	if input is the same replace dictionary(underscores) with dictionary(word)
		if no underscores in dictionary(underscores) then user wins
	if input is not the same, draw the hangman
		if hangman is completed, player loses
