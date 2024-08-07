#!/usr/bin/env python3

def	main() -> None:
	user_input: str = input("What you gotta say? : ")
	while True:
		user_input = input("I got that! Anything else? : ")
		if user_input == "STOP":
			break

if __name__ == "__main__":
	main()
