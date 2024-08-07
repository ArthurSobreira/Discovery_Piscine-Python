#!/usr/bin/env python3

def	main() -> None:
	original_array: list[int] = [2, 8, 9, 48, 8, 22, -12, 2]
	new_array: list[int] = [x + 2 for x in original_array]

	print(f"Original array: {original_array}")
	print(f"New array: {new_array}")	
    
if __name__ == "__main__":
	main()
