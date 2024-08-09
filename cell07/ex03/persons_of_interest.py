#!/usr/bin/env python3

def	sort(elem) -> int:
	return int(elem[1]["date_of_birth"])

def	famous_births(historical_figures: dict) -> None:
	ordered_figures = sorted(historical_figures.items(), key=sort)

	for figure in ordered_figures:
		print(f"{figure[1]['name']} is a great scientist born in {figure[1]['date_of_birth']}.")

def	main() -> None:
	women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
	}
 
	famous_births(women_scientists)

if __name__ == "__main__":
	main()
