"""
        بسم الله الرحمن الرحیم

        Project name: Main

        Programmer: Mohammad Mahdi Ansarian

        Letters: Ee, Qq, Xx

        Definition: A program to practice creating a GUI.
"""


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.setupUi(self)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.ui.add_score()


class Ui_Page(object):
    def __init__(self):
        self.counter = 1
        self.score_list = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 589)
        MainWindow.setMinimumSize(QtCore.QSize(900, 589))
        MainWindow.setMaximumSize(QtCore.QSize(900, 589))
        MainWindow.setBaseSize(QtCore.QSize(900, 589))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Average Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.resultPage = QtWidgets.QTextBrowser(MainWindow)
        self.resultPage.setGeometry(QtCore.QRect(340, 10, 551, 400))
        self.resultPage.setBaseSize(QtCore.QSize(321, 231))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.resultPage.setFont(font)
        self.resultPage.setObjectName("resultPage")
        self.addButton = QtWidgets.QPushButton(MainWindow)
        self.addButton.setGeometry(QtCore.QRect(40, 140, 230, 60))
        self.addButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.addButton.setSizeIncrement(QtCore.QSize(71, 20))
        self.addButton.setBaseSize(QtCore.QSize(71, 20))
        self.resultPage.setPlainText("**  Averages  **\n\n")
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.addButton.setFont(font)
        self.addButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addButton.setObjectName("addButton")
        self.calculateButton = QtWidgets.QPushButton(MainWindow)
        self.calculateButton.setGeometry(QtCore.QRect(40, 240, 231, 61))
        self.calculateButton.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.calculateButton.setFont(font)
        self.calculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateButton.setObjectName("calculateButton")
        self.scoreInput = QtWidgets.QLineEdit(MainWindow)
        self.scoreInput.setGeometry(QtCore.QRect(10, 40, 290, 50))
        self.scoreInput.setSizeIncrement(QtCore.QSize(0, 0))
        self.scoreInput.setBaseSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.scoreInput.setFocus()
        self.scoreInput.setFont(font)
        self.scoreInput.setText("")
        self.scoreInput.setMaxLength(7)
        self.scoreInput.setDragEnabled(False)
        self.scoreInput.setClearButtonEnabled(False)
        self.scoreInput.setObjectName("scoreInput")
        self.clearButton = QtWidgets.QPushButton(MainWindow)
        self.clearButton.setGeometry(QtCore.QRect(40, 340, 231, 61))
        self.clearButton.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.clearButton.setFont(font)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setObjectName("clearButton")
        self.scores = QtWidgets.QTextBrowser(MainWindow)
        self.scores.setGeometry(QtCore.QRect(10, 420, 880, 161))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.scores.setFont(font)
        self.scores.setObjectName("scores")
        self.scores.setPlainText("**  Numbers  **")


        self.retranslateUi(MainWindow)
        self.addButton.clicked.connect(self.add_score)
        self.calculateButton.clicked.connect(self.calculate_score)
        self.clearButton.clicked.connect(self.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_score(self):
        if self.scoreInput != "":
            try:
                if float(self.scoreInput.text()) % 1 == 0:
                    self.score_list.append(int(self.scoreInput.text()))
                    self.scores.setPlainText(f"**  {len(self.score_list)} numbers added  **\n\n{", ".join(map(str, self.score_list))}") if len(self.score_list) > 1 else self.scores.setPlainText(f"**  {len(self.score_list)} number added  **\n\n{", ".join(map(str, self.score_list))}")
                else:
                    self.score_list.append(float(self.scoreInput.text()))
                    self.scores.setPlainText(f"**  {len(self.score_list)} numbers added  **\n\n{", ".join(map(str, self.score_list))}") if len(self.score_list) > 1 else self.scores.setPlainText(f"**  {len(self.score_list)} number added  **\n\n{", ".join(map(str, self.score_list))}")
            except ValueError:
                self.scoreInput.clear()
        self.scoreInput.clear()
        self.scoreInput.setFocus()

    def calculate_score(self):
        try:
            result = round(sum(self.score_list) / len(self.score_list), 2)
            self.resultPage.append(f"{self.counter}) Average of {len(self.score_list)} numbers ({', '.join(map(str, self.score_list))}):  {result}") if len(self.score_list) > 1 else self.resultPage.append(f"{self.counter}) Average of {len(self.score_list)} number ({', '.join(map(str, self.score_list))}):  {result}")
            self.resultPage.append(f"\n")
            self.score_list.clear()
            self.counter += 1
        except ZeroDivisionError:
            pass
        self.scores.setPlainText("**  Numbers  **")
        self.scoreInput.setFocus()

    def clear(self):
        self.score_list.clear()
        self.scores.setPlainText("**  Numbers  **")
        self.resultPage.setPlainText("**  Averages  **\n\n")
        self.counter = 1
        self.scoreInput.setFocus()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Page", "Average Calculator"))
        self.addButton.setText(_translate("Page", "Add"))
        self.calculateButton.setText(_translate("Page", "Calculate"))
        self.scoreInput.setPlaceholderText(_translate("Page", "Enter Score"))
        self.clearButton.setText(_translate("Page", "Clear all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Page()
    mainWindow = MainWindow(ui)
    mainWindow.show()
    sys.exit(app.exec_())
