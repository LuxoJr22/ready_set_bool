def adder(a, b):
	carry = a & b
	result = a ^ b
	while(carry != 0):
		shiftedcarry = carry << 1
		carry = result & shiftedcarry
		result = result ^ shiftedcarry
	return result

def multiplier(a, b):
	factor1 = a
	factor2 = b
	result = 0
	while(factor2 != 0):
		if (factor2 & 1):
			result = adder(result, factor1)
		factor2 = factor2 >> 1
		factor1 = factor1 << 1
	return result

def main():
	print(multiplier(4, 1))
	return 0

if __name__ == "__main__":
	main()