#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc < 3:
		print("none")
		return

	args_list: list[str] = sys.argv[1:]
	args_list.reverse()
	for arg in args_list:
		print(arg)

if __name__ == "__main__":
	main()
