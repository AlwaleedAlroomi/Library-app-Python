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
        pass

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
        print('book added successfully')

    def Edit_Book(self):
        # Edit_Book
        pass

    def Delete_Book(self):
        # To Delete_Book
        pass

    ##########################################
    # Clients
    def Show_All_Clients(self):
        # To Show_All_Clients
        pass

    def Add_New_Client(self):
        # To Add_New_Clients
        pass

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
        print('branch added')

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
        print('category added')
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
        print('publisher added')

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
        print('Author added')

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
            print('Wrong password')

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
            SELECT category_name FROM category
        ''')
        categories = self.cur.fetchall()
        for category in categories:
            self.comboBox_12.addItem(str(category[0]))
            self.comboBox_3.addItem(str(category[0]))

    def Show_Branchies(self):
        self.cur.execute('''
            SELECT name FROM branch
        ''')
        branchies = self.cur.fetchall()
        for branch in branchies:
            self.comboBox_20.addItem(str(branch[0]))
            self.comboBox_21.addItem(str(branch[0]))

    def Show_Publisher(self):
        self.cur.execute('''
            SELECT name FROM publisher
        ''')
        publishers = self.cur.fetchall()
        for publisher in publishers:
            self.comboBox_7.addItem(str(publisher[0]))

    def Show_Authors(self):
        self.cur.execute('''
            SELECT name FROM author
        ''')
        authores = self.cur.fetchall()
        for author in authores:
            self.comboBox_6.addItem(str(author[0]))

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
