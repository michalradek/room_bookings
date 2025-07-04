import tkinter as tk
from room_bookings_backend import create_user, login

root = tk.Tk()
root.title("Room's bookings")
root.geometry("1200x700")
root.resizable(False, False)

def on_click_add():
    create_user(login_entry.get(), password_entry.get())

def on_click_login():
    state = login(login_entry.get(), password_entry.get())
    if state:
        login_frame.pack_forget()
        main_frame.pack()


#login frame
login_frame = tk.Frame(root)
login_label = tk.Label(login_frame, text="Enter login")
login_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Enter password")
password_entry = tk.Entry(login_frame, show="*")
login_button = tk.Button(login_frame, text="Log in", command=on_click_login)
new_user_button = tk.Button(login_frame, text="Create user", command=on_click_add)


login_label.pack(pady=10, fill="x")
login_entry.pack(pady=5, fill="x")
password_label.pack(pady=10, fill="x")
password_entry.pack(pady=5, fill="x")
login_button.pack(pady=10, fill="x")
new_user_button.pack(pady=10, fill="x")
login_frame.pack(expand=True)

main_frame = tk.Frame(root, bg="blue", width=200, height=200)


root.mainloop()