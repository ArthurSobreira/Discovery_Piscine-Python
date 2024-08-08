#!/usr/bin/env python3

def	greetings(arg: str = None) -> None:
	if arg == None:
		print("Hello, noble stranger")
	elif not isinstance(arg, str):
		print("Error! It was not a name.")
	else:
		print(f"Hello, {arg}.")

def	main() -> None:
	greetings('Alexandra')
	greetings('Wil')
	greetings()
	greetings(42)

if __name__ == "__main__":
	main()
