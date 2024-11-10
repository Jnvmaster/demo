
##-----------------------import the required methodes-------------------------##

import mysql.connector as MyConn
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk


###--------------create login window--------##

def login():
    username = username_var.get()
    password = password_var.get()

    # Connect to the database to validate the credentials
    
    conn = MyConn.connect(host="localhost", user="root", password="pratik@05", database="student_manegment_system")
    my_cursor = conn.cursor()
    my_cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    result = my_cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Succses", "WELCOME")
        login_window.destroy()
         # Call the main application
    else:
        messagebox.showerror("Error", "Invalid username or password")



# Create the login window
login_window = tk.Tk()
login_window.iconbitmap("C:\\Users\\kafag\\Downloads\\stu.ico")
login_window.configure(bg="cyan4")
login_window.resizable(0,0)
login_window.title("Login page")
login_window.geometry("1400x700")




# Username and Password Variables
username_var = tk.StringVar()
password_var = tk.StringVar()


heading_label=tk.Label(login_window,text = "LOGIN PAGE" ,bg="cyan4",fg="black",font=("Arial",25,"bold"))
heading_label.place(x=530,y=110)

# Username Label and Entry
username_label = tk.Label(login_window, text="USERNAME" ,bg="cyan4",fg="black" ,font=("Lightning Script",15,"bold"))
username_label.place(x=580,y=270)
username_entry = tk.Entry(login_window, textvariable=username_var,bd=7,width=30,font=("Lightning Script",10,"bold"))
username_entry.place(x=545,y=300)

# Password Label and Entry
password_label = tk.Label(login_window, text="PASSWORD",bg="cyan4",fg="black",font=("Lightning Script",15,"bold"))
password_label.place(x=580,y=370)
password_entry = tk.Entry(login_window, textvariable=password_var, show="*",bd=7,width=30,font=("Lightning Script",10,"bold"))
password_entry.place(x=545,y=400)

# Login Button
login_button = tk.Button(login_window, text="LOGIN", command=login,bg="white",fg="black",width=15,bd=7,font=("Lightning Script",13,"bold"))
login_button.place(x=555,y=460)

# Start the login window
login_window.mainloop()










##--------------------------------creating the window---------------------

win=tk.Tk()
win.iconbitmap("C:\\Users\\kafag\\Downloads\\system student.ico")
win.title("STUDENT MANEGMENT SYSTEM")
win.geometry("1200x700")
win.resizable(0,0)

title_Label=tk.Label(win,text="STUDENT MANEGMENT SYSTEM",font=("Arial",30,"bold"),border=14,relief=tk.GROOVE,bg="black",foreground="white")
title_Label.pack(side=tk.TOP,fill=tk.X)

##-----------------------creating detail_frame----------------------##

detail_frame=tk.LabelFrame(win,text="ENTER DERAILS",font=("Arial",15,"bold"),bd=14,relief=tk.GROOVE,bg="grey",fg="black")
detail_frame.place(x=0,y=100,width=450,height=580)

##------------------------creating data_frame------------------------##


data_frame=tk.Frame(win,bd=14,relief=tk.GROOVE,bg="grey")
data_frame.place(x=500,y=100,width=730,height=500)


##-----------------------creating the string variable as string_var------------------------------------##


prn_number=tk.StringVar()
roll_no=tk.StringVar()
student_name=tk.StringVar()
class_var=tk.StringVar()
contact=tk.StringVar()
dob=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()

search_by=tk.StringVar()

### --------------------------Entry Label------------------------------##


prn_number_lbl=tk.Label(detail_frame,text=" PRN NUMBER",font=("Arial",15,"bold"),bg="grey",fg="black")
prn_number_lbl.grid(row=0,column=0,padx=2,pady=5,sticky="w")

prn_number_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=prn_number)
prn_number_ent.grid(row=0,column=1,padx=2,pady=3,sticky="w")


roll_no_lbl=tk.Label(detail_frame,text="ROLL NO",font=("Arial",15,"bold"),bg="grey",fg="black")
roll_no_lbl.grid(row=1,column=0,padx=2,pady=3,sticky="w")

