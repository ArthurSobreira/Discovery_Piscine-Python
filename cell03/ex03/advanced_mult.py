#!/usr/bin/env python3
import sys

def	verify_args() -> bool:
	argc: int = len(sys.argv)
	if (argc != 1):
		print("none")
		return False
	return True

def	main() -> None:
	if (not verify_args()):
		return

	i: int = 0
	while (i <= 10):
		j: int = 0
		print(f"Table de {i}: ", end="")
		while (j <= 10):
			print(i * j, end=" ")
			j += 1
		print()
		i += 1

if __name__ == "__main__":
	main()
