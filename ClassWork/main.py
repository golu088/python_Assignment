import tkinter as tk
import os
from organizer import organize_files 

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x250")

def submit_function():
    address =entry.get()
    print("Address is: \t", address)
    if os.path.exists(address):
        organize_files(address)

label = tk.Label(root,text="Enter Directory Address: ")
label.pack(pady=20)


entry=tk.Entry(root, width=30)
entry.pack(pady=5)

button= tk.Button(root, text="Submit", command=submit_function)
button.pack(pady=10)

root.mainloop()