#!/usr/bin/env python3

def	array_of_names(names_dict: dict) -> list:
	names_array: list = []
	
	for key in names_dict:
		whole_name: str = key.capitalize() + " " \
			+ names_dict[key].capitalize()

		names_array.append(whole_name)
	
	return names_array

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
