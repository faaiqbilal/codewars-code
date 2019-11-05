def anagrams(word, words):
	agrams = []
	s1 = sorted(word)
	for i in range (0, len(words)):
		s2 = sorted(words[i])
		if s1 == s2:
			agrams.append(words[i])
	return agrams