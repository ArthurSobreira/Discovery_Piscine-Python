#!/usr/bin/env python3
from math import ceil

def	main() -> None:
	try:
		number = float(input("Give me a number: "))
		print(f"Rounded up: {ceil(number)}")

	except ValueError:
		print("Please enter a valid number.")
		return

if __name__ == "__main__":
	main()
