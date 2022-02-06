import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import webbrowser
from qt_material import apply_stylesheet, QtStyleTools
import threading
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Ui(QtWidgets.QMainWindow, QtStyleTools):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("MainWindow.ui", self)
        self.apply_stylesheet(app, "dark_red.xml")
        self.setWindowTitle('Lambda')
        self.setWindowIcon(QtGui.QIcon('lambda.svg'))
        self.setFixedSize(1200, 600)
        self.show()

    def GithubAction():
                print("Opens Github")
                webbrowser.open("https://github.com/seamusmullan/CherryBomb")


    ## MISC FUNCTIONS

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


    ## TABLE FUNCTIONS

    def tableSetup(self):
        headers = ["Nickname", "Platform", "Followers", "Following", "No. Posts", "Link", "Bio"]
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
            

    def addAccount(self, platform):
        link = str(self.inputWindow(str("Enter Link to Account")))
        nickname = str(self.inputWindow(str("Enter Nickname for Account")))
        self.addToTable(nickname, platform, link=link)


    def buttonSetup(self):
        self.actionGithub.triggered.connect(lambda: webbrowser.open("https://github.com/seamusmullan"))

        self.IGButton.clicked.connect(lambda: self.addAccount("Instagram"))
        self.FBButton.clicked.connect(lambda: self.addAccount("Facebook"))
        self.TWButton.clicked.connect(lambda: self.addAccount("Twitter"))
        self.SCButton.clicked.connect(lambda: self.addAccount("Snapchat"))
        self.TTButton.clicked.connect(lambda: self.addAccount("TikTok"))
        


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.buttonSetup()
    window.progBarReset()
    window.tableSetup()
    window.show()
    sys.exit(app.exec_())
