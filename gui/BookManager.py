from tkinter import *
import pymysql

button_width = 14
button_height = 2
bg_color = 'sky blue'


class AddBookWindow:
    def __init__(self):
        add_book_root = Tk()
        add_book_root.title("New Book")
        frame = Frame(add_book_root)
        frame.pack()
        bottom_frame = Frame(add_book_root)
        bottom_frame.pack(side=BOTTOM)

        self.book_id_label = Label(frame, text="ID")
        self.book_name_label = Label(frame, text="Name")
        self.book_author_label = Label(frame, text="Author")
        self.book_price_label = Label(frame, text="Price")

        self.id_field = Entry(frame)
        self.name_field = Entry(frame)
        self.author_field = Entry(frame)
        self.price_field = Entry(frame)

        self.book_id_label.grid(row=0, sticky=E)
        self.book_name_label.grid(row=1, sticky=E)
        self.book_author_label.grid(row=2, sticky=E)
        self.book_price_label.grid(row=3, sticky=E)
        self.id_field.grid(row=0, column=1)
        self.name_field.grid(row=1, column=1)
        self.author_field.grid(row=2, column=1)
        self.price_field.grid(row=3, column=1)

        self.add_button = Button(bottom_frame, width=button_width, height=button_height, fg="green", text="ADD", command=self.add)
        self.add_button.config(relief=RAISED)
        self.add_button.pack(side=LEFT)

    def add(self):
        print("Add Book to DB...")
        id=self.id_field.get()
        name=self.name_field.get()
        author=self.author_field.get()
        price=self.price_field.get()
        print(id, name, author, price)

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        add = "INSERT INTO `books` (`book_id`, `title`, `author`, `price`) VALUES (%s, %s, %s, %s)"
        val = (id, name, author, price)
        cursor.execute(add, val)
        conn.commit()

        self.id_field.delete(0, 'end')
        self.name_field.delete(0, 'end')
        self.author_field.delete(0, 'end')
        self.price_field.delete(0, 'end')

    def cancel(self):
        print("cancelled...")


