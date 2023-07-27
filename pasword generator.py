#Task 3 Given by CodSoft
#Python program to creat a password generator

import tkinter as tk
from tkinter import messagebox
import random
import string


entry_username = None
entry_password_length = None
entry_generated_password = None

def generate_password():
    global entry_generated_password
    password_length = int(entry_password_length.get())
    if password_length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    entry_generated_password.delete(0, tk.END)
    entry_generated_password.insert(tk.END, generated_password)

def accept_password():
    global entry_username, entry_generated_password
    username = entry_username.get()
    password = entry_generated_password.get()
    if not username or not password:
        messagebox.showwarning("Warning", "Please enter username and generate a password.")
        return


    messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")

def reset_fields():
    global entry_username, entry_password_length, entry_generated_password
    entry_username.delete(0, tk.END)
    entry_password_length.delete(0, tk.END)
    entry_generated_password.delete(0, tk.END)

def main():
    global entry_username, entry_password_length, entry_generated_password
    root = tk.Tk()
    root.title("Password Generator")


    heading_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
    heading_label.grid(row=0, column=0, columnspan=3, pady=20)


    label_username = tk.Label(root, text="Enter Username:")
    label_username.grid(row=1, column=0, sticky=tk.E)

    entry_username = tk.Entry(root, width=30)
    entry_username.grid(row=1, column=1, columnspan=2)


    label_password_length = tk.Label(root, text="Enter Password Length:")
    label_password_length.grid(row=2, column=0, sticky=tk.E)

    entry_password_length = tk.Entry(root, width=10)
    entry_password_length.grid(row=2, column=1)


    label_generated_password = tk.Label(root, text="Generated Password:")
    label_generated_password.grid(row=3, column=0, sticky=tk.E)

    entry_generated_password = tk.Entry(root, width=30)
    entry_generated_password.grid(row=3, column=1, columnspan=2)


    button_generate_password = tk.Button(root, text="Generate Password", command=generate_password)
    button_generate_password.grid(row=4, column=0, padx=5, pady=10)

    button_accept_password = tk.Button(root, text="Accept", command=accept_password)
    button_accept_password.grid(row=4, column=1, padx=5, pady=10)

    button_reset_fields = tk.Button(root, text="Reset", command=reset_fields)
    button_reset_fields.grid(row=4, column=2, padx=5, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
