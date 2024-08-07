#!/usr/bin/env python3

def	main() -> None:
	first_number: int = int(input("Enter the first number: "))
	second_number: int = int(input("Enter the second number: "))
	result: int = first_number * second_number

	print(f"\n{first_number} x {second_number} = {result}")

	if result < 0:
		print("The result is negative.")
	elif result > 0:
		print("The result is positive.")
	else:
		print("The result is positive and negative.")
  
if __name__ == "__main__":
	main()
