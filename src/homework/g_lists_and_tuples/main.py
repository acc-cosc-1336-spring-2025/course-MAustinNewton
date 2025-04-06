from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\n1 - Show the list low/high values")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            numbers = []
            while True:
                try:
                    value = int(input("Enter a list value: "))
                    numbers.append(value)
                except ValueError:
                    print("Please enter a valid integer.")
                    continue

                if len(numbers) >= 3:
                    cont = input("Do you want to enter another value? (y/n): ")
                    if cont.lower() != 'y':
                        break

            if numbers:
                print(f"Lowest value: {get_lowest_list_value(numbers)}")
                print(f"Highest value: {get_highest_list_value(numbers)}")
            else:
                print("No values entered.")

        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
