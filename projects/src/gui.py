import tkinter as tk

root = tk.Tk()
root.title("Global Impact High School - SMS GUI")
root.geometry("500x400")

label = tk.Label(root, text="Welcome to the School Management System", font=("Arial", 12))
label.pack(pady=20)

btn_add = tk.Button(root, text="Add Student", width=25, command=add_student)
btn_add.pack(pady=10)

btn_view = tk.Button(root, text="View Students", width=25, command=view_students)
btn_view.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", width=25, command=root.destroy)
btn_exit.pack(pady=10)

root.mainloop()