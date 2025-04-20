from dictionary import add_inventory, remove_inventory_widget, inventory_dictionary

def menu():
    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter widget name: ")
            try:
                quantity = int(input("Enter quantity to add/update: "))
                add_inventory(name, quantity)
                print(f"{name} updated. Current quantity: {inventory_dictionary[name]}")
            except ValueError:
                print("Please enter a valid integer quantity.")

        elif choice == "2":
            name = input("Enter widget name to delete: ")
            result = remove_inventory_widget(name)
            print(result)

        elif choice == "3":
            print("Exiting Inventory System.")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()