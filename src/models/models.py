from typing import List, TypedDict

class VerseMetadata(TypedDict):
	book: str
	chapter: int
	verse: int
	loc: int
	words: int

class Verse(TypedDict):
	metadata: VerseMetadata
	content: List[str]

class ChapterMetadata(TypedDict):
	book: str
	chapter: int
	loc: int
	verses: int
	words: int

class Chapter(TypedDict):
	metadata: ChapterMetadata
	content: List[Verse]

class BookMetadata(TypedDict):
	book: str
	loc: int
	chapters: int
	verses: int
	words: int

class Book(TypedDict):
	metadata: BookMetadata
	content: List[Chapter]


class BibleMetadata(TypedDict):
	translation: str
	books: int
	loc: int
	chapters: int
	words: int
	verses: int

class Bible(TypedDict): 
	metadata: BibleMetadata
	content: List[Book]

