#!/usr/bin/env python3

def	main() -> None:
	first_number: int = int(input("Give me the first number: "))
	second_number: int = int(input("Give me the second number: "))

	print("Thank you!")
	
	list_of_operations: list[str] = ['+', '-', '/', '*']
	for operation in list_of_operations:
		print(f"{first_number} + {second_number}")
		if (operation == '+'):
			print(f"{first_number} + {second_number} = {first_number + second_number}")
		elif (operation == '-'):
			print(f"{first_number} - {second_number} = {first_number - second_number}")
		elif (operation == '/'):
			print(f"{first_number} / {second_number} = {first_number // second_number}")
		elif (operation == '*'):
			print(f"{first_number} * {second_number} = {first_number * second_number}")
	
if __name__ == "__main__":
	main()
