#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv)
	if argc < 2:
		print("none")
		return

	print(f"parameters: {argc - 1}")
	for param in sys.argv[1:]:
		print(f"{param}: {len(param)}")
    
if __name__ == "__main__":
	main()
