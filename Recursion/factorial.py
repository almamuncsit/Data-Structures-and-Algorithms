
def fact(n):
	if n in [0, 1]:
		return 1
	return n * fact(n - 1)

def main():
	n = int( input() )
	print( 'Factorial is: ', fact(n) )


if __name__ == '__main__':
	main()