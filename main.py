import subprocess
import sys

def clear_screen():
    print("\n" * 50)

def run_find_duplicates():
    print("\n" + "="*50)
    print("Running Find Duplicates Program")
    print("="*50 + "\n")
    subprocess.run([sys.executable, "FindDuplicates.py"])
    input("\nPress Enter to return to menu...")

def run_prime_finder():
    print("\n" + "="*50)
    print("Running Prime Number Finder")
    print("="*50 + "\n")
    subprocess.run([sys.executable, "prime.py"])
    input("\nPress Enter to return to menu...")

def run_matching_game():
    print("\n" + "="*50)
    print("Running Matching Game")
    print("="*50 + "\n")
    print("Note: This game requires a graphical display (tkinter GUI).")
    print("It may not work properly in a console-only environment.")
    print("\nAttempting to launch...")
    try:
        subprocess.run([sys.executable, "MatchinGame.py"])
    except Exception as e:
        print(f"\nError: {e}")
        print("The matching game requires a display environment to run.")
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        clear_screen()
        print("="*50)
        print("Python Programs Collection")
        print("="*50)
        print("\nAvailable Programs:")
        print("1. Find Duplicates - Sort and find duplicate numbers")
        print("2. Prime Number Finder - Find prime numbers in a range")
        print("3. Matching Game - GUI memory matching game (requires display)")
        print("4. Exit")
        print("\n" + "="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            run_find_duplicates()
        elif choice == "2":
            run_prime_finder()
        elif choice == "3":
            run_matching_game()
        elif choice == "4":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
