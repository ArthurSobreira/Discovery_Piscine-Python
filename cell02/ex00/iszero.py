#!/usr/bin/env python3

def main() -> None:
	try:
		number: float = float(input("Enter a number: "))
	except ValueError:
		print("Please enter a valid number.")
		return
	if number == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")

if __name__ == "__main__":
	main()
