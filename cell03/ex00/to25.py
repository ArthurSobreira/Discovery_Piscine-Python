#!/usr/bin/env python3

def	main() -> None:
	try:
		number: int = int(input("Enter a number less than 25: "))
		if number > 25:
			print("Error")
		else:
			while number <= 25:
				print(f"Inside the loop, my variable is {number}")
				number += 1
	except ValueError:
		print("Please enter a valid number.")
		return

if __name__ == "__main__":
	main()
