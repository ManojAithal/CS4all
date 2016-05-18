class Rational:
	def __init__(self,num,denom):
		self.numerator = num
		self.denominator = denom
	def __add__(self,other):
		# overloading + operator
		newNumerator = self.numerator*other.denominator + other.numerator*self.denominator
		newDenominator = self.denominator*other.denominator
		return Rational(newNumerator,newDenominator)
	def __sub__(self,other):
		# overloading - operator
                newNumerator = self.numerator*other.denominator - other.numerator*self.denominator
                newDenominator = self.denominator*other.denominator
                return Rational(newNumerator,newDenominator)
	def __mul__(self,other):
		# overloading * operator
		newNumerator = self.numerator*other.numerator
		newDenominator = self.denominator*other.denominator
		return Rational(newNumerator,newDenominator)
	def __truediv__(self,other):
		# overloading / operator
		newNumerator = self.numerator*other.denominator
		newDenominator = self.denominator*other.numerator
		return Rational(newNumerator,newDenominator)
	def __eq__(self,other):
		# overloading == operator
		return self.numerator*other.denominator == other.numerator*self.denominator
	def __gt__(self,other):
		# overloading > operator
                return self.numerator*other.denominator > other.numerator*self.denominator
	def __lt__(self,other):
		# overloading < operator
                return self.numerator*other.denominator < other.numerator*self.denominator
	def __ge__(self,other):
		# overloading >= operator
                return self.numerator*other.denominator >= other.numerator*self.denominator
	def __le__(self,other):
		# overloading <= operator
                return self.numerator*other.denominator <= other.numerator*self.denominator
	def __ne__(self,other):
		# overloading != operator
                return self.numerator*other.denominator != other.numerator*self.denominator




