

from calendar import c
import json
from src.models.models import Bible, Book, Chapter, Verse
import os
import re

# pattern for all non-alphanumeric characters
pattern = re.compile('[\\W_]+')

def process_input():
	files = os.listdir('src/input')

	for file in files:
		with open(f'src/input/{file}', 'r') as fileRef:
			data = json.load(fileRef)
			process_file(file.split('.')[0], data)

def process_file(name: str, data):
	raw_bible = data[0]
	word_map = {}
	letter_map = {}
	cur_index = 0
	cur_bible = {
		'm': {
			't': name,
			'i': cur_index, 
			'l': 0,
			'nb': 0,
			'nc': 0,
			'nv': 0
		},
		'v': []
	}
	book_no = 0;
	for book, book_data in raw_bible.items():
		cur_book = {
			'm': {
				'b': book,
				'i': cur_index,
				'l': 0,
				'nc': 0,
				'nv': 0,
				'bn': book_no
			},
			'v': []
		}
		book_no += 1
		for chapter, chapter_data in book_data.items():
			cur_chapter = {
				'm': {
					'c': int(chapter),
					'i': cur_index,
					'l': 0,
					'nv': 0
				},
				'v': []
			}
			for verse, verse_data in chapter_data.items():
				verse_text = sanitize_verse(verse_data)
				cur_verse = {
					'm': {
						'v': int(verse),
						'i': cur_index,
						'l': len(verse_text)
					},
					'v': verse_text
				}
				add_to_word_map(word_map, verse_text, cur_index)
				add_to_letter_map(letter_map, verse_text, cur_index)
				cur_index += len(verse_text)
				cur_chapter['v'].append(cur_verse)

			cur_chapter['m']['l'] = sum([verse['m']['l'] for verse in cur_chapter['v']])
			cur_chapter['m']['nv'] = len(cur_chapter['v'])
			cur_book['v'].append(cur_chapter)

		cur_book['m']['l'] = sum([chapter['m']['l'] for chapter in cur_book['v']])
		cur_book['m']['nc'] = len(cur_book['v'])
		cur_book['m']['nv'] = sum([chapter['m']['nv'] for chapter in cur_book['v']])
		cur_bible['v'].append(cur_book)

	cur_bible['m']['l'] = sum([book['m']['l'] for book in cur_bible['v']])
	cur_bible['m']['nb'] = len(cur_bible['v'])
	cur_bible['m']['nc'] = sum([book['m']['nc'] for book in cur_bible['v']])
	cur_bible['m']['nv'] = sum([book['m']['nv'] for book in cur_bible['v']])

	with open(f'bibles/{name}.json', 'w+') as file:
		json.dump(cur_bible, file)
	
	with open(f'word_maps/{name}.json', 'w+') as file:
		json.dump(word_map, file)

	with open(f'letter_maps/{name}.json', 'w+') as file:
		json.dump(letter_map, file)
				
def add_to_word_map(word_map, verse_text, cur_index):
	for index, word in enumerate(verse_text):
		sanitized_word = pattern.sub('', word).lower()
		if sanitized_word not in word_map:
			word_map[sanitized_word] = [index + cur_index]
		else:
			word_map[sanitized_word].append(index + cur_index)

def add_to_letter_map(letter_map, verse_text, cur_index):
	for index, word in enumerate(verse_text):
		sanitized_word = pattern.sub('', word).lower()
		if len(sanitized_word) == 0:
			print(f'Empty word found: {word}')
			print(verse_text)
			continue;
		if sanitized_word[0] not in letter_map:
			letter_map[sanitized_word[0]] = [index + cur_index]
		else:
			letter_map[sanitized_word[0]].append(index + cur_index)
				
def sanitize_verse(verse):
	# Add spaces around em dashes to split connected words
	verse = verse.replace('\u2014', '\u2014 ')
	return verse.split()



if __name__ == '__main__':
	process_input()