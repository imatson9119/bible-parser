

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

def generate_headers_dictionary():
	with open('bible-esv-formatted.json', 'r') as file:
		bible: Bible = json.load(file)	
	
	metadata = {}

	for book in bible['content']:
		metadata[book['metadata']["loc"]] = {'b': book['metadata']['book']}
		for chapter in book['content']:
			if chapter['metadata']['loc'] not in metadata:
				metadata[chapter['metadata']['loc']] = {'c': chapter['metadata']['chapter']}
			else:
				metadata[chapter['metadata']['loc']]['c'] = chapter['metadata']['chapter']
			for verse in chapter['content']:
				if verse['metadata']['loc'] not in metadata:
					metadata[verse['metadata']['loc']] = {'v': verse['metadata']['verse']}
				else:
					metadata[verse['metadata']['loc']]['v'] = verse['metadata']['verse']
	
	with open('bible-esv-headers.json', 'w') as file:
		json.dump(metadata, file)
	



if __name__ == '__main__':
	generate_headers_dictionary()