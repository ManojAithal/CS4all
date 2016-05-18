class Rational:
	def __init__(self,num,denom):
		self.numerator = num
		self.denominator = denom
	def add(self,other):
		newNumerator = self.numerator*other.denominator + other.numerator*self.denominator
		newDenominator = self.denominator*other.denominator
		return Rational(newNumerator,newDenominator)
