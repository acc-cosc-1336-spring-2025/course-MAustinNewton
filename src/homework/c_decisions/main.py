import decisions

def main():
    """Main program to calculate faculty rating based on user input"""
    try:
        options = float(input("Enter the number of options: "))
        total = float(input("Enter the total: "))

        if total == 0:
            print("Total cannot be zero.")
            return

        ratio = decisions.get_options_ratio(options, total)
        rating = decisions.get_faculty_rating(ratio)

        print(f"The faculty rating is: {rating}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
