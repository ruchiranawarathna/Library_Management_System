from tkinter import *
import pymysql
import datetime

button_width = 14
button_height = 2
bg_color = 'sky blue'


class IssuesWindow:
    def __init__(self):
        new_issue_root = Tk()
        new_issue_root.title("New Issue")
        frame = Frame(new_issue_root)
        frame.pack()
        bottom_frame = Frame(new_issue_root)
        bottom_frame.pack(side=BOTTOM)

        self.book_id_label = Label(frame, text="Book ID")
        self.student_id_label = Label(frame, text="Student ID")
        self.from_date_label = Label(frame, text="From Date")

        self.book_id_field = Entry(frame)
        self.student_id_field = Entry(frame)
        self.from_date_field = Entry(frame)

        self.book_id_label.grid(row=0, sticky=E)
        self.student_id_label.grid(row=1, sticky=E)
        self.from_date_label.grid(row=2, sticky=E)
        self.book_id_field.grid(row=0, column=1)
        self.student_id_field.grid(row=1, column=1)
        self.from_date_field.grid(row=2, column=1)

        self.from_date = datetime.datetime.today().strftime('%Y-%m-%d')
        self.from_date_field.delete(0, 'end')
        self.from_date_field.insert(0, self.from_date)
        self.add_button = Button(bottom_frame, width=button_width, height=button_height, fg="green", text="ADD", command=self.add)
        self.add_button.config(relief=RAISED)
        self.add_button.pack(side=LEFT)

    def add(self):
        print("Add issue to DB...")
        book_id=self.book_id_field.get()
        student_id=self.student_id_field.get()
        print(book_id, student_id)

        due_date = datetime.datetime.strptime(self.from_date, '%Y-%m-%d') + datetime.timedelta(days=14)
        print(due_date.date())
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        add = "INSERT INTO `issues` (`book_id`, `student_id`, `from_date`, `due_date`) VALUES (%s, %s, %s, %s)"
        val = (book_id, student_id, self.from_date, due_date.date())
        cursor.execute(add, val)
        conn.commit()

        update_book = "update `books` set `book_status`='" + student_id + "'where `book_id`='" + book_id + "';"
        cursor.execute(update_book)
        update_book = "update `books` set `lend_count`=`lend_count`+1 where `book_id`='" + book_id + "';"
        cursor.execute(update_book)
        update_student = "update `students` set `book_count`=`book_count`+1 where `student_id`='" + student_id + "';"
        cursor.execute(update_student)
        conn.commit()

        self.book_id_field.delete(0, 'end')
        self.student_id_field.delete(0, 'end')


class ReturnWindow:
    def __init__(self):
        return_root = Tk()
        return_root.title("Return Book")
        frame = Frame(return_root)
        frame.pack()
        bottom_frame = Frame(return_root)
        bottom_frame.pack(side=BOTTOM)

        self.book_id_label = Label(frame, text="Book ID")
        self.student_id_label = Label(frame, text="Student ID")

        self.book_id_field = Entry(frame)
        self.student_id_field = Entry(frame)
        self.student_id_field = Entry(frame, state='disabled')

        self.book_id_label.grid(row=0, sticky=E)
        self.student_id_label.grid(row=1, sticky=E)
        self.book_id_field.grid(row=0, column=1)
        self.student_id_field.grid(row=1, column=1)

        self.return_button = Button(bottom_frame, width=button_width, height=button_height, fg="blue", text="RETURN", command=self.return_book)
        self.return_button.config(relief=RAISED)
        self.return_button.pack(side=LEFT)

    def return_book(self):
        print("Return issue to DB...")
        book_id=self.book_id_field.get()

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        sql = "delete from `issues` where `book_id`='" + book_id + "';"
        cursor.execute(sql)
        conn.commit()
        print(sql)
        update_book = "update `books` set `book_status`= 'IN';"
        cursor.execute(update_book)
        conn.commit()

        self.book_id_field.delete(0, 'end')


class ShowIssuesWindow:
    def __init__(self):
        table = Tk()
        table.title("Show Books")
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()

        sql = 'select * from `issues`;'
        countrow = cursor.execute(sql)
        print("Number of rows :", countrow)

        data = cursor.fetchall()

        Label(table, text="Issue_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=0, sticky="nsew")
        Label(table, text="Book_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=1, sticky="nsew")
        Label(table, text="Student_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=2, sticky="nsew")
        Label(table, text="From_Date", bg=bg_color, relief=GROOVE).grid(row=0, column=3, sticky="nsew")
        Label(table, text="Due_Date", bg=bg_color, relief=GROOVE).grid(row=0, column=4, sticky="nsew")
        Label(table, text="Fine", bg=bg_color, relief=GROOVE).grid(row=0, column=5, sticky="nsew")

        for index, dat in enumerate(data):
            Label(table, text=dat[0], relief=GROOVE).grid(row=index + 1, column=0, sticky="nsew")
            Label(table, text=dat[1], relief=GROOVE).grid(row=index + 1, column=1, sticky="nsew")
            Label(table, text=dat[2], relief=GROOVE).grid(row=index + 1, column=2, sticky="nsew")
            Label(table, text=dat[3], relief=GROOVE).grid(row=index + 1, column=3, sticky="nsew")
            Label(table, text=dat[4], relief=GROOVE).grid(row=index + 1, column=4, sticky="nsew")
            Label(table, text=dat[5], relief=GROOVE).grid(row=index + 1, column=5, sticky="nsew")

        table.mainloop()
# root = Tk()
# root.title("Add New Issue")
# IssuesWindow(root)
# root.mainloop()



