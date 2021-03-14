from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import MySQLdb
import datetime

mainui, _ = uic.loadUiType('main.ui')


class Main(QMainWindow, mainui):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.DB_connect()
        self.Handle_Buttons()
        self.UI_changes()
        self.Open_Daily_movements_tab()
        self.Show_All_Categories()
        self.Show_Branchies()
        self.Show_Publisher()
        self.Show_Authors()
        self.Show_All_Books()
        self.Show_All_Clients()

    def UI_changes(self):
        # UI changes in login
        self.tabWidget.tabBar().setVisible(False)

    def DB_connect(self):
        # connection between app and db
        self.db = MySQLdb.connect(host='127.0.0.1', user='root', password='',
                                  db='libraryapp')
        self.cur = self.db.cursor()
        print('done')

    def Handle_Buttons(self):
        # To handle all buttons in the app
        self.pushButton.clicked.connect(self.Open_Daily_movements_tab)
        self.pushButton_2.clicked.connect(self.Open_Books_tab)
        self.pushButton_3.clicked.connect(self.Open_Clients_tab)
        self.pushButton_4.clicked.connect(self.Open_Dashboard_tab)
        self.pushButton_5.clicked.connect(self.Open_History_tab)
        self.pushButton_6.clicked.connect(self.Open_Reports_tab)
        self.pushButton_7.clicked.connect(self.Open_Settings_tab)
        # Secondary buttons
        self.pushButton_8.clicked.connect(self.Handle_Today_Work)
        self.pushButton_19.clicked.connect(self.Add_Branch)
        self.pushButton_21.clicked.connect(self.Add_Publisher)
        self.pushButton_23.clicked.connect(self.Add_Author)
        self.pushButton_24.clicked.connect(self.Add_Category)
        self.pushButton_20.clicked.connect(self.Add_Employee)
        self.pushButton_10.clicked.connect(self.Add_New_Book)
        self.pushButton_15.clicked.connect(self.Add_New_Client)
        self.pushButton_11.clicked.connect(self.Edit_Book_Search)
        self.pushButton_12.clicked.connect(self.Save_Edit)
        self.pushButton_17.clicked.connect(self.Edit_Client_Search)

    def Handle_Login(self):
        # Handle login
        pass

    def Handle_Reset_Password(self):
        # Handle reset password
        pass

    def Handle_Today_Work(self):
        # Handle today operations
        pass
    ##########################################
    # Books

    def Show_All_Books(self):
        # To Show_All_Books
        self.tableWidget_2.insertRow(0)
        self.cur.execute('''
            SELECT code, title, category_id, author_id, price FROM books
        ''')
        date = self.cur.fetchall()
        for row, form in enumerate(date):
            for col, item in enumerate(form):
                self.tableWidget_2.setItem(
                    row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

    def Add_New_Book(self):
        # To Add_New_Book
        book_title = self.lineEdit_51.text()
        book_description = self.lineEdit_2.text()
        book_category = self.comboBox_3.currentIndex()
        book_code = self.lineEdit_4.text()
        book_barcode = self.lineEdit_52.text()
        book_part_order = self.lineEdit_5.text()
        book_price = self.lineEdit_3.text()
        book_publisher = self.comboBox_7.currentIndex()
        book_author = self.comboBox_6.currentIndex()
        book_status = self.comboBox_22.currentIndex()
        date = datetime.datetime.now()

        self.cur.execute('''
            INSERT INTO books
            (title, description, category_id, code, barcode, part_order, price, publisher_id, author_id, status, date)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (book_title, book_description, book_category, book_code, book_barcode, book_part_order, book_price, book_publisher, book_author, book_status, date))
        self.db.commit()
        self.statusBar().showMessage('Book added successfully')

    def Edit_Book_Search(self):
        # Edit_Book
        book_code = self.lineEdit_10.text()
        sql = ('''
            SELECT * FROM books WHERE code = %s
        ''')
        self.cur.execute(sql, [(book_code)])
        date = self.cur.fetchone()
        # Set the date in their fields
        self.lineEdit_8.setText(date[1])
        self.lineEdit_7.setText(date[2])
        self.lineEdit_6.setText(str(date[6]))
        self.lineEdit_9.setText(str(date[7]))
        self.comboBox_4.setCurrentIndex(int(date[3]))
        self.comboBox_9.setCurrentIndex(int(date[8]))
        self.comboBox_10.setCurrentIndex(int(date[9]))
        self.comboBox_8.setCurrentIndex(int(date[11]))

    def Save_Edit(self):
        # To save edits
        book_title = self.lineEdit_8.text()
        book_description = self.lineEdit_7.text()
        book_category = self.comboBox_3.currentIndex()
        book_code = self.lineEdit_10.text()
        book_part_order = self.lineEdit_6.text()
        book_price = self.lineEdit_9.text()
        book_publisher = self.comboBox_9.currentIndex()
        book_author = self.comboBox_10.currentIndex()
        book_status = self.comboBox_8.currentIndex()
        self.cur.execute('''
                         UPDATE books 
                         SET title = %s, description = %s, code = %s, 
                         part_order = %s, price = %s, status = %s, 
                         category_id = %s, publisher_id = %s, author_id = %s
                         WHERE code = %s
                         ''', (book_title, book_description, book_code,
                               book_part_order, book_price, book_status,
                               book_category, book_publisher, book_author,
                               book_code))
        self.db.commit()
        self.statusBar().showMessage('Book information updated successfully')

    def Delete_Book(self):
        # To Delete_Book
        pass

    ##########################################
    # Clients
    def Show_All_Clients(self):
        # To Show_All_Clients
        self.tableWidget_3.insertRow(0)
        self.cur.execute('''
            SELECT name, mail, phone, date, National_ID FROM clients
        ''')
        date = self.cur.fetchall()
        for row, form in enumerate(date):
            for col, item in enumerate(form):
                self.tableWidget_3.setItem(
                    row, col, QTableWidgetItem(str(item)))
                col += 1
            row_position = self.tableWidget_3.rowCount()
            self.tableWidget_3.insertRow(row_position)

    def Add_New_Client(self):
        # To Add_New_Clients
        client_name = self.lineEdit_11.text()
        client_mail = self.lineEdit_12.text()
        client_phone = self.lineEdit_13.text()
        client_national_id = self.lineEdit_14.text()
        date = datetime.datetime.now()

        self.cur.execute('''
            INSERT INTO clients
            (name, mail, phone, date, National_ID)
            VALUES
            (%s, %s, %s, %s, %s)
        ''', (client_name, client_mail, client_phone, date, client_national_id))
        self.db.commit()
        self.statusBar().showMessage('Client added successfully')

    def Edit_Client_Search(self):
        # Edit_Client
        client_data = self.lineEdit_19.text()
        if self.comboBox_11.currentIndex() == 0:
            sql = ('''
                SELECT * FROM clients WHERE name = %s
            ''')
            self.cur.execute(sql, [(client_data)])
            date = self.cur.fetchone()
            print(date)
        elif self.comboBox_11.currentIndex() == 1:
            sql = ('''
                SELECT * FROM clients WHERE mail = %s
            ''')
            self.cur.execute(sql, [(client_data)])
            date = self.cur.fetchone()
            print(date)
        elif self.comboBox_11.currentIndex() == 2:
            sql = ('''
                SELECT * FROM clients WHERE phone = %s
            ''')
            self.cur.execute(sql, [(client_data)])
            date = self.cur.fetchone()
            print(date)
        else:
            sql = ('''
                SELECT * FROM clients WHERE National_ID = %s
            ''')
            self.cur.execute(sql, [(client_data)])
            date = self.cur.fetchone()
            print(date)

    def Edit_Client(self):
        # Edit_Client
        pass

    def Delete_Client(self):
        # To Delete_Client
        pass

    ##########################################
    # History
    def Show_History(self):
        # Show All History to the Admin
        pass

    ##########################################
    # Books Reports
    def All_Books_Reports(self):
        # To All_Books_Reports
        pass

    def Books_Filter_Reports(self):
        # To Books_Filter_Reports
        pass

    def Books_Export_Report(self):
        # export Books Data to Excel file
        pass

    ##########################################
    # Clients Reports
    def All_Clients_Reports(self):
        # To All_Clients_Reports
        pass

    def Clients_Filter_Reports(self):
        # To Clients_Filter_Reports
        pass

    def Clients_Export_Report(self):
        # export Clients Data to Excel file
        pass

    ##########################################
    # Monthly Reports
    def Monthly_Reports(self):
        # To Monthly_Reports
        pass

    def Monthly_Reports_Export(self):
        # To Monthly_Reports_Export to excel file
        pass

    ##########################################
    # Settings
    def Add_Branch(self):
        # To Add_Branch
        branch_name = self.lineEdit_20.text()
        branch_code = self.lineEdit_21.text()
        branch_location = self.lineEdit_22.text()
        self.cur.execute('''
            INSERT INTO branch
            (name, code, location)
            VALUES
            (%s, %s, %s)
        ''', (branch_name, branch_code, branch_location))
        self.db.commit()
        self.statusBar().showMessage('Branch added successfully')

    def Add_Category(self):
        # To Add_Category
        category_name = self.lineEdit_33.text()
        parent_category_text = self.comboBox_12.currentText()
        # To get the id of the parent category
        query = '''SELECT id FROM category WHERE category_name = %s'''
        self.cur.execute(query, [(parent_category_text)])
        data_id = self.cur.fetchone()
        parent_category_id = data_id[0]
        # To add the new category with the parent category id
        self.cur.execute('''
            INSERT INTO category
            (category_name, parent_category)
            VALUES
            (%s, %s)
        ''', (category_name, parent_category_id))
        self.db.commit()
        self.statusBar().showMessage('Category added successfully')
        # To show the new category after added without restart the app
        self.Show_All_Categories()

    def Add_Publisher(self):
        # To Add_Publisher
        publisher_name = self.lineEdit_26.text()
        publisher_location = self.lineEdit_28.text()
        self.cur.execute('''
            INSERT INTO publisher
            (name, Location)
            VALUES
            (%s, %s)
        ''', (publisher_name, publisher_location))
        self.db.commit()
        self.statusBar().showMessage('Publisher added successfully')

    def Add_Author(self):
        # To Add_Author
        author_name = self.lineEdit_31.text()
        author_location = self.lineEdit_32.text()
        self.cur.execute('''
            INSERT INTO author
            (name, Location)
            VALUES
            (%s, %s)
        ''', (author_name, author_location))
        self.db.commit()
        self.statusBar().showMessage('Author added successfully')

    def Add_Employee(self):
        # To Add_Employee
        employee_name = self.lineEdit_24.text()
        employee_mail = self.lineEdit_23.text()
        employee_phone = self.lineEdit_27.text()
        employee_branch = self.comboBox_20.currentIndex()
        employee_national_id = self.lineEdit_25.text()
        employee_periority = self.lineEdit_49.text()
        employee_password = self.lineEdit_29.text()
        employee_password_confirm = self.lineEdit_30.text()
        date = datetime.datetime.now()

        if employee_password == employee_password_confirm:
            self.cur.execute('''
                INSERT INTO employee 
                (name, mail, phone, date, National_ID, periority, password, branch)
                VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)
            ''', (employee_name, employee_mail, employee_phone, date, employee_national_id, employee_periority, employee_password, employee_branch))
            self.db.commit()
        else:
            self.statusBar().showMessage('Wrong password')

    def Edit_Employee(self):
        # To Edit_Employee
        pass

    def Add_Employee_Permision(self):
        # To Add_Employee_Permision
        pass

    def Admin_Report(self):
        # To send Admin_Report
        pass

    ###############################
    # Show Functions
    def Show_All_Categories(self):
        self.comboBox_12.clear()
        self.cur.execute('''
            SELECT category_name FROM category ORDER BY id ASC
        ''')
        categories = self.cur.fetchall()
        for category in categories:
            self.comboBox_12.addItem(str(category[0]))
            self.comboBox_3.addItem(str(category[0]))
            self.comboBox_4.addItem(str(category[0]))

    def Show_Branchies(self):
        self.cur.execute('''
            SELECT name FROM branch ORDER BY id ASC
        ''')
        branchies = self.cur.fetchall()
        for branch in branchies:
            self.comboBox_20.addItem(str(branch[0]))
            self.comboBox_21.addItem(str(branch[0]))

    def Show_Publisher(self):
        self.cur.execute('''
            SELECT name FROM publisher ORDER BY id ASC
        ''')
        publishers = self.cur.fetchall()
        for publisher in publishers:
            self.comboBox_7.addItem(str(publisher[0]))
            self.comboBox_9.addItem(str(publisher[0]))

    def Show_Authors(self):
        self.cur.execute('''
            SELECT name FROM author ORDER BY id ASC
        ''')
        authores = self.cur.fetchall()
        for author in authores:
            self.comboBox_6.addItem(str(author[0]))
            self.comboBox_10.addItem(str(author[0]))

    ###############################

    def Open_Login_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Reset_Password_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Daily_movements_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Books_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Clients_tab(self):
        self.tabWidget.setCurrentIndex(4)

    def Open_Dashboard_tab(self):
        self.tabWidget.setCurrentIndex(5)

    def Open_History_tab(self):
        self.tabWidget.setCurrentIndex(6)

    def Open_Reports_tab(self):
        self.tabWidget.setCurrentIndex(7)

    def Open_Settings_tab(self):
        self.tabWidget.setCurrentIndex(8)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
