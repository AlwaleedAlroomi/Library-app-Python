from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

mainui,_ = uic.loadUiType('main.ui')

class Main(QMainWindow, mainui):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

    def UI_changes(self):
        #UI changes in login
        pass

    def DB_connect(self):
        #connection between app and db
        pass

    def Handle_Buttons(self):
        #To handle all buttons in the app
        pass

    def Handle_Login(self):
        #Handle login
        pass

    def Handle_Reset_Password(self):
        #Handle reset password
        pass

    def Handle_Today_Work(self):
        #Handle today operations 
        pass
    
    ##########################################
    #Books
    def Show_All_Books(self):
        #To Show_All_Books
        pass

    def Add_New_Book(self):
        #To Add_New_Book
        pass

    def Edit_Book(self):
        #Edit_Book
        pass

    def Delete_Book(self):
        #To Delete_Book
        pass

    ##########################################
    #Clients
    def Show_All_Clients(self):
        #To Show_All_Clients
        pass

    def Add_New_Client(self):
        #To Add_New_Clients
        pass

    def Edit_Client(self):
        #Edit_Client
        pass

    def Delete_Client(self):
        #To Delete_Client
        pass

    ##########################################
    #History
    def Show_History(self):
        #Show All History to the Admin
        pass

    ##########################################
    #Books Reports
    def All_Books_Reports(self):
        #To All_Books_Reports
        pass

    def Books_Filter_Reports(self):
        #To Books_Filter_Reports
        pass

    def Books_Export_Report(self):
        #export Books Data to Excel file
        pass

    ##########################################
    #Clients Reports
    def All_Clients_Reports(self):
        #To All_Clients_Reports
        pass

    def Clients_Filter_Reports(self):
        #To Clients_Filter_Reports
        pass

    def Clients_Export_Report(self):
        #export Clients Data to Excel file
        pass

    ##########################################
    #Monthly Reports
    def Monthly_Reports(self):
        #To Monthly_Reports
        pass

    def Monthly_Reports_Export(self):
        #To Monthly_Reports_Export to excel file
        pass

    ##########################################
    #Settings
    def Add_Branch(self):
        #To Add_Branch
        pass

    def Add_Category(self):
        #To Add_Category
        pass

    def Add_Publisher(self):
        #To Add_Publisher
        pass

    def Add_Author(self):
        #To Add_Author
        pass

    def Add_Employee(self):
        #To Add_Employee
        pass

    def Edit_Employee(self):
        #To Edit_Employee
        pass

    def Add_Employee_Permision(self):
        #To Add_Employee_Permision
        pass

    def Admin_Report(self):
        #To send Admin_Report
        pass

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
