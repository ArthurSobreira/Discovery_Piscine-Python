#!/usr/bin/env python3

def	array_of_names(names_dict: dict) -> list:
	return [f"{key.capitalize()} {value.capitalize()}" \
     	for key, value in names_dict.items()]

def	main() -> None:
	persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
	}

	print(array_of_names(persons))

if __name__ == "__main__":
	main()
