#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc != 3:
		print("none")
		return

	begin: int = int(sys.argv[1])
	end: int = int(sys.argv[2])
	
	if begin < end:
		print(list(range(begin, end + 1)))
	else:
		print(list(range(begin, end - 1, -1)))

if __name__ == "__main__":
	main()
