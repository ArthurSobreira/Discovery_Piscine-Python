#!/usr/bin/env python3
import sys

def downcase_it(arg: str) -> str:
	return arg.lower()

def	main() -> None:
	argc: int = len(sys.argv)
	if argc < 2:
		print("none")
		return

	for param in sys.argv[1:]:
		print(downcase_it(param))

if __name__ == "__main__":
	main()
