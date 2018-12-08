from tkinter import *
import pymysql

button_width = 14
button_height = 2
bg_color = 'sky blue'


class AddStudentWindow:
    def __init__(self):
        add_student_root = Tk()
        add_student_root.title("New Student")
        frame = Frame(add_student_root)
        frame.pack()
        bottom_frame = Frame(add_student_root)
        bottom_frame.pack(side=BOTTOM)

        self.student_id_label = Label(frame, text="ID")
        self.student_name_label = Label(frame, text="Name")

        self.id_field = Entry(frame)
        self.name_field = Entry(frame)

        self.student_id_label.grid(row=0, sticky=E)
        self.student_name_label.grid(row=1, sticky=E)
        self.id_field.grid(row=0, column=1)
        self.name_field.grid(row=1, column=1)

        self.add_button = Button(bottom_frame, width=button_width, height=button_height, fg="green", text="ADD", command=self.add)
        self.add_button.config(relief=RAISED)
        self.add_button.pack(side=LEFT)

    def add(self):
        print("Add student to DB...")
        id=self.id_field.get()
        name=self.name_field.get()
        print(id, name)

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        add = "INSERT INTO `students` (`student_id`, `name`) VALUES (%s, %s)"
        val = (id, name)
        cursor.execute(add, val)
        conn.commit()

        self.id_field.delete(0, 'end')
        self.name_field.delete(0, 'end')


class RemoveStudentWindow:
    def __init__(self):
        remove_student_root = Tk()
        remove_student_root.title("Remove Student")
        frame = Frame(remove_student_root)
        frame.pack()
        bottom_frame = Frame(remove_student_root)
        bottom_frame.pack(side=BOTTOM)

        self.student_id_label = Label(frame, text="Student ID")
        self.id_field = Entry(frame)

        self.student_id_label.grid(row=0, sticky=E)
        self.id_field.grid(row=0, column=1)

        self.find_button = Button(frame, width=button_width, height=button_height, fg="green", text="FIND", relief=RAISED, command=self.find)
        self.find_button.grid(row=0, column=2)

        self.student_name_label = Label(bottom_frame, text="Student Name")
        self.name_field = Entry(bottom_frame, state='disabled')
        self.delete_button = Button(bottom_frame, width=button_width, height=button_height, fg="green", text="DELETE", relief=RAISED, command=self.remove)
        self.student_name_label.pack(side=LEFT)
        self.name_field.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)

    def remove(self):
        print("Delete Student from DB...")
        student_id=self.id_field.get()

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        sql = "delete from `students` where `student_id`='" + student_id + "';"
        cursor.execute(sql)
        conn.commit()

        self.id_field.delete(0, 'end')
        self.name_field.delete(0, 'end')

    def find(self):
        print("finding student...")
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()

        student_id=self.id_field.get()
        sql = "select `name` from `students` where `student_id`='" + student_id + "';"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)
        self.name_field.config(state='normal')
        self.name_field.delete(0, 'end')
        self.name_field.insert(0, data)
        self.name_field.config(state='disabled')


class ShowStudentsWindow:
    def __init__(self):
        table = Tk()
        table.title("Show Students")
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()

        sql = 'select * from `students`;'
        countrow = cursor.execute(sql)
        print("Number of rows :", countrow)

        data = cursor.fetchall()

        Label(table, text="Student_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=0, sticky="nsew")
        Label(table, text="Name", bg=bg_color, relief=GROOVE).grid(row=0, column=1, sticky="nsew")
        Label(table, text="Lend_Count", bg=bg_color, relief=GROOVE).grid(row=0, column=2, sticky="nsew")
        Label(table, text="Fine", bg=bg_color, relief=GROOVE).grid(row=0, column=3, sticky="nsew")

        for index, dat in enumerate(data):
            Label(table, text=dat[0], relief=GROOVE).grid(row=index + 1, column=0, sticky="nsew")
            Label(table, text=dat[1], relief=GROOVE).grid(row=index + 1, column=1, sticky="nsew")
            Label(table, text=dat[2], relief=GROOVE).grid(row=index + 1, column=2, sticky="nsew")
            Label(table, text=dat[3], relief=GROOVE).grid(row=index + 1, column=3, sticky="nsew")

        table.mainloop()