import csv
import pymysql
from tkinter import *

conn = pymysql.connect(host='localhost', user='root', password='root', db='library')
cursor = conn.cursor()

button_width = 14
button_height = 2


class DataStore:
    def __init__(self):
        print("Data Store Init")
        self.value = None
        self.reset_confirm_root = None

    def backup_data(self):
        print("Backing up data")
        self.__backup_books()
        self.__backup_studens()
        self.__backup_issues()

    def load_data(self):
        print("Restoring data")
        self.__load_books()
        self.__load_students()
        self.__load_issues()

    def __backup_books(self):
        print("Backup books")
        sql = 'select * from `books`;'
        book_count = cursor.execute(sql)
        print("Number of books :", book_count)

        data = cursor.fetchall()
        csv_data = [["Book ID", "Title", "Author", "Price", "Lend Count", "Status"]]
        for index, dat in enumerate(data):
            row_data = [dat[0], dat[1], dat[2], dat[3], dat[4], dat[5]]
            csv_data.append(row_data)

        with open(r'../../backup/books.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=",")
            for line in csv_data:
                writer.writerow(line)

        csvFile.close()

    def __backup_studens(self):
        print("Backup students")
        sql = 'select * from `students`;'
        student_count = cursor.execute(sql)
        print("Number of students :", student_count)

        data = cursor.fetchall()
        csv_data = [["Student ID", "Name", "Book Count", "Total Fine"]]
        for index, dat in enumerate(data):
            row_data = [dat[0], dat[1], dat[2], dat[3]]
            csv_data.append(row_data)

        with open(r'../../backup/students.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=",")
            for line in csv_data:
                writer.writerow(line)

        csvFile.close()

    def __backup_issues(self):
        print("Backup issues")
        sql = 'select * from `issues`;'
        issue_count = cursor.execute(sql)
        print("Number of issues :", issue_count)

        data = cursor.fetchall()
        csv_data = [["Issue ID", "Book ID", "Student ID", "From Date", "Due Date", "Fine"]]
        for index, dat in enumerate(data):
            row_data = [dat[0], dat[1], dat[2], dat[3], dat[4], dat[5]]
            csv_data.append(row_data)

        with open(r'../../backup/issues.csv', 'w', newline='') as csvFile:
            writer = csv.writer(csvFile, delimiter=",")
            for line in csv_data:
                writer.writerow(line)

        csvFile.close()

    def __load_books(self):
        print("Load books")
        with open(r'../../backup/books.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t ID: {row[0]}   Title: {row[1]}  Author: {row[2]}  Price: {row[3]}  Count: {row[4]}  Status: {row[5]}')
                    add = "INSERT INTO `books` (`book_id`, `title`, `author`, `price`, `lend_count`, `book_status`) VALUES (%s, %s, %s, %s, %s, %s);"
                    val = ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]})
                    cursor.execute(add, val)
                    conn.commit()
                    line_count += 1
            print(f'Processed {line_count} lines.')

    def __load_students(self):
        print("Load students")
        with open(r'../../backup/students.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t ID: {row[0]}   Name: {row[1]}  Count: {row[2]}  Fine: {row[3]}')
                    add = "INSERT INTO `students` (`student_id`, `name`, `book_count`, `total_fine`) VALUES (%s, %s, %s, %s);"
                    val = ({row[0]}, {row[1]}, {row[2]}, {row[3]})
                    cursor.execute(add, val)
                    conn.commit()
                    line_count += 1
            print(f'Processed {line_count} lines.')

    def __load_issues(self):
        print("Load issues")
        with open(r'../../backup/issues.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t Issue ID: {row[0]}   Book ID: {row[1]}  Student ID: {row[2]}  From Date: {row[3]}  Due Date: {row[4]}  Fine: {row[5]}')
                    add = "INSERT INTO `issues` (`issue_id`, `book_id`, `student_id`, `from_date`, `due_date`, `fine`) VALUES (%s, %s, %s, %s, %s, %s);"
                    val = ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]})
                    cursor.execute(add, val)
                    conn.commit()
                    line_count += 1
            print(f'Processed {line_count} lines.')

    def reset_data(self):
        print("Reset Data...")
        # if self.is_reset_confirmed():
        print("Reset Confirmed")
        print("Reset Issues")
        sql = "truncate table `issues`;"
        cursor.execute(sql)
        print("Reset Students")
        sql = "delete from `students`;"
        cursor.execute(sql)
        print("Reset Books")
        sql = "delete from `books`;"
        cursor.execute(sql)

        conn.commit()
        # else:
        #     print("Reset Declined")

    def is_reset_confirmed(self):
        print("Confirmation required for data reset")

        self.reset_confirm_root = Tk()
        self.reset_confirm_root.title("Confirmation")

        message = Label(self.reset_confirm_root, text="Do you want to reset data?")
        message.pack(side=LEFT)

        yes_button = Button(self.reset_confirm_root, width=button_width, height=button_height, fg="green", text="YES", command=lambda: self.finish(True))
        no_button = Button(self.reset_confirm_root, width=button_width, height=button_height, fg="green", text="NO", command=lambda: self.finish(False))

        yes_button.pack()
        no_button.pack()
        print("Finish before mainloop")
        self.reset_confirm_root.mainloop()
        print("Finish before return")
        return self.value

    def finish(self, value):
        print("Finish: %s" % value)
        self.value = value
        self.reset_confirm_root.destroy()
        print("Finish: destroyed")
