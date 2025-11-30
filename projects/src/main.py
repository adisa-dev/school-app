import tkinter as tk

root = tk.Tk()
root.title("Global Impact High School - SMS GUI")
root.geometry("500x400")

label = tk.Label(root, text="Welcome to the School Management System GUI!", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
