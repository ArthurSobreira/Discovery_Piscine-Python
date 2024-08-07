#!/usr/bin/env python3

def	main() -> None:
	try:
		number: float = float(input("Hey, give me a number: "))
	except ValueError:
		print("Please enter a valid number.")
		return
	if number < 0:
		print("This number is negative.")
	elif number > 0:
		print("This number is positive.")
	else:
		print("This number is both positive and negative.")

if __name__ == "__main__":
	main()
