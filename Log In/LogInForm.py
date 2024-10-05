import tkinter
from tkinter import messagebox


window=tkinter.Tk()
window.title("Login Form")
window.geometry('400x500')
window.configure(bg='#333333')

frame = tkinter.Frame(bg="#333333")

def login():
    username = "john"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You Succefully Login")
    else:
        messagebox.showerror(title="Error", message="Invalid Login")

#creating Widgets
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg="white", font=("Aeial",30))
username_label = tkinter.Label(frame, text="Username",bg='#333333', fg="white", font=("Aeial",16))
username_entry = tkinter.Entry(frame, font=("Aeial",16))
password_entry = tkinter.Entry(frame, show="*", font=("Aeial",16))
password_label = tkinter.Label(frame, text="Password", bg='#333333', fg="white", font=("Aeial",16))
login_button = tkinter.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Aeial",16), command=login)

#Placing Widgets on screen
#sticky take space in North south west soutn news
#pady=40 is add space in y direction

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0, pady=20)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()




window.mainloop()
