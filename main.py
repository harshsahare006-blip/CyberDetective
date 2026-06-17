# ==========================================
# CyberDetectiveX - Main Game File
# Version 2.0
# ==========================================

import os

from core.player import Player
from core.save_load import save_game, load_game
from core.case_engine import CaseEngine
from cases.case001 import get_case
from cases.case002 import get_case as get_case002
from cases.case003 import get_case as get_case003
from cases.case004 import get_case as get_case004
from cases.case005 import get_case as get_case005
from cases.case006 import get_case as get_case006
from cases.case007 import get_case as get_case007
from cases.case008 import get_case as get_case008
from cases.case009 import get_case as get_case009
from cases.case010 import get_case as get_case010
from tools.hash_checker import run as hash_run
from tools.password_strength import run as password_run
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("=" * 60)
    print(r"""
  ____ __   __  ____   ______  _____  
 / ___|\ \ / / |  _ \ |  ____||  __ \ 
| |     \ V /  | |_) || |__   | |__) |
| |      | |   |  _ < |  __|  |  _  / 
| |___   | |   | |_) || |____ | | \ \ 
 \____|  |_|   |____/ |______||_|  \_\
""")
    print("                CYBER X")
    print("     Digital Investigation Simulator")
    print("                 v2.0")
    print("=" * 60)

def create_new_player():
    clear_screen()
    banner()

    print("\nCreate Your Detective Profile")
    print("-" * 30)

    while True:
        name = input("Enter Detective Name: ").strip()

        if len(name) > 0:
            break

        print("Name cannot be empty!")

    player = Player(name)

    print(f"\nWelcome Detective {name}!")
    input("\nPress Enter to continue...")

    return player


def show_profile(player):
    clear_screen()
    banner()

    print("\nDETECTIVE PROFILE")
    print("-" * 30)

    print(f"Name       : {player.name}")
    print(f"Rank       : {player.rank}")
    print(f"XP         : {player.xp}")
    print(f"Cases Solved : {player.cases_solved}")

    print("\nAchievements")

    if player.achievements:
        for achievement in player.achievements:
            print(f"✓ {achievement}")
    else:
        print("No achievements unlocked.")

    input("\nPress Enter to return...")


def investigations_menu(player):

    while True:

        clear_screen()
        banner()

        print("\nINVESTIGATIONS")
        print("-" * 30)

        print("1. Case 001 - The Missing Database")
        print("2. Case 002 - The Phishing Wire Transfer")
        print("3. Case 003 - The Encrypted Files")
        print("4. Case 004 - The Disgruntled Departure")
        print("5. Case 005 - The Open Bucket")
        print("6. Case 006 - The Vanishing Records")
        print("7. Case 007 - The Laptop Left Behind")
        print("8. Case 008 - The USB In The Parking Lot")
        print("9. Case 009 - The Vendor's Weak Link")
        print("10. Case 010 - The Relentless Login Attempts")
        print("0. Back")

        choice = input("\nSelect: ")

        if choice == "1":

            case = get_case()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input(
                "\nPress Enter to continue..."
            )
        

        elif choice == "2":

            case = get_case002()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "3":

            case = get_case003()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")
        
        elif choice == "4":

            case = get_case004()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")
        
        elif choice == "5":

            case = get_case005()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")
        
        elif choice == "6":

            case = get_case006()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "7":

            case = get_case007()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "8":

            case = get_case008()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "9":

            case = get_case009()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "10":

            case = get_case010()

            engine = CaseEngine(
                player,
                case
            )

            engine.start()

            input("\nPress Enter to continue...")

        elif choice == "0":

            break

        else:

            print("\nInvalid choice.")
            input("Press Enter...")


def tools_menu():
    while True:
        clear_screen()
        banner()

        print("\nCYBER TOOLS")
        print("-" * 30)

        print("1. Hash Checker")
        print("2. Password Strength Checker")
        print("0. Back")

        choice = input("\nSelect option: ")

        if choice == "1":
            hash_run()
            input("\nPress Enter to return...")

        elif choice == "2":
            password_run()
            input("\nPress Enter to return...")

        elif choice == "0":
            break

        else:
            print("Invalid choice!")
            input("Press Enter to try again...")

def main_menu(player):
    while True:

        clear_screen()
        banner()

        print(f"\nDetective : {player.name}")
        print(f"Rank      : {player.rank}")
        print(f"XP        : {player.xp}")

        print("\nMAIN MENU")
        print("-" * 30)

        print("1. Detective Profile")
        print("2. Investigations")
        print("3. Cyber Tools")
        print("4. Save Game")
        print("5. Load Game")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            show_profile(player)

        elif choice == "2":
            investigations_menu(player)

        elif choice == "3":
            tools_menu()

        elif choice == "4":
            save_game(player)
            print("\nGame Saved Successfully!")
            input("Press Enter...")

        elif choice == "5":
            loaded_player = load_game()

            if loaded_player:
                player = loaded_player
                print("\nSave Loaded Successfully!")

            else:
                print("\nNo save found.")

            input("Press Enter...")

        elif choice == "0":

            save_choice = input(
                "\nSave before exiting? (y/n): "
            ).lower()

            if save_choice == "y":
                save_game(player)

            print("\nGoodbye Detective.")
            break

        else:
            print("\nInvalid choice.")
            input("Press Enter...")


def start_game():

    while True:

        clear_screen()
        banner()

        print("\n1. New Game")
        print("2. Load Game")
        print("0. Exit")

        choice = input("\nSelect Option: ")

        if choice == "1":
            player = create_new_player()
            main_menu(player)

        elif choice == "2":

            player = load_game()

            if player:
                main_menu(player)
            else:
                print("\nNo save file found.")
                input("Press Enter...")

        elif choice == "0":
            print("\nExiting CyberDetectiveX...")
            break

        else:
            print("\nInvalid choice.")
            input("Press Enter...")


if __name__ == "__main__":
    start_game()