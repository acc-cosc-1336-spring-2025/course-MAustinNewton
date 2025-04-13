import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

def main():
    while True:
        print("\n1 - Get p distance matrix")
        print("2 - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number of DNA strings (≤ 10): "))
            dna_lists = []
            for i in range(n):
                dna = list(input(f"Enter DNA string {i+1}: ").strip())
                dna_lists.append(dna)

            matrix = get_p_distance_matrix(dna_lists)
            print("\nP-Distance Matrix:")
            for row in matrix:
                print(" ".join(f"{val:.5f}" for val in row))
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
