def valid_parentheses(string):
	counter1 = 0
	counter2 = 0
	for i in range(0, len(string)):
		if string[i] == '(':
			counter1 = counter1 + 1
		elif string[i] == ')':
			counter2 = counter2 + 1
		if counter2 > counter1:
			return False
	if counter1 != counter2:
		return False
	else:
		return True