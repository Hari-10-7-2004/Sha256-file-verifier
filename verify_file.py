import hashlib
import json

def get_sha256_hash(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

file_path = "files/test1.txt"


with open("hash_records.json", "r") as f:
    hash_data = json.load(f)

original_hash = hash_data.get(file_path)

if not original_hash:
    print("No hash record found for this file.")
else:
    current_hash = get_sha256_hash(file_path)
    print(f"Original Hash: {original_hash}")
    print(f"Current  Hash: {current_hash}")

    if original_hash == current_hash:
        print(" File is safe. No changes detected.")
    else:
        print(" File has been tampered with!")
