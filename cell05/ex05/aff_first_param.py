#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc > 1:
		print(sys.argv[1])
	else:
		print("none")

if __name__ == "__main__":
	main()
