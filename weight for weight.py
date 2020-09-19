def longest_consec(strarr, k):
	indarr = []
	for j in range(0, len(strarr)):
		indarr.append(strarr[j])
	if len(strarr) ==0 or k > len(strarr) or k <= 0:
		print("")
		return ""
	else:
		final_string = ""
		for i in range (0, k):
			final_string += strarr[i]
		print(final_string)
		return final_string