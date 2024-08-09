#!/usr/bin/env python3

def	find_the_redheads(family: dict) -> list:
	return [key for key, value in family.items() if value == "red"]

def	main() -> None:
	dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
	}

	print(find_the_redheads(dupont_family))

if __name__ == "__main__":
	main()
