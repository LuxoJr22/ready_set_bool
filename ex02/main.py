def gray_code(n):
	return n ^ (n >> 1)

def main():
	print(gray_code(3))
	return 0

if __name__ == "__main__":
	main()