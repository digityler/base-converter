import math

class BaseConversion:
	''' converts any number to and from any base of 20 or less '''
	''' number is type string. baseFrom and baseTo are type integer '''

	def __init__(self, number, baseFrom, baseTo):
		self.number = number
		self.baseFrom = baseFrom
		self.baseTo = baseTo
		
		self.letterCodes = { 
			'A': 10,
			'10': 'A',
			'B': 11,
			'11': 'B',
			'C': 12,
			'12': 'C',
			'D': 13,
			'13': 'D',
			'E': 14,
			'14': 'E',
			'F': 15,
			'15': 'F',
			'G': 16,
			'16': 'G',
			'H': 17,
			'17': 'H',
			'J': 18,
			'18': 'J',
			'K': 19,
			'19': 'K'
		}
	
	def aceOfBase(self):
		baseFrom = self.baseFrom
		baseTo = self.baseTo

		if baseFrom == baseTo:
			return self.number
		elif baseFrom == 10:
			return self.convertFromBaseTen()
		elif baseTo == 10:
			return self.convertToBaseTen()
		else:
			self.number = self.convertToBaseTen()
			return self.convertFromBaseTen()

	def convertToBaseTen(self):
		number = self.number
		baseFrom = self.baseFrom
		numList = []
		numList = list(number)
		letterCodes = self.letterCodes

		if baseFrom > 10:
			for index, k in enumerate(numList):
				try: 
					letterCodes[k]
					numList[index] = letterCodes[k]
				except:
					continue

		listReverse = list(reversed(numList))
		numLen = len(numList)
		numberInBaseTen = 0

		for i in range(numLen):
			numberInBaseTen += int(listReverse[i]) * baseFrom**i	

		return numberInBaseTen

	def convertFromBaseTen(self):
		number = int(self.number)
		baseTo = self.baseTo
		letterCodes = self.letterCodes
		digits = []
		basePower = int(math.floor(math.log(number, baseTo)))

		for i in range(basePower, -1, -1):
			q = number // (baseTo**i)
			number -= q * baseTo**i
			if q > 9:
				q = letterCodes[str(q)]
			digits.append(str(q))

		return ''.join(digits)

if __name__ == "__main__":
	conversionInstance = BaseConversion('348', 19, 7)
	result = conversionInstance.baseFunction()
	print(result)
