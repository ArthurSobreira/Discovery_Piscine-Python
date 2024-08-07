#!/usr/bin/env python3

def	main() -> None:
	try:
		number = float(input("Give me a number: "))
		string_number: str = str(number)
		dot_position: int = string_number.find('.')

		if (string_number[dot_position:] != '.0'):
			print("This number is a decimal.")
		else:
			print("This number is an integer.")

	except ValueError:
		print("Please enter a valid number.")
		return

if __name__ == "__main__":
	main()
