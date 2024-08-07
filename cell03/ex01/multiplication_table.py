#!/usr/bin/env python3

def	main() -> None:
	try:
		number: int = int(input("Enter a number: "))
		mult = 0
		while mult < 10:
			print(f"{mult} x {number} = {number * mult}")
			mult += 1
	except ValueError:
		print("Please enter a valid number.")
		return

if	__name__ == "__main__":
	main()
