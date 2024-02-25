import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, difficulty):
    if difficulty == "Easy":
        characters = string.ascii_letters + string.digits
    elif difficulty == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        characters = string.ascii_letters + string.digits + string.punctuation + string.hexdigits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def fetch_password():
    length = int(length_entry.get())
    difficulty = difficulty_combobox.get()
    password = generate_password(length, difficulty)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Colorful Password Fetcher")
root.geometry("400x200")  # Set initial size of the window

# Center the window on the screen
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

# Create a frame to contain the input fields
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, padx=10, pady=10)

# Create input fields inside the frame
length_label = ttk.Label(frame, text="Password Length:", foreground="blue")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(frame)
length_entry.grid(row=0, column=1, padx=5, pady=5)

difficulty_label = ttk.Label(frame, text="Difficulty:", foreground="blue")
difficulty_label.grid(row=1, column=0, padx=5, pady=5)
difficulty_combobox = ttk.Combobox(frame, values=["Easy", "Medium", "Hard"])
difficulty_combobox.current(0)
difficulty_combobox.grid(row=1, column=1, padx=5, pady=5)

password_label = ttk.Label(frame, text="Generated Password:", foreground="blue")
password_label.grid(row=2, column=0, padx=5, pady=5)
password_entry = ttk.Entry(frame)
password_entry.grid(row=2, column=1, padx=5, pady=5)

fetch_button = ttk.Button(frame, text="Fetch Password", command=fetch_password)
fetch_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main loop
root.mainloop()
