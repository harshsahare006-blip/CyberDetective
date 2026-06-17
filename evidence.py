class EvidenceLocker:

    def __init__(self):
        self.evidence = []

    def add(self, item):
        if item not in self.evidence:
            self.evidence.append(item)

    def show(self):

        if not self.evidence:
            print("\nNo evidence collected yet.")
            return

        print("\n===== EVIDENCE LOCKER =====")

        for index, item in enumerate(
            self.evidence,
            start=1
        ):
            print(f"{index}. {item}")