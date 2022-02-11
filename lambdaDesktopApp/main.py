from getpass import getuser
import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import webbrowser
from qt_material import apply_stylesheet, QtStyleTools
import threading as th
from functions import *
import sqlite3
import os
import time

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class DB_Search(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self):
        super(DB_Search, self).__init__()
        uic.loadUi('DatabaseSearch.ui', self)
        self.setWindowTitle('Lambda - Database Search')
        self.setWindowIcon(QtGui.QIcon('lambda.svg'))
        self.setFixedSize(1200, 600)
        self.setupButtons()
        self.tableSetup()
        self.show()
        

    ## Open DB file and add every entry to the table
    def openDB(self):
        pass

    def dbSearch(self, platform, searchTerm):
        conn = sqlite3.connect(f"{platform}.db")
        c = conn.cursor()
        c.execute("SELECT * FROM accounts WHERE username LIKE ?", (f"%{searchTerm}%",))
        data = c.fetchall()
        conn.close()
        
        # add data to table
        for i in range(0, len(data)):
            self.databaseTable.insertRow(i)
            for j in range(0, len(data[i])):
                self.databaseTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j])))


    def setupButtons(self):
        # self.ButtonName.clicked.connect()
        self.SearchDBButton.clicked.connect(lambda: self.dbSearch(self.PlatformDropdown.currentText(), self.DBSearchBox.text()))
        self.OpenDBButton.clicked.connect(lambda: self.openDB)




class Ui(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        self.apply_stylesheet(app, "dark_red.xml")
        self.setWindowTitle('Lambda')
        self.setWindowIcon(QtGui.QIcon('lambda.svg'))
        self.setFixedSize(1200, 600)
        self.show()


    def databaseSearchWindow(self, database=None):
        self.dbSearchWindow = DB_Search()
        self.dbSearchWindow.show()
        if database != None:
            self.dbSearchWindow.setWindowTitle(f"Lambda - Database Search - {database}")
        else:
            self.dbSearchWindow.setWindowTitle(f"Lambda - Database Search")
        self.dbSearchWindow.setWindowIcon(QtGui.QIcon('lambda.svg'))
        self.dbSearchWindow.setFixedSize(1200, 600)
        self.dbSearchWindow.show()


    def GithubAction():
                print("Opens Github")
                webbrowser.open("https://github.com/seamusmullan/CherryBomb")


    ## MISC FUNCTIONS

    def progBarAdd(self, n):
        self.progBar.setValue(self.progBar.value() + n)
        self.progBar.update()

    def progBarSet(self, n):
        self.progBar.setValue(n)
        self.progBar.update()

    def progBarSmooth(self, start, end, sleepTime):
        self.progBar.setValue(start)
        for i in range(start, end):
            self.progBar.setValue(i)
            self.progBar.update()
            time.sleep(sleepTime)

    def progBarReset(self, ):
        self.progBar.setValue(0)
        self.progBar.update()

    def yesNoWindow(self, text):
        self.yesNoWindow = QtWidgets.QMessageBox.question(self, 'Message', text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        return self.yesNoWindow

    def errorWindow(self, text):
        self.errorWindow = QtWidgets.QMessageBox.critical(self, 'Error', text, QtWidgets.QMessageBox.Ok)
        self.errorWindow.show()

    def infoWindow(self, text):
        self.infoWindow = QtWidgets.QMessageBox.information(self, 'Info', text, QtWidgets.QMessageBox.Ok)
        self.infoWindow.show()


    ## DATABASE FUNCTIONS

    def dbSetup(self, platform):
        ## if database doesn't exist, create it and add the table + columns
        conn = sqlite3.connect(f"{platform}.db")
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS accounts (username text, platform text, followers int, following int, posts int, link text, bio text)")
        conn.commit()
        conn.close()

    def dbAdd(self, platform, username, link, followers, following, posts, bio):
        conn = sqlite3.connect(f"{platform}.db")
        c = conn.cursor()
        c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?, ?, ?)", (username, platform, followers, following, posts, link, bio))
        conn.commit()
        conn.close()

    ## TABLE FUNCTIONS

    def tableSetup(self):
        headers = ["Username", "Platform", "Followers", "Following", "No. Posts", "Link", "Bio"]
        for i in range(0, len(headers)):
            self.tableWidget.insertColumn(i)
        self.tableWidget.setHorizontalHeaderLabels(headers)


    def addToTable(self, item, platform=None, followers=None, following=None, posts=None, link=None, bio=None):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(item))
        
        ## DETAILS

        if platform != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(platform))
        if followers != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(str(followers)))
        if following != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(following)))
        if posts != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 4, QtWidgets.QTableWidgetItem(str(posts)))
        if link != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 5, QtWidgets.QTableWidgetItem(link))
        if bio != None:
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 6, QtWidgets.QTableWidgetItem(bio))


    ## ADD ACCOUNT FUNCTIONS

    def inputWindow(self, text):
        x = QtWidgets.QInputDialog.getText(self, 'Input Dialog', text)
        if x != None:
            pass
        else:
            self.errorWindow(str("Nothing Entered"))
        return x[0]
            

    def addIGAccount(self, platform):
        self.dbSetup(platform)
        link = str(self.inputWindow(str("Enter Link to Account")))
        username = str(self.inputWindow(str("Enter Username for Account")))
        self.progBarSmooth(0, 20, 0.1)
        # self.addToTable(nickname, platform, link=link)
        data = getUserIG(clientLoginIG("calmingnatureposts", "xN353@uxr"), username)
        self.progBarSmooth(20, 40, 0.2)
        self.addToTable(username, platform, data['follower_count'], data['following_count'], data['media_count'], link, data['biography'])
        self.dbAdd(platform, username, link, data['follower_count'], data['following_count'], data['media_count'], data['biography'])
        self.progBarSmooth(40, 110, 0.01)


    def addFBAccount(self, platform):
        self.dbSetup(platform)
        pass


    def addTwitterAccount(self, platform):
        self.dbSetup(platform)
        pass


    def addSnapchatAccount(self, platform):
        self.dbSetup(platform)
        pass


    def addTiktokAccount(self, platform):
        self.dbSetup(platform)
        pass




    def buttonSetup(self):
        ## MENU BUTTONS
        self.actionGithub.triggered.connect(lambda: webbrowser.open("https://github.com/seamusmullan"))

        ## ADD ACCOUNT BUTTONS
        self.IGButton.clicked.connect(lambda: th.Thread(target=self.addIGAccount, args=("Instagram",)).start())
        self.FBButton.clicked.connect(lambda: th.Thread(target=self.addFBAccount, args=("Facebook",)).start())
        self.TWButton.clicked.connect(lambda: th.Thread(target=self.addTwitterAccount, args=("Twitter",)).start())
        self.SCButton.clicked.connect(lambda: th.Thread(target=self.addSnapchatAccount, args=("Snapchat",)).start())
        self.TTButton.clicked.connect(lambda: th.Thread(target=self.addTiktokAccount, args=("TikTok",)).start())

        ## STATISTICS BUTTONS



        ## DATABASE BUTTONS
        self.DBSearchButton.clicked.connect(lambda: self.databaseSearchWindow())
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.buttonSetup()
    window.progBarReset()
    window.tableSetup()
    window.show()
    sys.exit(app.exec_())
