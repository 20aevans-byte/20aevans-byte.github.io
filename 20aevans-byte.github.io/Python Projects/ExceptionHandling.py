# 4.1.1.9 Exception Handling Assessment

# --- Data type check ---
while True:
    try:
        age = int(input("Enter your age (integer): "))
        print("Data type check passed!")
        break
    except ValueError:
        print("Invalid data type. Please enter an integer.")

# --- Range check ---
while True:
    try:
        score = int(input("Enter your score (0-100): "))
        if 0 <= score <= 100:
            print("Range check passed!")
            break
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid integer.")

# --- Limit check ---
while True:
    amount = float(input("Enter withdrawal amount (max 500): "))
    if amount <= 500:
        print("Limit check passed!")
        break
    else:
        print("Amount exceeds the allowed limit.")

# --- Length check ---
while True:
    username = input("Enter username (3-10 chars): ")
    if 3 <= len(username) <= 10:
        print("Length check passed!")
        break
    else:
        print("Username must be between 3 and 10 characters.")

# --- Format check ---
import re
while True:
    email = input("Enter your email: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Format check passed!")
        break
    else:
        print("Invalid email format.")

# --- Presence check ---
while True:
    name = input("Enter your name: ").strip()
    if name:
        print("Presence check passed!")
        break
    else:
        print("Name cannot be empty.")

# --- Existence check ---
existing_users = ["alice", "bob", "charlie"]
while True:
    user = input("Enter username to log in: ").lower()
    if user in existing_users:
        print("Existence check passed!")
        break
    else:
        print("Username not found.")

# --- Uniqueness check ---
registered_emails = ["a@example.com", "b@example.com"]
while True:
    new_email = input("Enter new email: ").lower()
    if new_email not in registered_emails:
        print("Uniqueness check passed!")
        break
    else:
        print("Email already registered.")

# --- Consistency check ---
while True:
    password = input("Enter password: ")
    confirm = input("Confirm password: ")
    if password == confirm:
        print("Consistency check passed!")
        break
    else:
        print("Passwords do not match.")

# --- Extension check (Check digit) ---
while True:
    isbn = input("Enter 10-digit ISBN: ")
    if len(isbn) == 10 and isbn[:-1].isdigit():
        # Check digit validation
        total = sum((i + 1) * int(x) for i, x in enumerate(isbn[:-1]))
        check = total % 11
        if str(check) == isbn[-1] or (check == 10 and isbn[-1] == 'X'):
            print("Check digit valid!")
            break
        else:
            print("Invalid check digit.")
    else:
        print("Invalid ISBN format.")