
#STUDENT MANAGEMENT SYSTEM

from functools import partial
from tkinter import *
from tkinter import messagebox
import pymysql
import custom as cs
import credentials as cr


class Management:

    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("800x530")
        self.window.config(bg = "white")

        
        #title
        self.lb1 = Label(self.window, text="Student Management System", font=("times new roman", 40, "bold"))
        self.lb1.pack()


        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font = cs.font
       

        # User Credentials
        self.host = cr.host
        self.user = cr.user
        self.password = cr.password
        self.database = cr.database


        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=70, width=540, relheight = 1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg = self.color_2)
        self.frame_2.place(x=540,y=70,relwidth=1, relheight=1)

        # Buttons

        self.add_bt = Button(self.frame_2, text='Add', font=(self.font, 12), bd=2, command=self.AddStudent, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=40,width=100)
        self.view_bt = Button(self.frame_2, text='View', font=(self.font, 12), bd=2, command=self.GetRoll_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=100,width=100)
        self.update_bt = Button(self.frame_2, text='Update', font=(self.font, 12), bd=2, command=self.GetRoll_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=160,width=100)
        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font, 12), bd=2, command=self.GetRoll_Delete,cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=220,width=100)
        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=280,width=100)
        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font, 12), bd=2, command=self.Exit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=68,y=340,width=100)


    #Widgets for adding student data

    def AddStudent(self):

        self.ClearScreen()

        self.rollno = Label(self.frame_1, text="Roll Number", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        self.rollno_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.rollno_entry.place(x=40,y=60, width=200)

        self.firstname = Label(self.frame_1, text="First Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.firstname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.firstname_entry.place(x=300,y=60, width=200)

        self.lastname = Label(self.frame_1, text="Last Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.lastname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.lastname_entry.place(x=40,y=130, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=300,y=130, width=200)

        self.branch = Label(self.frame_1, text="Branch", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.branch_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.branch_entry.place(x=40,y=200, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=300,y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40,y=270, width=200)

        self.address = Label(self.frame_1, text="Address", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.address_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.address_entry.place(x=300,y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40,y=340, width=200)

        self.email = Label(self.frame_1, text="E-mail", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300,y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font, 12), bd=2, command=self.Submit, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=389,width=100)


    #Get the contact number to show a student details

    def GetRoll_View(self):

        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter roll number to view details", font=(self.font, 18, "bold"), bg=self.color_1).place(x=90,y=50)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font, 10), bd=2, command=self.CheckRoll_View, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=180,width=80)


    #To update a student details, get the contact number

    def GetRoll_Update(self):

        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter roll number to update details", font=(self.font, 18, "bold"), bg=self.color_1).place(x=90,y=50)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font, 10), bd=2, command=self.CheckRoll_Update, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=180,width=80)


    #Get the contact number to delete a student record

    def GetRoll_Delete(self):

        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter roll number to delete details", font=(self.font, 18, "bold"), bg=self.color_1).place(x=100,y=50)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font, 10), bd=2, command=self.DeleteData, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=220,y=180,width=80)


    #Remove all widgets from the frame 1

    def ClearScreen(self):

        for widget in self.frame_1.winfo_children():
            widget.destroy()

    #Exit window

    def Exit(self):
        self.window.destroy()

    
    #Checks whether the contact number is available or not. If available, the function calls the 'ShowDetails' function to display the result.
    
    def CheckRoll_View(self):

        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your roll number",parent=self.window)

        else:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cu = con.cursor()
                cu.execute("select * from student_register where rollno=%s", self.getInfo_entry.get())
                row=cu.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll number doesn't exists",parent=self.window)
                else:
                    self.ShowDetails(row)
                    con.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    
    #Checks whether the contact number is available or not. If available, the function calls the 'GetUpdateDetails' function to get the new data to perform update operation.
    
    def CheckRoll_Update(self):

        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your roll number",parent=self.window)

        else:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cu = con.cursor()
                cu.execute("select * from student_register where rollno=%s", self.getInfo_entry.get())
                row=cu.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll number doesn't exists",parent=self.window)
                else:
                    self.GetUpdateDetails(row)
                    con.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    
    #Clears a student record

    def DeleteData(self):

        if self.getInfo_entry.get() == "":
            messagebox.showerror("Error!", "Please enter your roll number",parent=self.window)

        else:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cu = con.cursor()
                cu.execute("select * from student_register where rollno=%s", self.getInfo_entry.get())
                row=cu.fetchone()
                
                if row == None:
                    messagebox.showerror("Error!","Roll number doesn't exists",parent=self.window)

                else:
                    cu.execute("delete from student_register where rollno=%s", self.getInfo_entry.get())
                    con.commit()
                    messagebox.showinfo('Done!', "The data has been deleted")
                    con.close()
                    self.ClearScreen()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    #Gets the data that the user wants to update to perform the update operation

    def GetUpdateDetails(self, row):

        self.ClearScreen()

        rollno = Label(self.frame_1, text="Roll Number", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        rollno_data = Label(self.frame_1, text=row[0], font=(self.font, 10)).place(x=40, y=60,width=200)

        self.firstname = Label(self.frame_1, text="First Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        self.firstname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.firstname_entry.insert(0, row[1])
        self.firstname_entry.place(x=300,y=60, width=200)

        self.lastname = Label(self.frame_1, text="Last Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        self.lastname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.lastname_entry.insert(0, row[2])
        self.lastname_entry.place(x=40,y=130, width=200)

        self.course = Label(self.frame_1, text="Course", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.insert(0, row[3])
        self.course_entry.place(x=300,y=130, width=200)

        self.branch = Label(self.frame_1, text="Branch", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        self.branch_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.branch_entry.insert(0, row[4])
        self.branch_entry.place(x=40,y=200, width=200)

        self.year = Label(self.frame_1, text="Year", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.insert(0, row[5])
        self.year_entry.place(x=300,y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.insert(0, row[6])
        self.gender_entry.place(x=40,y=270, width=200)

        self.address = Label(self.frame_1, text="Address", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        self.address_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.address_entry.insert(0, row[7])
        self.address_entry.place(x=300,y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.insert(0, row[8])
        self.contact_entry.place(x=40,y=340, width=200)

        self.email = Label(self.frame_1, text="E-mail", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.insert(0, row[9])
        self.email_entry.place(x=300,y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font, 12), bd=2, command=partial(self.UpdateDetails, row), cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=160,y=389,width=100)
        self.cancel_bt = Button(self.frame_1, text='Cancel', font=(self.font, 12), bd=2, command=self.ClearScreen, cursor="hand2", bg=self.color_2,fg=self.color_3).place(x=280,y=389,width=100)

    
    #Within frame 1, it displays information about a student

    def ShowDetails(self, row):

        self.ClearScreen()

        rollno = Label(self.frame_1, text="Roll Number", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=30)
        rollno_data = Label(self.frame_1, text=row[0], font=(self.font, 10)).place(x=40, y=60,width=200)

        firstname = Label(self.frame_1, text="First Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=30)
        firstname_data = Label(self.frame_1, text=row[1], font=(self.font, 10)).place(x=300, y=60,width=200)

        lastname = Label(self.frame_1, text="Last Name", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=100)
        lastname_data = Label(self.frame_1, text=row[2], font=(self.font, 10)).place(x=40, y=130,width=200)

        course = Label(self.frame_1, text="Course", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=100)
        course_data = Label(self.frame_1, text=row[3], font=(self.font, 10)).place(x=300, y=130,width=200)

        branch = Label(self.frame_1, text="Branch", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=170)
        branch_data = Label(self.frame_1, text=row[4], font=(self.font, 10)).place(x=40, y=200,width=200)

        year = Label(self.frame_1, text="Year", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=170)
        year_data = Label(self.frame_1, text=row[5], font=(self.font, 10)).place(x=300, y=200,width=200)

        address = Label(self.frame_1, text="Gender", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=240)
        address_data = Label(self.frame_1, text=row[6], font=(self.font, 10)).place(x=40, y=270,width=200)

        birth = Label(self.frame_1, text="Address", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=240)
        birth_data = Label(self.frame_1, text=row[7], font=(self.font, 10)).place(x=300, y=270,width=200)

        contact = Label(self.frame_1, text="Contact", font=(self.font, 15, "bold"), bg=self.color_1).place(x=40,y=310)
        contact_data = Label(self.frame_1, text=row[8], font=(self.font, 10)).place(x=40, y=340,width=200)

        email = Label(self.frame_1, text="E-mail", font=(self.font, 15, "bold"), bg=self.color_1).place(x=300,y=310)
        email_data = Label(self.frame_1, text=row[9], font=(self.font, 10)).place(x=300, y=340,width=200)
        

    #Updates student data

    def UpdateDetails(self, row):

        if self.firstname_entry.get() == "" or self.lastname_entry.get() == "" or self.course_entry.get() == "" or self.branch_entry.get() == "" or self.year_entry.get() == "" or self.gender_entry.get() == "" or self.address_entry.get() == "" or self.contact_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        else:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cu = con.cursor()
                cu.execute("select * from student_register where rollno=%s", row[0])
                row=cu.fetchone()

                if row==None:
                    messagebox.showerror("Error!","The roll number doesn't exists",parent=self.window)

                else:
                    
                    cu.execute("update student_register set firstname=%s,lastname=%s, course=%s, branch=%s, year=%s, gender=%s, address=%s, contact=%s, email=%s where rollno=%s",
                                        (
                                            self.firstname_entry.get(),
                                            self.lastname_entry.get(),
                                            self.course_entry.get(),
                                            self.branch_entry.get(),
                                            self.year_entry.get(),
                                            self.gender_entry.get(),
                                            self.address_entry.get(),
                                            self.contact_entry.get(),
                                            self.email_entry.get(),
                                            row[0]
                                        ))

                    con.commit()
                    con.close()
                    messagebox.showinfo('Done!', "The data has been updated")
                    self.ClearScreen()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)
    
    
    #It adds the information of new students

    def Submit(self):

        if self.rollno_entry.get() == "" or self.firstname_entry.get() == "" or self.lastname_entry.get() == "" or self.course_entry.get() == "" or self.branch_entry.get() == "" or self.year_entry.get() == "" or self.gender_entry.get() == "" or self.address_entry.get() == "" or self.contact_entry.get() == "" or self.email_entry.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)

        else:
            try:
                con = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
                cu = con.cursor()
                cu.execute("select * from student_register where rollno=%s", self.contact_entry.get())
                row=cu.fetchone()

                if row!=None:
                    messagebox.showerror("Error!","The roll number is already exists, please try again with another roll number",parent=self.window)
                else:
                    cu.execute("insert into student_register (rollno,firstname,lastname,course,branch,year,gender,address,contact,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        
                                        (
                                            self.rollno_entry.get(),
                                            self.firstname_entry.get(),
                                            self.lastname_entry.get(),
                                            self.course_entry.get(),
                                            self.branch_entry.get(),
                                            self.year_entry.get(),
                                            self.gender_entry.get(),
                                            self.address_entry.get(),
                                            self.contact_entry.get(),
                                            self.email_entry.get()  
                                        ))

                    con.commit()
                    con.close()
                    messagebox.showinfo('Done!', "The data has been submitted")
                    self.reset_fields()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)


    #Reset all the entry fields

    def reset_fields(self):

        self.rollno_entry.delete(0, END)
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.branch_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.gender_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.email_entry.delete(0, END)


# The main function

if __name__ == "__main__":
    root = Tk()
    obj = Management(root)
    root.mainloop()