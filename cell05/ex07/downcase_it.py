#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc == 2:
		print(sys.argv[1].lower())
	else:
		print("none")
    
if __name__ == "__main__":
	main()
