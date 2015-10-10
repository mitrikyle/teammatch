#!/usr/bin/env python
def score( hacker, profile ):
	''' Returns score based on how close profile is to what is wanted'''
	
	
	hlang = hacker.languages_wanted
	plang =  profile.languages_well
	plang2 = profile.languages_bad
	score = 0.0
	for h in hlang:
		for p in plang:
			if h == p:
				score+= 1.0
				
		for p in plang2:
			if h == p:
				score += 0.5
	score /= 2
				
	hyr = hacker.year
	pyr = profile.year
	score += (3 - abs(hyr-pyr))
	
	hgenre = hacker.genre
	pgenre = profile.genre
	if hgenre == pgenre:
		score += 2
		
	htype= hacker.type
	ptype = profile.type
	if htype == ptype:
		score += 2
		
	
	
	
				
	return score

def matches( hacker, profiles ):
	'''Returns list of profiles with best matches first'''
	results = []
	for profile in profiles:
		results.append( (score(hacker,profile), profile ))
	results = sorted( results, key=lambda score: score[0])
	results = list(reversed(results))
	final = []
	for i in range(len(results)):
		final.append(results[i][1])
	return final
	
class hacker:
	def __init__(self, lang, yr, genre, type):
		self.languages_wanted = lang
		self.year = yr
		self.genre = genre
		self.type = type
		
class prof:
	def __init__(self, name, langwell, langbad, yr, genre,type):
		self.name = name
		self.languages_well = langwell
		self.languages_bad = langbad
		self.year = yr
		self.genre = genre
		self.type = type
		
me = hacker(('python', 'ruby', 'c++', 'javascript' ),4, 'education','app')
joe = prof('joe',('python', 'ruby', 'c++' ), ('java','javascript'),3,'education','app')
john = prof('john',('python', 'ruby'),( 'c++' ,'java'),1,'social','app')
josh = prof('josh',('java', 'python', 'ruby'),('c++','javascript'),2,'social','app')
profiles = [joe, john,josh]
for i in matches(me,profiles):
	print i.name
		
	
	
	