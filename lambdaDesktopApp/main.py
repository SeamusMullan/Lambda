import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import os
import instaloader
import threading
import webbrowser
import qdarkstyle


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        # scale with the screen size
        self.setWindowTitle('Lambda')
        self.setWindowIcon(QtGui.QIcon('lambda.png'))
        self.setFixedSize(1200, 600)
        self.show()

    def GithubAction():
                print("Opens Github")
                webbrowser.open("https://github.com/seamusmullan/CherryBomb")

    def tableSetup(self):
        headers = ["Profile Link", "Platform", "Followers", "Following", "Post Amount", "Synced"]
        for i in range(0, len(headers)):
            self.tableWidget.insertColumn(i)
        self.tableWidget.setHorizontalHeaderLabels(headers)

    def addToTable(self, item):
        self.tableWidget.insertRow(self.tableWidget.rowCount())
        self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(item))

    def progBarAdd(self, n):
        self.progBar.setValue(self.progBar.value() + n)

    def progBarSet(self, n):
        self.progBar.setValue(n)

    def progBarReset(self, ):
        self.progBar.setValue(0)   

    def yesNoWindow(self, text):
        self.yesNoWindow = QtWidgets.QMessageBox.question(self, 'Message', text, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        return self.yesNoWindow

    def errorWindow(self, text):
        self.errorWindow = QtWidgets.QMessageBox.critical(self, 'Error', text, QtWidgets.QMessageBox.Ok)
        self.errorWindow.show()
    
    ## ADD ACCOUNT FUNCTIONS

    def inputWindow(self, text):
        x = QtWidgets.QInputDialog.getText(self, 'Input Dialog', text)
        if x[1]:
            self.addToTable(x[0])
        else:
            self.errorWindow(str("No Username Entered"))
            

    def buttonSetup(self):
        self.actionGithub.triggered.connect(lambda: webbrowser.open("https://github.com/seamusmullan"))

    	## Add Account Buttons
        # IGButton, FBButton, TWButton, SCButton, TTButton

        self.IGButton.clicked.connect(lambda: self.inputWindow(str("Enter Instagram Username")))
        self.FBButton.clicked.connect(lambda: self.inputWindow(str("Enter Facebook Username")))
        self.TWButton.clicked.connect(lambda: self.inputWindow(str("Enter Twitter Username")))
        self.SCButton.clicked.connect(lambda: self.inputWindow(str("Enter Snapchat Username")))
        self.TTButton.clicked.connect(lambda: self.inputWindow(str("Enter TikTok Username")))
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = Ui()
    window.buttonSetup()
    window.progBarReset()
    window.tableSetup()
    window.show()
    sys.exit(app.exec_())
