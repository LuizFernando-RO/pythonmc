'''
Interactive Dictionanry Application
- GOAL
This projects aims to create a program that allows the user to
type a word and retrieve it's definition.
- KNOWLEDGE
	- Import and reading from a JSON file
	- Dictionary operations
	- User interaction
	- String operations
	- 
'''
from difflib import get_close_matches
import json

data = json.load(open('data.json'))

def query(word):
	if word.lower() not in data.keys():
		if word.title() in data.keys():
			return data[word.title()]
		if word.upper() in data.keys():
			return data[word.upper()]
		matches = get_close_matches( word.lower(), data.keys() )
		if len(matches) == 0:
			return 'Definition of {} not found.'.format(word)
		else:
			choice = input('Did you mean {}? (Y/N) '.format(matches[0]))
			if choice.upper() == 'Y':
				return data[matches[0]]
			else:
				return 'Definition of {} not found.'.format(word)
	return data[word]

word = input("Enter word: ")

results = query(word)

if type(results) == str:
	print(results)
else:
	for result, index in zip(results,range(len(results))):
		print('{} - {}'.format(index+1,result))