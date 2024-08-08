#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc < 2:
		print("none")
		return

	for param in sys.argv[1:]:
		if param.find("ism") == -1:
			print(param, end="ism")
			print()

if __name__ == "__main__":
	main()
