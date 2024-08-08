#!/usr/bin/env python3
import sys

def	shrink(arg: str) -> None:
	print(arg[:8])

def	enlarge(arg: str) -> None:
	print(arg.ljust(8, 'Z'))

def	main() -> None:
	argc: int = len(sys.argv)
	if argc < 2:
		print("none")
		return

	for param in sys.argv[1:]:
		if len(param) > 8:
			shrink(param)
		elif len(param) < 8:
			enlarge(param)
		else:
			print(param)
 
if __name__ == "__main__":
	main()