class EditBookWindow:
    def __init__(self):
        edit_book_root = Tk()
        edit_book_root.title("Edit Book")
        frame = Frame(edit_book_root)
        frame.pack()

        self.book_details_root=None

        self.book_id_label = Label(frame, text="Book ID")
        self.id_field = Entry(frame)

        self.book_id_label.grid(row=0, sticky=E)
        self.id_field.grid(row=0, column=1)

        self.ok_button = Button(frame, width=button_width, height=button_height, fg="green", text="OK", relief=RAISED, command=self.get_book_details)
        self.ok_button.grid(row=0, column=2)

        self.book_id_field = None
        self.name_field = None
        self.author_field = None
        self.price_field = None
        self.count_field = None
        self.status_field = None

    def get_book_details(self):
        print("finding book...")

        self.book_details_root = Tk()
        self. book_details_root.title("Book Details")

        book_id=self.id_field.get()
        edit_button=Button(self.book_details_root, width=button_width, height=button_height, fg="green", text="OK", relief=RAISED, command=self.edit_book)

        Label(self.book_details_root, text="Book_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=0, sticky="nsew")
        Label(self.book_details_root, text="Book_Title", bg=bg_color, relief=GROOVE).grid(row=1, column=0, sticky="nsew")
        Label(self.book_details_root, text="Author", bg=bg_color, relief=GROOVE).grid(row=2, column=0, sticky="nsew")
        Label(self.book_details_root, text="Price", bg=bg_color, relief=GROOVE).grid(row=3, column=0, sticky="nsew")
        Label(self.book_details_root, text="Issue_Count", bg=bg_color, relief=GROOVE).grid(row=4, column=0, sticky="nsew")
        Label(self.book_details_root, text="Status", bg=bg_color, relief=GROOVE).grid(row=5, column=0, sticky="nsew")

        self.book_id_field = Entry(self.book_details_root, state='disabled')
        self.name_field = Entry(self.book_details_root)
        self.author_field = Entry(self.book_details_root)
        self.price_field = Entry(self.book_details_root)
        self.count_field = Entry(self.book_details_root)
        self.status_field = Entry(self.book_details_root)

        self.book_id_field.grid(row=0, column=1, sticky="nsew")
        self.name_field.grid(row=1, column=1, sticky="nsew")
        self.author_field.grid(row=2, column=1, sticky="nsew")
        self.price_field.grid(row=3, column=1, sticky="nsew")
        self.count_field.grid(row=4, column=1, sticky="nsew")
        self.status_field.grid(row=5, column=1, sticky="nsew")

        edit_button.grid(row=6, column=1, sticky="nsew")

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        sql = "select * from `books` where `book_id`='" + book_id + "';"
        cursor.execute(sql)
        data = cursor.fetchone()

        self.book_id_field.config(state='normal')
        self.book_id_field.delete(0, 'end')
        self.book_id_field.insert(0, data[0])
        self.book_id_field.config(state='disabled')
        self.name_field.delete(0, 'end')
        self.name_field.insert(0, data[1])
        self.author_field.delete(0, 'end')
        self.author_field.insert(0, data[2])
        self.price_field.delete(0, 'end')
        self.price_field.insert(0, data[3])
        self.count_field.delete(0, 'end')
        self.count_field.insert(0, data[4])
        self.status_field.delete(0, 'end')
        self.status_field.insert(0, data[5])

    def edit_book(self):
        print("edit_book...")

        id=self.book_id_field.get()
        title=self.name_field.get()
        author=self.author_field.get()
        price=self.price_field.get()
        count=self.count_field.get()
        status=self.status_field.get()

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        sql = "update `books` set"
        sql = sql + " `title`='" + title + "',"
        sql = sql + " `author`='" + author + "',"
        sql = sql + " `price`='" + price + "',"
        sql = sql + " `lend_count`='" + count + "',"
        sql = sql + " `book_status`='" + status + "'"
        sql = sql + "where `book_id`='" + id + "';"
        print(sql)

        cursor.execute(sql)
        conn.commit()
        self.book_details_root.destroy()


class RemoveBookWindow:
    def __init__(self):
        remove_book_root = Tk()
        remove_book_root.title("Remove Book")
        frame = Frame(remove_book_root)
        frame.pack()
        bottom_frame = Frame(remove_book_root)
        bottom_frame.pack(side=BOTTOM)

        self.book_id_label = Label(frame, text="Book ID")
        self.id_field = Entry(frame)

        self.book_id_label.grid(row=0, sticky=E)
        self.id_field.grid(row=0, column=1)

        self.find_button = Button(frame, width=button_width, height=button_height, fg="green", text="FIND", relief=RAISED, command=self.find)
        self.find_button.grid(row=0, column=2)

        self.book_name_label = Label(bottom_frame, text="Book Name")
        self.name_field = Entry(bottom_frame, state='disabled')
        self.delete_button = Button(bottom_frame, width=button_width, height=button_height, fg="green", text="DELETE", relief=RAISED, command=self.remove)
        self.book_name_label.pack(side=LEFT)
        self.name_field.pack(side=LEFT)
        self.delete_button.pack(side=LEFT)

    def remove(self):
        print("Delete Book from DB...")
        book_id=self.id_field.get()

        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()
        sql = "delete from `books` where `book_id`='" + book_id + "';"
        cursor.execute(sql)
        conn.commit()

        self.id_field.delete(0, 'end')
        self.name_field.delete(0, 'end')

    def find(self):
        print("finding book...")
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()

        book_id=self.id_field.get()
        sql = "select `title` from `books` where `book_id`='" + book_id + "';"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)
        self.name_field.config(state='normal')
        self.name_field.delete(0, 'end')
        self.name_field.insert(0, data)
        self.name_field.config(state='disabled')


class ShowBooksWindow:
    def __init__(self):
        table = Tk()
        table.title("Show Books")
        conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
        cursor = conn.cursor()

        sql = 'select * from `books`;'
        countrow = cursor.execute(sql)
        print("Number of rows :", countrow)

        data = cursor.fetchall()

        Label(table, text="Book_ID", bg=bg_color, relief=GROOVE).grid(row=0, column=0, sticky="nsew")
        Label(table, text="Book_Title", bg=bg_color, relief=GROOVE).grid(row=0, column=1, sticky="nsew")
        Label(table, text="Author", bg=bg_color, relief=GROOVE).grid(row=0, column=2, sticky="nsew")
        Label(table, text="Price", bg=bg_color, relief=GROOVE).grid(row=0, column=3, sticky="nsew")
        Label(table, text="Issue_Count", bg=bg_color, relief=GROOVE).grid(row=0, column=4, sticky="nsew")
        Label(table, text="Status", bg=bg_color, relief=GROOVE).grid(row=0, column=5, sticky="nsew")

        for index, dat in enumerate(data):
            Label(table, text=dat[0], relief=GROOVE).grid(row=index + 1, column=0, sticky="nsew")
            Label(table, text=dat[1], relief=GROOVE).grid(row=index + 1, column=1, sticky="nsew")
            Label(table, text=dat[2], relief=GROOVE).grid(row=index + 1, column=2, sticky="nsew")
            Label(table, text=dat[3], relief=GROOVE).grid(row=index + 1, column=3, sticky="nsew")
            Label(table, text=dat[4], relief=GROOVE).grid(row=index + 1, column=4, sticky="nsew")
            Label(table, text=dat[5], relief=GROOVE).grid(row=index + 1, column=5, sticky="nsew")

        table.mainloop()
