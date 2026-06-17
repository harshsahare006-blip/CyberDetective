import hashlib

def detect_hash_type(hash_value):
    length = len(hash_value)

    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    else:
        return "Unknown"


def generate_hash(text, hash_type="sha256"):
    hash_type = hash_type.lower()

    if hash_type == "md5":
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()


def run():   # ✅ THIS IS REQUIRED
    print("\n=== HASH CHECKER ===")

    print("1. Generate Hash")
    print("2. Detect Hash Type")

    choice = input("Choose: ")

    if choice == "1":
        text = input("Enter text: ")
        htype = input("Hash type (md5/sha1/sha256): ")
        print("Hash:", generate_hash(text, htype))

    elif choice == "2":
        h = input("Enter hash: ")
        print("Detected:", detect_hash_type(h))

    else:
        print("Invalid choice")