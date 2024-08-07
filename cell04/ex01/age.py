#!/usr/bin/env python3

def	main() -> None:
	try:
		age: int = int(input("Please tell me your age: "))
		print(f"You are currently {age} years old.")
	
		ages: list[int] = [age + 10, age + 20, age + 30]
		for i in range(3):
			print(f"In {(i + 1) * 10} years, you will be {ages[i]} years old.")
	except ValueError:
		print("Please enter a valid age.")
		return

if __name__ == "__main__":
	main()
