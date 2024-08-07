#!/usr/bin/env python3

def	main() -> None:
	try:
		first_number: int = int(input("Give me the first number: "))
		second_number: int = int(input("Give me the second number: "))

		print("Thank you!")
		
		list_of_operations: list[str] = ['+', '-', '/', '*']
		for operation in list_of_operations:
			print(f"{first_number} {operation} {second_number}", end=" = ")
			if (operation == '+'):
				print(first_number + second_number)
			elif (operation == '-'):
				print(first_number - second_number)
			elif (operation == '/'):
				print(first_number // second_number)
			elif (operation == '*'):
				print(first_number * second_number)

	except ValueError:
		print("Please enter a valid number.")
		return
	
if __name__ == "__main__":
	main()
