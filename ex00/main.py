def adder(a, b):
	mask = 1
	m = a if a > b else b
	ret = 0
	while (mask <= m):
		mask = mask << 1
	while (mask > 0):
		ret = a & mask
		mask = mask >> 1
	return ret

def main():
	print(adder(4, 1))
	return 0

if __name__ == "__main__":
	main()