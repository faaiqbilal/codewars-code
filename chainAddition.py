class CustomInt(int):
	def __call__(self, v):
		return CustomInt(self+v)

def add(nyeow):
	return CustomInt(nyeow)
	
print(add(1)(2)(3)(4)(66))