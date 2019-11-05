def longest_consec(strarr, k):
	strarr.sort(key=len)
	final_string = ""
	for i in range (0, k):
		final_string += strarr[i]

	print(final_string)
	return final_string