from src.homework.c_decisions.decisions import get_options_ratio, get_faculty_rating

def main():
    # Prompt the user for options and total and convert input to numbers
    options = float(input("Enter the number of options: "))
    total = float(input("Enter the total number of options: "))

    # Get the ratio by calling get_options_ratio
    ratio = get_options_ratio(options, total)

    # Get the faculty rating by calling get_faculty_rating
    rating = get_faculty_rating(ratio)

    # Display the result
    print(f"The faculty rating is: {rating}")

if __name__ == "__main__":
    main()
