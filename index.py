from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import MySQLdb

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
        pass

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
        parent_category

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
        pass

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
