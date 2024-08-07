def main() -> None:
	first_name: str = input("Hey, what's your first name? : ").strip()
	last_name: str = input("And your last name? : ").strip()
	whole_name: str = first_name + " " + last_name

	print(f"Well, pleased to meet you, {whole_name}.")

if __name__ == "__main__":
	main()
