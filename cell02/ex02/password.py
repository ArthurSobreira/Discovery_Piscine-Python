#!/usr/bin/env python3

def	main() -> None:
	password: str = "Python is awesome"
	user_password: str = str(input("Enter the password: "))
	if user_password == password:
		print("ACCESS GRANTED")
	else:
		print("ACCESS DENIED")

if __name__ == "__main__":
	main()
