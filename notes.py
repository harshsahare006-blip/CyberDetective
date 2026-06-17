class NotesManager:

    def __init__(self):
        self.notes = []

    def add_note(self, note):

        if note.strip():
            self.notes.append(note)

            print("\nNote saved.")

    def show_notes(self):

        if not self.notes:
            print("\nNo notes available.")
            return

        print("\n===== CASE NOTES =====")

        for index, note in enumerate(
            self.notes,
            start=1
        ):
            print(f"{index}. {note}")