roll_no_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=roll_no)
roll_no_ent.grid(row=1,column=1,padx=2,pady=3,sticky="w")

Student_name_lbl=tk.Label(detail_frame,text=" STUDENT NAME",font=("Arial",15,"bold"),bg="grey",fg="black")
Student_name_lbl.grid(row=2,column=0,padx=2,pady=3,sticky="w")

Student_name_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=student_name)
Student_name_ent.grid(row=2,column=1,padx=2,pady=3,sticky="w")

class_lbl=tk.Label(detail_frame,text=" CLASS",font=("Arial",15,"bold"),bg="grey",fg="black")
class_lbl.grid(row=3,column=0,padx=2,pady=3,sticky="w")

class_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=class_var)
class_ent.grid(row=3,column=1,padx=2,pady=3,sticky="w")

contact_lbl=tk.Label(detail_frame,text=" CONTACT",font=("Arial",15,"bold"),bg="grey",fg="black")
contact_lbl.grid(row=4,column=0,padx=2,pady=3,sticky="w")

contact_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=3,sticky="w")

dob_lbl=tk.Label(detail_frame,text=" DATE OF BIRTH",font=("Arial",15,"bold"),bg="grey",fg="black")
dob_lbl.grid(row=5,column=0,padx=2,pady=3,sticky="w")

dob_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=dob)
dob_ent.grid(row=5,column=1,padx=2,pady=3,sticky="w")

address_lbl=tk.Label(detail_frame,text="ADDRESS",font=("Arial",15,"bold"),bg="grey",fg="black")
address_lbl.grid(row=6,column=0,padx=2,pady=3,sticky="w")

address_ent=tk.Entry(detail_frame,bd=6,font=("Arial",15),bg="grey",fg="black",textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=3,sticky="w")

gender_lbl=tk.Label(detail_frame,text="GENDER",font=("Arial",15,"bold"),bg="grey",fg="black")
gender_lbl.grid(row=7,column=0,padx=2,pady=3,sticky="w")

gender_ent=ttk.Combobox(detail_frame,font=("Arial",15),textvariable=gender)
gender_ent["values"]=("MALE","FEMALE","OTHERS")
gender_ent.grid(row=7,column=1,padx=2,pady=5,sticky="w")



##-------------------------creating the function to impliment the working of buttons--------------------##



def student_data():
    conn=MyConn.connect(host="localhost",user="root",password="pratik@05",database="student_manegment_system")
    my_cursor=conn.cursor()
    my_cursor.execute("select * from data")
    rows=my_cursor.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",tk.END,values=row)
        conn.commit()
    conn.close()




        



def add_func():
    if prn_number.get()=="" or student_name.get()=="" or class_var.get()=="":
        messagebox.showerror("error","plese fill the required data")
    else:
        conn=MyConn.connect(host="localhost",user="root",password="pratik@05",database="student_manegment_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s)",(prn_number.get(),
                                                                              roll_no.get(),
                                                                              student_name.get(),
                                                                              class_var.get(),
                                                                              contact.get(),
                                                                              dob.get(),
                                                                              address.get(),
                                                                              gender.get()
                                                                          ))
        conn.commit()
        conn.close()

        student_data()

       




def get_cursor(event):
    cursor_row = student_table.focus()
    if not cursor_row:  # Check if a row is selected
        return
    content = student_table.item(cursor_row)
    row = content["values"]
    if len(row) < 8:  # Ensure there are enough elements
        return
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content["values"]
    prn_number.set(row[0])
    roll_no.set(row[1])
    student_name.set(row[2])
    class_var.set(row[3])
    contact.set(row[4])
    dob.set(row[5])
    address.set(row[6])
    gender.set(row[7])


def clear_func():
    prn_number.set("")
    roll_no.set("")
    student_name.set("")
    class_var.set("")
    contact.set("")
    dob.set("")
    address.set("")
    gender.set("")
    



