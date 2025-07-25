# 🔐 SHA256 File Integrity Verifier

A simple Python project to check whether a file has been tampered with using SHA256 hashing. It stores and verifies hashes against saved records in a JSON file.

---

## 📌 Features

- Generate and store SHA256 hash of any file
- Verify a file's integrity by comparing its hash to a saved hash
- Uses JSON to store and manage hash records

---

## 🛠 Tech Stack

- Python 3.x
- Modules: `hashlib`, `json`, `os`

---

## 📁 File Structure

.
├── files/
│ └── test1.txt # Example file to verify
├── hash_records.json # Stores file hash records
├── save_file.py # Script to save file's hash
└── verify_file.py # Script to verify file integrity
