import random
import string
import tkinter as tk
from tkinter import messagebox
import os
import sys

# ---------------- Get Correct App Path ----------------
def get_app_path():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)  # EXE location
    else:
        return os.path.dirname(os.path.abspath(__file__))  # .py location

# ---------------- Password Strength ----------------
def check_strength(password):
    strength = 0

    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Medium"
    else:
        return "Strong"

# ---------------- Generate Password ----------------
def generate_password():
    try:
        length = int(entry_length.get())

        if length < 6:
            messagebox.showwarning("Warning", "Password must be at least 6 characters")
            return

        characters = ""

        if var_letters.get():
            characters += string.ascii_letters
        if var_numbers.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)

        strength = check_strength(password)
        label_strength.config(text=f"Strength: {strength}")

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")

# ---------------- Copy Password ----------------
def copy_password():
    password = entry_result.get()
    if password == "":
        messagebox.showwarning("Warning", "No password to copy")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---------------- Save Password ----------------
def save_password():
    password = entry_result.get()
    if password == "":
        messagebox.showwarning("Warning", "No password to save")
        return

    base_path = get_app_path()
    file_path = os.path.join(base_path, "passwords.txt")

    with open(file_path, "a") as file:
        file.write(password + "\n")

    messagebox.showinfo("Saved", f"Password saved in:\n{file_path}")

# ---------------- Open Saved Passwords ----------------
def open_passwords():
    base_path = get_app_path()
    file_path = os.path.join(base_path, "passwords.txt")

    if not os.path.exists(file_path):
        messagebox.showwarning("Warning", "No saved passwords found!")
        return

    try:
        os.startfile(file_path)  # Windows
    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- Clear Saved Passwords ----------------
def clear_passwords():
    base_path = get_app_path()
    file_path = os.path.join(base_path, "passwords.txt")

    if not os.path.exists(file_path):
        messagebox.showwarning("Warning", "No file to clear!")
        return

    confirm = messagebox.askyesno("Confirm", "Delete all saved passwords?")
    
    if confirm:
        open(file_path, "w").close()
        messagebox.showinfo("Success", "All passwords cleared!")

# ---------------- UI Window ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")

# Length
tk.Label(root, text="Password Length:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

# Options
var_letters = tk.BooleanVar()
var_numbers = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=var_letters).pack()
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack()

# Generate
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result
entry_result = tk.Entry(root, width=30)
entry_result.pack()

# Strength
label_strength = tk.Label(root, text="Strength: ")
label_strength.pack()

# Buttons
tk.Button(root, text="Copy", command=copy_password).pack(pady=5)
tk.Button(root, text="Save Password", command=save_password).pack(pady=5)
tk.Button(root, text="Open Saved Passwords", command=open_passwords).pack(pady=5)
tk.Button(root, text="Clear Saved Passwords", command=clear_passwords).pack(pady=5)

# Run
root.mainloop()