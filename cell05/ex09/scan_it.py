#!/usr/bin/env python3
from re import findall
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc != 3:
		print("none")
		return

	keyword: str = sys.argv[1]
	phrase: str = sys.argv[2]
	occurrences: list[str] = findall(keyword, phrase)	

	if len(occurrences) != 0:
		print(len(occurrences))
	else:
		print("none")

if __name__ == "__main__":
	main()
