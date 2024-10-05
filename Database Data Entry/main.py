import tkinter
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
import sqlite3



def enter_D_data():
    accepted = accept_var.get()

    if accepted=="Accepted":

        #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_ComboBox.get()

            #course info

            regestration_status = reg_status_var.get()
            numcourse = numcourses_spinbox.get()
            numsemester = numsemesters_spinbox.get()

            print("first Name: ", firstname,"Last Name: ", lastname)
            print("Title: ",title,"Age: ",age,"nationality: ",nationality)
            print("# Course: ",numcourse, "Semester: ", numsemester)
            print("regestration Status: ", regestration_status)
            print("-----------------------------------------------------------")

            #Create DB
            #create table  conncet db with name data
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                    (title TEXT, firstname TEXT, lastname TEXT, age INT,
                    nationality TEXT, regestration_status TEXT, num_courses INT, num_semesters INT )
            '''
            #sql syntex
            conn.execute(table_create_query)
            # insert data need insert query and tuple
            data_insert_query = '''INSERT INTO Student_Data (Title, FirstName, LastName, Age, 
            Nationality, Regestration_Status, Num_courses, Num_semesters) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (title, firstname, lastname, age, nationality, regestration_status, numcourse, numsemester)
            cursor = conn.cursor()
            #it is middle way btwn sqlite and actual DB exexute query and manage
            cursor.execute(data_insert_query, data_insert_tuple)

            conn.commit()
            #commit the changes in DB



            conn.close()
            #close connection



        else:
            tkinter.messagebox.showwarning(title="Error", message=" Firstname And Lastname are Required!!")
    else:
        tkinter,messagebox.showwarning(title="Error",message="Terms & Conditions are not accepted!!")

window = tkinter.Tk()
window.title("DATA ENTRY FORM")

frame = tkinter.Frame(window)
frame.pack()

#saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0 , column=0, padx= 20 , pady=10 )

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.","Ms.","Dr.", "Er."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="District")
nationality_ComboBox = ttk.Combobox(user_info_frame, values = ["Chamba", "Kangra", "Hamirpur", "Una","Bilaspur","Mandi","Kullu", "Lahul-Spiti", "Shimla","Solan", "Sirmour", "Kinnour"])
nationality_label.grid(row=2, column=1)
nationality_ComboBox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# saving Course Info
course_frame = tkinter.Frame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

regestered_label = tkinter.Label(course_frame, text="Regestration Status")
#binding-----
reg_status_var = tkinter.StringVar(value="Not Regestered")


regestered_check = tkinter.Checkbutton(course_frame, text="Currently Regestered", variable=reg_status_var, onvalue="Regestered", offvalue="Not Regestered")
regestered_label.grid(row=0, column=0)
regestered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="# Completed Semester")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(course_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept Terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable= accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Buttons
button = tkinter.Button(frame, text="Enter data", command = enter_D_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



window.mainloop()