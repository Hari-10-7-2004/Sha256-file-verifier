# 🔐 SHA256 File Integrity Checker

Hi there! 👋  
This little Python project helps you check if a file has been changed or tampered with using SHA256 hash values.

---

## ✨ What it does

- 🔄 Generates SHA256 hash for a file
- 🧾 Saves it to a JSON file
- 🔍 Later checks if the file is the same or has been changed

---

## 📂 Files

- `save_file.py` → Saves the hash of your file
- `verify_file.py` → Compares your file's current hash with the saved one
- `hash_records.json` → Stores hash values
- `files/test1.txt` → Example file (you can try your own!)

---

## 🛠 How to Use

```bash
python save_file.py      # Save hash
python verify_file.py    # Check if file is still the same
