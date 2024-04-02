from typing import List, TypedDict

class VerseMetadata(TypedDict):
	v: int
	i: int
	l: int

class Verse(TypedDict):
	m: VerseMetadata
	v: List[str]

class ChapterMetadata(TypedDict):
	c: int
	i: int
	l: int
	nv: int

class Chapter(TypedDict):
	m: ChapterMetadata
	v: List[Verse]

class BookMetadata(TypedDict):
	b: str
	i: int
	l: int
	nc: int
	nv: int

class Book(TypedDict):
	m: BookMetadata
	v: List[Chapter]


class BibleMetadata(TypedDict):
	t: str
	i: int
	l: int
	nb: int
	nc: int
	nv: int

class Bible(TypedDict): 
	m: BibleMetadata
	v: List[Book]
