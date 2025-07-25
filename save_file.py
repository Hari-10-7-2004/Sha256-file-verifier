import hashlib
import json
import os

def get_sha256_hash(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        return hashlib.sha256(data).hexdigest()

file_path = "files/test1.txt"  

hash_value = get_sha256_hash(file_path)

hash_file = "hash_records.json"
if os.path.exists(hash_file):
    with open(hash_file, "r") as f:
        try:
            hash_data = json.load(f)
        except json.JSONDecodeError:
            hash_data = {}  
else:
    hash_data = {}

hash_data[file_path] = hash_value

with open(hash_file, "w") as f:
    json.dump(hash_data, f, indent=4)

print(f"Hash stored for {file_path}: {hash_value}")
