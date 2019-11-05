def digital_root(n):
	total = 0
	while n > 0:
		x = n%10
		total = total + x
		n = int(n/10)
	if total >= 10:
		total = digital_root(total)			
	print(total)	
	return total
digital_root(456687987654)