def adder(a, b):
    carry = a & b
    result = a ^ b
    while(carry != 0):
        shiftedcarry = carry << 1
        carry = result & shiftedcarry
        result = result ^ shiftedcarry
    return result

def main():
	print(adder(4, 4))
	return 0

if __name__ == "__main__":
	main()