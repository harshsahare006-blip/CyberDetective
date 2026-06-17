import re

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        return "WEAK ❌", score
    elif score == 3 or score == 4:
        return "MEDIUM ⚠️", score
    else:
        return "STRONG 💪", score


def run():
    print("\n=== PASSWORD STRENGTH CHECKER ===")

    password = input("Enter password: ")
    strength, score = check_strength(password)

    print(f"\nStrength: {strength}")
    print(f"Score: {score}/5")