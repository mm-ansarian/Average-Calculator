from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.ui.setupUi(self)

    # If Enter key is pressed, the add_number() will be called.
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.ui.add_number()


class UiPage(object):
    def __init__(self):
        self.counter = 1  # Initialize counter for number of averages calculated.
        self.numbers_list = []  # initialize numbers_list to store entered numbers.

    def setupUi(self, main_window):
        # Main window set up with fixed size and an icon.
        main_window.setObjectName("MainWindow")
        main_window.setEnabled(True)
        main_window.resize(900, 589)
        main_window.setMinimumSize(QtCore.QSize(900, 589))
        main_window.setMaximumSize(QtCore.QSize(900, 589))
        main_window.setBaseSize(QtCore.QSize(900, 589))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)

        # Set up the text browser to display results.
        self.averages_text_browser = QtWidgets.QTextBrowser(main_window)
        self.averages_text_browser.setGeometry(QtCore.QRect(340, 10, 551, 400))
        self.averages_text_browser.setBaseSize(QtCore.QSize(321, 231))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.averages_text_browser.setFont(font)
        self.averages_text_browser.setObjectName("ResultPage")

        # Initialize the result page with a header.
        self.averages_text_browser.setPlainText("**  Averages  **\n\n")

        # Set up the "Add" button.
        self.add_number_button = QtWidgets.QPushButton(main_window)
        self.add_number_button.setGeometry(QtCore.QRect(40, 140, 230, 60))
        self.add_number_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_number_button.setSizeIncrement(QtCore.QSize(71, 20))
        self.add_number_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.add_number_button.setFont(font)
        self.add_number_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_number_button.setObjectName("AddBtn")

        # Set up the "Calculate" button.
        self.calculate_numbers_button = QtWidgets.QPushButton(main_window)
        self.calculate_numbers_button.setGeometry(QtCore.QRect(40, 240, 231, 61))
        self.calculate_numbers_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.calculate_numbers_button.setFont(font)
        self.calculate_numbers_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_numbers_button.setObjectName("CalcBtn")

        # Set up the input field for getting numbers.
        self.number_input_text_box = QtWidgets.QLineEdit(main_window)
        self.number_input_text_box.setGeometry(QtCore.QRect(10, 40, 290, 50))
        self.number_input_text_box.setSizeIncrement(QtCore.QSize(0, 0))
        self.number_input_text_box.setBaseSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.number_input_text_box.setFocus()
        self.number_input_text_box.setFont(font)
        self.number_input_text_box.setText("")
        self.number_input_text_box.setMaxLength(12)
        self.number_input_text_box.setDragEnabled(False)
        self.number_input_text_box.setClearButtonEnabled(False)
        self.number_input_text_box.setObjectName("NumberInput")

        # Set up the "Clear all" button.
        self.clear_all_button = QtWidgets.QPushButton(main_window)
        self.clear_all_button.setGeometry(QtCore.QRect(40, 340, 231, 61))
        self.clear_all_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all_button.setObjectName("ClearBtn")

        # Set up a text browser to display the list of added numbers.
        self.numbers_text_browser = QtWidgets.QTextBrowser(main_window)
        self.numbers_text_browser.setGeometry(QtCore.QRect(10, 420, 880, 161))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.numbers_text_browser.setFont(font)
        self.numbers_text_browser.setObjectName("Numbers")
        self.numbers_text_browser.setPlainText("**  Numbers  **")

        # Connect button clicks to their respective methods.
        self.retranslateUi(main_window)
        self.add_number_button.clicked.connect(self.add_number)
        self.calculate_numbers_button.clicked.connect(self.calculate_numbers)
        self.clear_all_button.clicked.connect(self.clear)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def add_number(self):
        # Add the number from the input field to the numbers list and update the display.
        if self.number_input_text_box != "":
            try:
                # Display the added numbers in the "numbers" page.
                if float(self.number_input_text_box.text()) % 1 == 0:
                    self.numbers_list.append(int(float(self.number_input_text_box.text())))
                    self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} numbers added  **\n\n{", ".join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} number added  **\n\n{", ".join(map(str, self.numbers_list))}")
                else:
                    self.numbers_list.append(float(self.number_input_text_box.text()))
                    self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} numbers added  **\n\n{", ".join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} number added  **\n\n{", ".join(map(str, self.numbers_list))}")
            except ValueError:
                # Clear input field if the value is not a number.
                self.number_input_text_box.clear()
        self.number_input_text_box.clear()
        self.number_input_text_box.setFocus()

    def calculate_numbers(self):
        # Calculate the average of the numbers in the list and display it.
        try:
            # Calculate the average and display it.
            result = round(sum(self.numbers_list) / len(self.numbers_list), 2)
            self.averages_text_browser.append(f"{self.counter}) Average of {len(self.numbers_list)} numbers ({', '.join(map(str, self.numbers_list))}):  {result}") if len(self.numbers_list) > 1 else self.averages_text_browser.append(f"{self.counter}) Average of {len(self.numbers_list)} number ({', '.join(map(str, self.numbers_list))}):  {result}")
            self.averages_text_browser.append(f"\n")
            # Clear the number list and increment the counter for the next calculation.
            self.numbers_list.clear()
            self.counter += 1
            self.number_input_text_box.clear()
        except ZeroDivisionError:
            pass
        # Clear the displayed numbers and refocus the input field.
        self.numbers_text_browser.setPlainText("**  Numbers  **")
        self.number_input_text_box.setFocus()

    def clear(self):
        # Clear everything.
        self.numbers_list.clear()
        self.number_input_text_box.clear()
        self.numbers_text_browser.setPlainText("**  Numbers  **")
        self.averages_text_browser.setPlainText("**  Averages  **\n\n")
        self.counter = 1
        self.number_input_text_box.setFocus()

    def retranslateUi(self, MainWindow):
        # Set the text for various UI elements.
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Page", "Average Calculator"))
        self.add_number_button.setText(_translate("Page", "Add"))
        self.calculate_numbers_button.setText(_translate("Page", "Calculate"))
        self.number_input_text_box.setPlaceholderText(_translate("Page", "Enter Number"))
        self.clear_all_button.setText(_translate("Page", "Clear all"))


# Run the program.
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiPage()
    mainWindow = MainWindow(ui)
    mainWindow.show()
    sys.exit(app.exec_())
