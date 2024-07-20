import tkinter
from tkinter import ttk
from tkinter import messagebox
import os 
import openpyxl



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
            print("Title: ",title,"Age: ",age,"nationality: ",nationality)
            print("# Course: ",numcourse, "Semester: ", numsemester)
            print("regestration Status: ", regestration_status)
            print("-----------------------------------------------------------")

            filepath = "F:\PROGRAMMING\MY PROJECTS\Excell\data.xlsx"
            # if dont have file
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                #open xl workbook open object
                sheet = workbook.active
                heading = ["Title","First Name", "Last Name","Age","Nationality","# Courses","# Semester","Regestration Status"]
                sheet.append(heading)
                #append take list and attch it into excell sheet in row
                workbook.save(filepath)
                #save tha data
            
            workbook = openpyxl.load_workbook(filepath)
            #call fun load workbook 
            sheet = workbook.active
            sheet.append([title, firstname, lastname, age, nationality, numcourse, numsemester, regestration_status])
            
            workbook.save(filepath)
            #save the data in file


        else:
            tkinter.messagebox.showwarning(title="Error", message=" Firstname And Lastname are required!!")
    else:
        tkinter,messagebox.showwarning(title="Error",message="Terms & Conditions are not accepted!!")

window = tkinter.Tk()
window.title("DATA ENTRY  FORM")

frame = tkinter.Frame(window, bg="gray")
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


nationality_label = tkinter.Label(user_info_frame, text="nationality")
nationality_ComboBox = ttk.Combobox(user_info_frame, values = ["India", "Africa", "USA", "Antarctica","north America","England","South America"])
nationality_label.grid(row=2, column=1)
nationality_ComboBox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# saving Course Info
course_frame = tkinter.Frame(frame)
course_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

regestered_label = tkinter.Label(course_frame, text="Regestration Status")
#binding-----
reg_status_var = tkinter.StringVar(value="Not regestered")


regestered_check = tkinter.Checkbutton(course_frame, text="Currently regestered", variable=reg_status_var, onvalue="Regestered", offvalue="Not Regestered")
regestered_label.grid(row=0, column=0)
regestered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(course_frame, text="# Completed Courses")
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
terms_frame = tkinter.LabelFrame(frame, text="terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", variable= accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

#Buttons
button = tkinter.Button(frame, text="Enter data", command = enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



window.mainloop()