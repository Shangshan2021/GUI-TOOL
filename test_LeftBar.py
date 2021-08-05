import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Left_Bar import Ui_MainPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())