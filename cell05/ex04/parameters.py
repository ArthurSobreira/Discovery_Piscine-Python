#!/usr/bin/env python3
import sys

def	main() -> None:
	argc: int = len(sys.argv) - 1
	print(f"Number of parameters: {argc}.")
    
if __name__ == "__main__":
	main()
