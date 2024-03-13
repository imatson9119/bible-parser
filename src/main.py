

import json
from src.models.models import Bible

def create_min_bible():
	with open('bible-esv-formatted.json', 'r') as file:
		bible: Bible = json.load(file)
	
	min_bible = {
		'm': {
			't': bible['metadata']['translation'],
			'i': bible['metadata']['loc'],
			'l': bible['metadata']['words'],
			'nb': bible['metadata']['books'],
			'nc': bible['metadata']['chapters'],
			'nv': bible['metadata']['verses']
		},
		'v': []
	}

	for book in bible['content']:
		min_book = {
			'm': {
				'b': book['metadata']['book'],
				'i': book['metadata']['loc'],
				'l': book['metadata']['words'],
				'nc': book['metadata']['chapters'],
				'nv': book['metadata']['verses']
			},
			'v': []
		}

		for chapter in book['content']:
			min_chapter = {
				'm': {
					'c': chapter['metadata']['chapter'],
					'i': chapter['metadata']['loc'],
					'l': chapter['metadata']['words'],
					'nv': chapter['metadata']['verses']
				},
				'v': []
			}

			for verse in chapter['content']:
				min_verse = {
					'm': {
						'v': verse['metadata']['verse'],
						'i': verse['metadata']['loc'],
						'l': verse['metadata']['words']
					},
					'v': verse['content']
				}

				min_chapter['v'].append(min_verse)

			min_book['v'].append(min_chapter)

		min_bible['v'].append(min_book)
	
	with open('bible-esv-min.json', 'w') as file:
		json.dump(min_bible, file)

def create_min_bible_2():
	with open('bible-esv-formatted.json', 'r') as file:
		bible: Bible = json.load(file)
	
	min_bible = [
		{
			't': bible['metadata']['translation'],
			'i': bible['metadata']['loc'],
			'l': bible['metadata']['words'],
			'nb': bible['metadata']['books'],
			'nc': bible['metadata']['chapters'],
			'nv': bible['metadata']['verses']
		},
		[]
	]

	for book in bible['content']:
		min_book = [
			{
				'b': book['metadata']['book'],
				'i': book['metadata']['loc'],
				'l': book['metadata']['words'],
				'nc': book['metadata']['chapters'],
				'nv': book['metadata']['verses']
			},
			[]
		]

		for chapter in book['content']:
			min_chapter = [
				{
					'c': chapter['metadata']['chapter'],
					'i': chapter['metadata']['loc'],
					'l': chapter['metadata']['words'],
					'nv': chapter['metadata']['verses']
				},
				[]
			]

			for verse in chapter['content']:
				min_verse = [
					{
						'v': verse['metadata']['verse'],
						'i': verse['metadata']['loc'],
						'l': verse['metadata']['words']
					},
					verse['content']
				]

				min_chapter[1].append(min_verse)

			min_book[1].append(min_chapter)

		min_bible[1].append(min_book)
	
	with open('bible-esv-min_2.json', 'w') as file:
		json.dump(min_bible, file)

if __name__ == '__main__':
	create_min_bible_2()