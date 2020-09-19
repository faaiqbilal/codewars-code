def top_3_words(text):
	text=text.lower()
	import re
	list_of_words = re.findall("[\s]?([']?[A-Za-z]+'?[A-Za-z']*)[\s,:]?", text)
	list_of_words.sort()

	final_word_array = []
	word_array = []
	seen = set()
	for word in list_of_words:
		word_array.append([word, list_of_words.count(word)])

	for word in word_array:
		t = tuple(word)
		if t not in seen:
			final_word_array.append(t)
			seen.add(t)

	final_word_array.sort(key=lambda x:x[1])
	print(len(final_word_array))
	if len(final_word_array) == 0:
		return []
		print([]) 

	
	elif len(final_word_array) >= 3:
		words_and_count = [final_word_array[-1], final_word_array[-2], final_word_array[-3]]
		words_only = []
		print(words_and_count)
		for wnc in words_and_count:
			words_only.append(wnc[0])
		return words_only		
		# print(words_only)


	elif len(final_word_array) == 2:
		words_and_count = [final_word_array[-1], final_word_array[-2]]
		words_only = []
		for wnc in words_and_count:
			words_only.append(wnc[0])
		return words_only		
		# print(words_only)

		
	elif len(final_word_array) == 1:
		words_and_count = [final_word_array[-1]]
		words_only = []
		for wnc in words_and_count:
			words_only.append(wnc[0])
		return words_only		
		# print(words_only)

