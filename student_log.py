from tkinter import *
import mysql.connector as mysql
from tkinter import messagebox

'''try:
    cur_obj.execute("create database STUDENT")
except Exception as e:
    print(e)
print("Database created successfully!")
'''
'''try:
    cur_obj.execute("create table STUDENT (user_index int(11) primary key auto_increment,"
                    "STUDENT_ID int(3),"
                    "STUDENT_NAME varchar(30),"
                    "STUDENT_DOB varchar(10),"
                    "STUDENT_DOJ varchar(10))")
except Exception as e:
    print(e)#
print("Table created Successfully!")'''


root=Tk()
root.geometry("600x400")
root.title("Student Info")

def insert():
    STUDENT_ID = (e_stu_no.get())
    STUDENT_NAME = (e_stu_name.get())
    STUDENT_DOB = (e_stu_DOB.get())
    STUDENT_DOJ = (e_stu_DOJ.get())

    if STUDENT_ID=="" or STUDENT_NAME=="" or STUDENT_DOB=="" or STUDENT_DOJ=="":
        messagebox.showinfo("Insert Status","All Fields are Required")
    else:
        my_connect = mysql.connect(host="localhost", user="root", passwd="root", database="STUDENT")
        cur_obj = my_connect.cursor()
        cur_obj.execute("select STUDENT_ID from STUDENT")
        result = cur_obj.fetchall()
        r = list(result)

        for x in r:
            if x[0] == int(e_stu_no.get()):
                print(x[0] == e_stu_no.get())
                messagebox.showinfo("Insert Status", "ID present, Change ID")
                break
        else:
            cur_obj.execute("insert into student values('"+ STUDENT_ID +"','"+ STUDENT_NAME +"','"+ STUDENT_DOB +"','"+ STUDENT_DOJ +"')")
            cur_obj.execute("commit")
            show()
            messagebox.showinfo("Insert Status", "Inserted Successfully")

        e_stu_no.delete(0,'end')
        e_stu_name.delete(0,'end')
        e_stu_DOB.delete(0,'end')
        e_stu_DOJ.delete(0,'end')

        my_connect.close()


def delete():
    if e_stu_no=="":
        messagebox.showinfo("Delete Status","Student no is Required to delete")
    else:
        my_connect = mysql.connect(host="localhost", user="root", passwd="root", database="STUDENT")
        cur_obj = my_connect.cursor()
        cur_obj.execute("delete from student where STUDENT_ID='" + e_stu_no.get() + "'")
        cur_obj.execute("commit")

        e_stu_no.delete(0,'end')
        e_stu_name.delete(0,'end')
        e_stu_DOB.delete(0,'end')
        e_stu_DOJ.delete(0,'end')
        show()
        messagebox.showinfo("Delete Status", "Delete Successfully")
        my_connect.close()

def update():
    STUDENT_ID = (e_stu_no.get())
    STUDENT_NAME = (e_stu_name.get())
    STUDENT_DOB = (e_stu_DOB.get())
    STUDENT_DOJ = (e_stu_DOJ.get())

    if STUDENT_ID == "" or STUDENT_NAME == "" or STUDENT_DOB == "" or STUDENT_DOJ == "":
        messagebox.showinfo("Update Status", "All Fields are Required")
    else:
        my_connect = mysql.connect(host="localhost", user="root", passwd="root", database="STUDENT")
        cur_obj = my_connect.cursor()
        cur_obj.execute("update student set STUDENT_NAME='" + STUDENT_NAME + "',STUDENT_DOB='" + STUDENT_DOB + "', STUDENT_DOJ='" + STUDENT_DOJ + "' where STUDENT_ID ='" + STUDENT_ID + "'")
        cur_obj.execute("commit")

        e_stu_no.delete(0, 'end')
        e_stu_name.delete(0, 'end')
        e_stu_DOB.delete(0, 'end')
        e_stu_DOJ.delete(0, 'end')
        show()
        messagebox.showinfo("Update Status", "Update Successfully")
        my_connect.close()

def get_info():
    if e_stu_no=="":
        messagebox.showinfo("Fetch Status","Student no. is Required to Fetch")
    else:
        my_connect = mysql.connect(host="localhost", user="root", passwd="root", database="STUDENT")
        cur_obj = my_connect.cursor()
        cur_obj.execute("select * from student where STUDENT_ID='" + e_stu_no.get() + "'")
        rows=cur_obj.fetchall()

        for row in rows:
            e_stu_name.insert(0,row[1])
            e_stu_DOB.insert(0,row[2])
            e_stu_DOJ.insert(0,row[3])

        my_connect.close()

def show():
    my_connect = mysql.connect(host="localhost", user="root", passwd="root", database="STUDENT")
    cur_obj = my_connect.cursor()
    cur_obj.execute("select * from student")
    rows = cur_obj.fetchall()
    list1.delete(0,list1.size())

    for row in rows:
        InsertData=str(row[0])+'   '+row[1]+'   '+row[2]+'   '+row[3]
        list1.insert(list1.size()+1,InsertData)
    my_connect.close()


stu_no = Label(root, text="Enter student ID ", font=("bold",10)).place(x=20,y=30)
stu_name = Label(root, text="Enter Student name ", font=("bold",10)).place(x=20,y=60)
stu_DOB = Label(root, text="Enter student DOB ", font=("bold",10)).place(x=20,y=90)
stu_DOJ = Label(root, text="Enter student DOJ ", font=("bold",10)).place(x=20,y=120)

e_stu_no=Entry(root)
e_stu_no.place(x=150,y=30)
e_stu_name=Entry(root)
e_stu_name.place(x=150,y=60)
e_stu_DOB=Entry(root)
e_stu_DOB.place(x=150,y=90)
e_stu_DOJ=Entry(root)
e_stu_DOJ.place(x=150,y=120)

insert=Button(root,text="Insert",font=("italic",10), bg="white", command=insert).place(x=20,y=160)
delete=Button(root,text="Delete",font=("italic",10), bg="white", command=delete).place(x=80,y=160)
update=Button(root,text="Update",font=("italic",10), bg="white", command=update).place(x=140,y=160)
get=Button(root,text="Get",font=("italic",10),bg="white",command=get_info).place(x=200,y=160)

list1=Listbox(root)
list1.place(x=320,y=30)
show()


root.mainloop()