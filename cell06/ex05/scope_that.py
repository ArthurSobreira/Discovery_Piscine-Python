#!/usr/bin/env python3

def	add_one(arg: int) -> None:
	arg += 1

def	main() -> None:
	number: int = 42

	print(number)
	add_one(number)
	print(number)

if __name__ == "__main__":
	main()
