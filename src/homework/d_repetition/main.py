import repetition

def main():
    while True:
        print("\nHomework 3 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                num = int(input("Enter a number between 1 and 9: "))
                if 1 <= num < 10:
                    print(f"Factorial of {num} is {repetition.get_factorial(num)}")
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 9.")

        elif choice == "2":
            while True:
                num = int(input("Enter a number between 1 and 99: "))
                if 1 <= num < 100:
                    print(f"Sum of odd numbers up to {num} is {repetition.sum_odd_numbers(num)}")
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 99.")

        elif choice == "3":
            exit_choice = input("Do you want to exit? (yes/no): ").strip().lower()
            if exit_choice == "yes":
                print("Exiting program.")
                break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
