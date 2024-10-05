import tkinter
from tkinter import ttk
from tkinter import messagebox
import os 
import openpyxl
import sqlite3

def enter_data():
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
            print("Title: ",title,"Age: ",age,"District: ",nationality)
            print("# Course: ",numcourse, "Semester: ", numsemester)
            print("regestration Status: ", regestration_status)
            print("-----------------------------------------------------------")

            filepath = "F:\PROGRAMMING\MY PROJECTS\Tkinter PY\data1.xlsx"
            # if dont have file
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                #open xl workbook open object
                sheet = workbook.active
                heading = ["Title","First Name", "Last Name","Age","Nationality",
                           "# Courses","# Semester","Regestration Status"]
                sheet.append(heading)
                #append take list and attch it into excell sheet in row
                workbook.save(filepath)
                #save tha data
            
            workbook = openpyxl.load_workbook(filepath)
            #call fun load workbook 
            sheet = workbook.active
            sheet.append([title, firstname, lastname, age, nationality, 
                          numcourse, numsemester, regestration_status])
            
            workbook.save(filepath)
            #save the data in file


        else:
            tkinter.messagebox.showwarning(title="Error",
                                            message=" Firstname And Lastname are required!!")
    else:
        tkinter,messagebox.showwarning(title="Error",
                                       message="Terms & Conditions are not accepted!!")
        
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
            print("Title: ",title,"Age: ",age,"District: ",nationality)
            print("# Course: ",numcourse, "Semester: ", numsemester)
            print("regestration Status: ", regestration_status)
            print("-----------------------------------------------------------")

            #Create DB
            #create table  conncet db with name data
            conn = sqlite3.connect('data.db')
            table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data
                    (title TEXT, firstname TEXT, lastname TEXT, age INT,
                    nationality TEXT, regestration_status TEXT, num_courses INT,
                      num_semesters INT )
            '''
            #sql syntex
            conn.execute(table_create_query)
            # insert data need insert query and tuple
            data_insert_query = '''INSERT INTO Student_Data (Title, FirstName,
              LastName, Age, 
            Nationality, Regestration_Status, Num_courses, Num_semesters)
              VALUES(?, ?, ?, ?, ?, ?, ?, ?)'''
            data_insert_tuple = (title, firstname, lastname, age, nationality, 
                                 regestration_status, numcourse, numsemester)
            cursor = conn.cursor()
            #it is middle way btwn sqlite and actual DB exexute query and manage
            cursor.execute(data_insert_query, data_insert_tuple)

            conn.commit()
            #commit the changes in DB



            conn.close()
            #close connection



        else:
            tkinter.messagebox.showwarning(title="Error",
                                            message=" Firstname And Lastname are Required!!")
    else:
        tkinter,messagebox.showwarning(title="Error",
                                       message="Terms & Conditions are not accepted!!")        

window = tkinter.Tk()
window.title("DATA  ENTRY  FORM")

frame = tkinter.Frame(window, background="lemon chiffon")
frame.pack()

#saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information",borderwidth="10" ,
                                     foreground="black", font="bold", 
                                     background="light goldenrod")
user_info_frame.grid(row=0 , column=0, padx= 20 , pady=10 )

first_name_label = tkinter.Label(user_info_frame, text="First Name", 
                                  background="light goldenrod" ,
                                 foreground="purple", font="bold")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name",  
                                background="light goldenrod" ,
                                foreground="purple", font="bold")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title",  
                            background="light goldenrod",
                            foreground="purple", font="bold")
title_combobox = ttk.Combobox(user_info_frame,
                               values=["","Mr.","Ms.","Dr.", "Er."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)


age_label = tkinter.Label(user_info_frame, text="Age", 
                          background="light goldenrod",
                          foreground="purple", font="bold")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)


nationality_label = tkinter.Label(user_info_frame, text="District",
                                   background="light goldenrod",
                                  foreground="purple", font="bold")
nationality_ComboBox = ttk.Combobox(user_info_frame, values = ["Chamba", "Kangra", 
                                "Hamirpur", "Una","Bilaspur","Mandi","Kullu", 
                                "Lahul-Spiti", "Shimla","Solan", "Sirmour", "Kinnour"])
nationality_label.grid(row=2, column=1)
nationality_ComboBox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# saving Course Info
course_frame = tkinter.Frame(frame,  background="light goldenrod")
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

regestered_label = tkinter.Label(course_frame, text="Regestration Status", 
                                 background="light goldenrod",
                                 foreground="purple",
                                   font="bold")
#binding-----
reg_status_var = tkinter.StringVar(value="Not regestered")


regestered_check = tkinter.Checkbutton(course_frame, text="Currently Regestered", 
                                       background="light goldenrod",
                                        variable=reg_status_var, onvalue="Regestered",
                                          activebackground="indian red1",
                                          offvalue="Not Regestered",foreground="black")
regestered_label.grid(row=0, column=0)
regestered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="Completed Courses", 
                                  background="light goldenrod",foreground="purple",
                                    font="bold")
numcourses_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(course_frame, text="Semesters" , 
                                   background="light goldenrod",foreground="purple", 
                                   font="bold")
numsemesters_spinbox = tkinter.Spinbox(course_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

#Accept Terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions", 
                                 background="light goldenrod",
                                 foreground="purple")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                   variable= accept_var, onvalue="Accepted",
                                   activebackground="indian red" ,
                                   offvalue="Not Accepted",  
                                   background="light goldenrod")
terms_check.grid(row=0, column=0)

#Buttons
button = tkinter.Button(frame, text="Enter data (EXCEL)", activebackground="coral1",
                        background="springgreen",command = enter_data)
button.grid(row=3, column=0, sticky="news", padx=300, pady=10)

#Buttons Database
button = tkinter.Button(frame, text="Enter data (DATABASE)", command = enter_D_data, 
                        activebackground="coral1", background="springgreen",
                        )
button.grid(row=4, column=0, sticky="news", padx=200, pady=10)




window.mainloop()