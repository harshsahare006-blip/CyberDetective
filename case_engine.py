from core.evidence import EvidenceLocker
from core.notes import NotesManager
from core.report_system import ReportSystem

class CaseEngine:

    def __init__(
        self,
        player,
        case_data
    ):

        self.player = player

        self.case = case_data

        self.evidence = EvidenceLocker()

        self.notes = NotesManager()

        self.investigated = set()

        self.mission_stage = 1

    def show_help(self):

     print("\n===== COMMANDS =====")

     if self.mission_stage == 1:

        print("help")
        print("case")
        print("investigate")
        print("hint (get investigation clue)")

     elif self.mission_stage == 2:

        print("help")
        print("evidence")
        print("notes")
        print("add note <text>")
        print("hint (analyze clue)")

     elif self.mission_stage == 3:

        print("help")
        print("submit report")
        print("evidence")
        print("hint (final guidance)")

    def show_hint(self):

     if self.mission_stage == 1:
        print("\nHint: Investigate available targets.")

     elif self.mission_stage == 2:
        print("\nHint: Review evidence and write notes.")

     elif self.mission_stage == 3:
        print("\nHint: You have enough information to submit a report.")

    def show_case(self):

        print("\n===== CASE FILE =====")

        print(f"Title: {self.case['title']}")

        print(
            f"\n{self.case['briefing']}"
        )

    def investigate(self, target):

        if target not in self.case["clues"]:

            print("\nNothing found.")

            return

        if target in self.investigated:

            print(
                "\nAlready investigated."
            )

            return

        clue = self.case["clues"][target]

        print(f"\n{clue}")

        self.evidence.add(
            f"{target.title()} Evidence"
        )

        self.investigated.add(target)

    def show_investigation_menu(self):

     while True:

        print("\n===== INVESTIGATION TARGETS =====")
        print("1. Logs")
        print("2. Employees")
        print("3. Network")
        print("4. Database")
        print("0. Back")

        choice = input("\nSelect target: ")

        if choice == "1":
            self.handle_investigation("logs")

        elif choice == "2":
            self.handle_investigation("employees")

        elif choice == "3":
            self.handle_investigation("network")

        elif choice == "4":
            self.handle_investigation("database")

        elif choice == "0":
            break

        else:
            print("Invalid choice")

    def handle_investigation(self, target):

        print(f"\n[ANALYZING {target.upper()}...]\n")

        clues = self.case.get("clues", {})

        if target in clues:

            print(clues[target])

            self.evidence.add(f"{target.title()} Evidence")

        else:

            print("No significant findings in this area.")

        self.investigated.add(target)

        if len(self.investigated) >= 1:
          self.mission_stage = 2

        if len(self.investigated) == len(clues):

         self.mission_stage = 3

         print("\n" + "=" * 40)
         print("INVESTIGATION COMPLETE")
         print("=" * 40)

         print("✓ All clues collected")
         print("✓ Report System Unlocked")

         print("\nRecommended Commands:")
         print("evidence")
         print("notes")
         print("submit report")



        remaining = set(clues.keys()) - self.investigated

        if remaining:

          print("\nRemaining Targets:")

        for item in remaining:

         print(f"- {item.title()}")


        if len(self.investigated) < len(clues):

         print("\nNext Step:")
         print("Type 'investigate' to continue.")
         print("Type 'evidence' to review evidence.")
         print("Type 'notes' to review notes.")

    def start(self):

        print(
            f"\nStarting Case: "
            f"{self.case['title']}"
        )

        print(
            "\nType 'help' for commands."
        )

        while True:

            command = input(
                "\n> "
            ).strip().lower()

            if command == "help":

                self.show_help()

            elif command == "case":

                self.show_case()

            elif command == "investigate":
             
                self.show_investigation_menu()

            elif command == "evidence":

                self.evidence.show()

            elif command == "hint":

             self.show_hint()

            elif command == "notes":

                self.notes.show_notes()


            elif command == "add note":

             note_text = input("Enter note: ")

             self.notes.add_note(note_text)

            elif command == "submit report":

                report = ReportSystem(
                    self.case["solution"]
                )

                score = report.submit()

                print(
                    f"\nReport Score: "
                    f"{score}/3"
                )

                if score == 3:

                    self.evidence.submit()

                    print("\nCase Solved!")

                    print(
                        f"\n+{self.case['xp']} XP"
                    )

                    break

                elif score == 2:

                    print(
                        "\nGood Investigation."
                    )

                else:

                    print(
                        "\nInvestigation Incomplete."
                    )

            elif command == "exit":

                print(
                    "\nLeaving case..."
                )

                break

            else:

                print(
                    "\nUnknown command."
                )
