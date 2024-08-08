#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc != 2:
		print("none")
		return

	argument: str = sys.argv[1]
	user_input: str = input("What was the parameter? ")
	
	if argument == user_input:
		print("Good job!")
	else:
		print("Nope, sorry...")
 
if __name__ == "__main__":
	main()