def delete_func():
    if roll_no.get() == "":
        messagebox.showerror("Error", "Select a student to delete")
    else:
        conn = MyConn.connect(host="localhost", user="root", password="pratik@05", database="student_manegment_system")
        my_cursor = conn.cursor()
        my_cursor.execute("DELETE FROM data WHERE roll_no=%s", (roll_no.get(),))
        conn.commit()
        conn.close()
        student_data()
        clear_func()


def update_func():
    
    conn=MyConn.connect(host="localhost",user="root",password="pratik@05",database="student_manegment_system")
    my_cursor=conn.cursor()
    my_cursor.execute("update data SET prn=%s,student=%s,class=%s,contact=%s,date_of_birth=%s,address=%s,gender=%s where roll_no=%s",(prn_number.get(), student_name.get(), class_var.get(),contact.get(),dob.get(),address.get(),gender.get(),roll_no.get()))
                                                                                                    
    if my_cursor.rowcount == 0:
        messagebox.showwarning("Warning", "No record was updated. Check if the roll number exists.")
    else:
        conn.commit()
        messagebox.showinfo("Success", "Student data updated successfully.")


\
                     
    student_data()
    conn.close()  
    clear_func()    



def search_func():
    search_value = search_by.get()
    search_term = prn_number.get()

    ##if search_value == "" or search_term == "":
       ## messagebox.showerror("Error", "Please select a search criterion and enter a value")
        ##return

    query = f"SELECT * FROM data WHERE {search_value} LIKE %s"
    conn = MyConn.connect(host="localhost", user="root", password="pratik@05", database="student_manegment_system")
    my_cursor = conn.cursor()
    my_cursor.execute(query, ("%" + search_term + "%",))
    rows = my_cursor.fetchall()

    student_table.delete(*student_table.get_children())
    for row in rows:
        student_table.insert("", tk.END, values=row)

    conn.close()




             

    add_window=tk.Tk()
    add_window.grab_set()
    
    prn_label=tk.Label(add_window,text="PRN NUMBER",font=("Arial",15,"bold"))
    prn_label.grid(row=0,column=0,padx=30,pady=15)
    prn_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    prn_entry.grid(row=0,column=1,padx=10,pady=15)

    
    roll_no_label=tk.Label(add_window,text="ROLL NUMBER",font=("Arial",15,"bold"))
    roll_no_label.grid(row=1,column=0,padx=30,pady=15)
    roll_no_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    roll_no_entry.grid(row=1,column=1,padx=10,pady=15)


   
    student_name_label=tk.Label(add_window,text="STUDENT NAME",font=("Arial",15,"bold"))
    student_name_label.grid(row=2,column=0,padx=30,pady=15)
    student_name_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    student_name_entry.grid(row=2,column=1,padx=10,pady=15)
    

    class_label=tk.Label(add_window,text="CLASS",font=("Arial",15,"bold"))
    class_label.grid(row=3,column=0,padx=30,pady=15)
    class_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    class_entry.grid(row=3,column=1,padx=10,pady=15)

    
    contact_label=tk.Label(add_window,text="CONTACT",font=("Arial",15,"bold"))
    contact_label.grid(row=4,column=0,padx=30,pady=15)
    contact_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    contact_entry.grid(row=4,column=1,padx=10,pady=15)

    
    dob_label=tk.Label(add_window,text="DATE OF BIRTH",font=("Arial",15,"bold"))
    dob_label.grid(row=5,column=0,padx=30,pady=15)
    dob_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    dob_entry.grid(row=5,column=1,padx=10,pady=15)

   
    address_label=tk.Label(add_window,text="ADDRESS",font=("Arial",15,"bold"))
    address_label.grid(row=0,column=0,padx=30,pady=15)
    address_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    address_entry.grid(row=0,column=1,padx=10,pady=15)

    
    gender_label=tk.Label(add_window,text="GENDERx",font=("Arial",15,"bold"))
    gender_label.grid(row=6,column=0,padx=30,pady=15)
    gender_entry=tk.Entry(add_window,font=("Arial",15,"bold"),width=24)
    gender_entry.grid(row=6,column=1,padx=10,pady=15)

    submit_button=ttk.Button(add_window,text="SUBMIT",command=student_data)
    submit_button.grid(row=7,columnspan=2)
   




        
    



