from class_a import Die

def main():
    die = Die()
    while True:
        input("Press Enter to roll the die...")
        die.roll()
        print(die)
        cont = input("Roll again? (y/n): ").strip().lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    main()
