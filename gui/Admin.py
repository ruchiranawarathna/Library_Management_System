from tkinter import *

from BookManager import AddBookWindow
from BookManager import RemoveBookWindow
from BookManager import ShowBooksWindow
from IssueManager import IssuesWindow
from IssueManager import ReturnWindow
from IssueManager import ShowIssuesWindow
from StudentManager import ShowStudentsWindow
from StudentManager import AddStudentWindow
from StudentManager import RemoveStudentWindow
from DataStoreManager import DataStore

store = DataStore()
button_width = 14
button_height = 2


def add_book():
    print("Add book")
    AddBookWindow()


def edit_book():
    print("Edit Book")


def remove_book():
    print("Remove book")
    RemoveBookWindow()


def show_books():
    print("Show Books")
    ShowBooksWindow()


def add_student():
    print("Add student to DB")
    AddStudentWindow()


def edit_student():
    print("Edit student")


def remove_student():
    print("Remove student")
    RemoveStudentWindow()


def show_students():
    print("Show students")
    ShowStudentsWindow()


def new_issue():
    print("New Issue")
    IssuesWindow()


def return_book():
    print("Return Book")
    ReturnWindow()


def show_issues():
    print("Show Issues")
    ShowIssuesWindow()


def backup():
    print("Backup Data")
    store.backup_data()


def load():
    print("Load Data")
    store.load_data()


def reset():
    print("Reset Data")
    store.reset_data()


def show(mster):
    print("Show")
    mster.title("LMS - Admin Panel")
    mster.iconbitmap(r'..\images\book.ico')

    institute = Label(root, text="Sumanadeva Daham Pasela", bg="white", fg="purple")
    institute.pack(fill=X)  # Dynamically change length in X direction
    heading = Label(root, text="Library Management System", bg="black", fg="yellow")
    heading.pack()  # Fits only for its length

    book_frame = Frame(root)
    book_frame.pack()
    student_frame = Frame(root)
    student_frame.pack(side=TOP)
    issue_frame = Frame(root)
    issue_frame.pack(side=TOP)
    backup_frame = Frame(root)
    backup_frame.pack(side=TOP)

    add_student_button = Button(student_frame, text="Add Student", fg="green", height=button_height, width=button_width,
                                command=add_student)
    edit_student_button = Button(student_frame, text="Edit Student", fg="blue", height=button_height,
                                 width=button_width, command=edit_student)
    remove_student_button = Button(student_frame, text="Remove Student", fg="red", height=button_height,
                                   width=button_width, command=remove_student)
    all_students_button = Button(student_frame, text="Show All Students", fg="black", height=button_height,
                                 width=button_width, command=show_students)

    add_book_button = Button(book_frame, text="Add Book", fg="green", height=button_height, width=button_width,
                             command=add_book)
    edit_book_button = Button(book_frame, text="Edit Book", fg="blue", height=button_height, width=button_width,
                              command=edit_book)
    remove_book_button = Button(book_frame, text="Remove Book", fg="red", height=button_height, width=button_width,
                                command=remove_book)
    all_book_button = Button(book_frame, text="Show All Books", fg="black", height=button_height, width=button_width,
                             command=show_books)

    new_issue_button = Button(issue_frame, text="New Issue", fg="green", height=button_height, width=button_width,
                              command=new_issue)
    return_button = Button(issue_frame, text="Return Book", fg="blue", height=button_height, width=button_width,
                           command=return_book)
    show_issues_button = Button(issue_frame, text="Show All Issues", fg="black", height=button_height,
                                width=button_width, command=show_issues)

    backup_button = Button(backup_frame, text="Backup Data", fg="black", height=button_height, width=button_width,
                           command=backup)
    load_button = Button(backup_frame, text="Load Data", fg="black", height=button_height, width=button_width,
                         command=load)
    reset_button = Button(backup_frame, text="Reset Data", fg="black", height=button_height, width=button_width,
                          command=reset)

    add_student_button.pack(side=LEFT)
    edit_student_button.pack(side=LEFT)
    remove_student_button.pack(side=LEFT)
    all_students_button.pack(side=LEFT)
    add_book_button.pack(side=LEFT)
    edit_book_button.pack(side=LEFT)
    remove_book_button.pack(side=LEFT)
    all_book_button.pack(side=LEFT)
    new_issue_button.pack(side=LEFT)
    return_button.pack(side=LEFT)
    show_issues_button.pack(side=LEFT)
    backup_button.pack(side=LEFT)
    load_button.pack(side=LEFT)
    reset_button.pack(side=LEFT)

    root.mainloop()


#   --------------------------------------------------------------
root = Tk()  # main window
show(root)