##----------------------------creating button_frame------------------------##

        

button_frame=tk.Frame(detail_frame,bd=10,bg="white",relief=tk.GROOVE)
button_frame.place(x=30,y=390,width=365,height=135)


##----------------------------creating the buttons----------------------------##


add_btn=tk.Button(button_frame,bg="grey",text="ADD",font=("Aieal",13,"bold"),bd=7,width=12,command= add_func)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn=tk.Button(button_frame,bg="grey",text="UPDATE",font=("Aieal",13,"bold"),bd=7,width=12,command=update_func)
update_btn.grid(row=0,column=1,padx=50,pady=2)

delete_btn=tk.Button(button_frame,bg="grey",text="DELETE",font=("Aieal",13,"bold"),bd=7,width=12,command=delete_func)
delete_btn.grid(row=1,column=0,padx=2,pady=20)

clear_btn=tk.Button(button_frame,bg="grey",text="CLEAR",font=("Aieal",13,"bold"),bd=7,width=12,command=clear_func)
clear_btn.grid(row=1,column=1,padx=50,pady=20)

##---------------------------creating sreach_frame and search_Label and sreach_button----------------------------##


search_frame=tk.Frame(data_frame,bg="grey",bd=7,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_label=tk.Label(search_frame,text="SEARCH",bg="grey",font=("Arial",15,"bold"))
search_label.grid(row=0,column=0,padx=2,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",10),width=10,textvariable=search_by)
search_in["values"]=("PRN","ROLL_NO","STUDENT","CLASS","CONTACT","DATE_OF_BIRTH","ADDRESS","GENDER")
search_in.grid(row=0,column=1,padx=12,pady=5,sticky="w")

search_entry=tk.Entry(search_frame,font=("Arial",10,"bold"),width=10)
search_entry.grid(row=0,column=2,padx=10,pady=15)


search_btn=tk.Button(search_frame,bg="grey",text="search",font=("Aieal",15,"bold"),bd=7,width=10,height=0,command=search_func)
search_btn.grid(row=0,column=3,padx=20,pady=7)

show_all_btn=tk.Button(search_frame,bg="grey",text="show all",font=("Aieal",15,"bold"),bd=7,width=10,height=0,command=student_data)
show_all_btn.grid(row=0,column=4,padx=40,pady=2) 

##------------------------------creating main_frame---------------------##


main_frame=tk.Frame(data_frame,bd=14,relief=tk.GROOVE,bg="grey")
main_frame.pack(fill=tk.BOTH,expand=True)

##--------------------------------creating scrollbar------------------------------##

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("PRN NUMBER","ROLL NO","STUDENT","CLASS","CONTACT","DATE OF BIRTH","ADDRESS","GENDER"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

##----------------------------creating heading--------------------------##

student_table.heading("PRN NUMBER",text="PRN NUMBER")
student_table.heading("ROLL NO",text= "ROLL NO")
student_table.heading("STUDENT",text="STUDENT")
student_table.heading("CLASS",text="CLASS")
student_table.heading("CONTACT",text="CONTACT")
student_table.heading("DATE OF BIRTH",text= "DATE OF BIRTH")
student_table.heading("ADDRESS",text="ADDRESS")
student_table.heading("GENDER",text="GENDER")


student_table["show"]="headings"
student_table.column("PRN NUMBER",width=100)
student_table.column("ROLL NO",width=100)
student_table.column("STUDENT",width=100)
student_table.column("CLASS",width=100)
student_table.column("CONTACT",width=100)
student_table.column("DATE OF BIRTH",width=100)
student_table.column("ADDRESS",width=110)
student_table.column("GENDER",width=100)



student_table.pack(fill=tk.BOTH,expand=True)

student_data()


student_table.bind("<ButtonRelease-1>",get_cursor)




win.mainloop()
