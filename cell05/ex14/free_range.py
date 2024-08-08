#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc != 3:
		print("none")
		return

	first: int = int(sys.argv[1])
	last: int = int(sys.argv[2])
	
	if first < last:
		print(list(range(first, last + 1)))
	else:
		print(list(range(first, last - 1, -1)))

if __name__ == "__main__":
	main()
