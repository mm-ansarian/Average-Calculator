from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys


# TODO (2024-07-27, Mohammad Mahdi Ansarian): Put every widgets in an organized table layout.
class uiPage(object):
    def __init__(self):
        self.counter = 1  # Initialize "counter" to count the number of calculated averages.
        self.numbers_list = []  # Initialize "numbers_list" to store entered numbers.
        self.numbers_list_trash = []  # Initialize "numbers_list_trash" to store deleted numbers.

    def setupUi(self, main_window):
        # Main window set up with fixed size and an icon.
        main_window.setObjectName("mainWindow")
        main_window.setEnabled(True)
        main_window.resize(900, 589)
        main_window.setMinimumSize(QtCore.QSize(900, 589))
        main_window.setMaximumSize(QtCore.QSize(900, 589))
        main_window.setBaseSize(QtCore.QSize(900, 589))
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, "Icon.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "Icon.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.averages_text_browser.setObjectName("resultPage")

        # Initialize the result page with a header.
        self.averages_text_browser.setPlainText("**  Averages  **\n\n")

        # Set up the "Add" button.
        self.add_number_button = QtWidgets.QPushButton(main_window)
        self.add_number_button.setGeometry(QtCore.QRect(40, 90, 230, 60))
        self.add_number_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_number_button.setSizeIncrement(QtCore.QSize(71, 20))
        self.add_number_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.add_number_button.setFont(font)
        self.add_number_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_number_button.setObjectName("addBtn")

        # Set up the "Calculate" button.
        self.calculate_numbers_button = QtWidgets.QPushButton(main_window)
        self.calculate_numbers_button.setGeometry(QtCore.QRect(40, 180, 231, 61))
        self.calculate_numbers_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.calculate_numbers_button.setFont(font)
        self.calculate_numbers_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_numbers_button.setObjectName("calcBtn")

        # Set up the input field for getting numbers.
        self.number_input_text_box = QtWidgets.QLineEdit(main_window)
        self.number_input_text_box.setGeometry(QtCore.QRect(10, 10, 290, 50))
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
        self.number_input_text_box.setObjectName("numberInput")

        # Set up the "Clear all" button.
        self.clear_all_button = QtWidgets.QPushButton(main_window)
        self.clear_all_button.setGeometry(QtCore.QRect(40, 270, 231, 61))
        self.clear_all_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all_button.setObjectName("clearBtn")

        # Set up a text browser to display the list of added numbers.
        self.numbers_text_browser = QtWidgets.QTextBrowser(main_window)
        self.numbers_text_browser.setGeometry(QtCore.QRect(10, 420, 880, 161))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(12)
        font.setItalic(True)
        self.numbers_text_browser.setFont(font)
        self.numbers_text_browser.setObjectName("numbers")
        self.numbers_text_browser.setPlainText("**  Numbers  **")

        # Set up the "Go back" button.
        self.go_back_button = QtWidgets.QPushButton(mainWindow)
        self.go_back_button.setEnabled(False)
        self.go_back_button.setGeometry(QtCore.QRect(40, 350, 111, 61))
        self.go_back_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(75)
        self.go_back_button.setFont(font)
        self.go_back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_back_button.setToolTip("")
        self.go_back_button.setStatusTip("")
        self.go_back_button.setAccessibleDescription("")
        self.go_back_button.setObjectName("goBackBtn")

        # Set up the "Go forward" button.
        self.go_forward_button = QtWidgets.QPushButton(mainWindow)
        self.go_forward_button.setEnabled(False)
        self.go_forward_button.setGeometry(QtCore.QRect(160, 350, 111, 61))
        self.go_forward_button.setBaseSize(QtCore.QSize(71, 20))
        font = QtGui.QFont()
        font.setFamily("Calisto MT")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.go_forward_button.setFont(font)
        font.setWeight(75)
        self.go_forward_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_forward_button.setStatusTip("")
        self.go_forward_button.setAccessibleDescription("")
        self.go_forward_button.setObjectName("goForwardBtn")

        # Connect button clicks to their respective methods.
        self.retranslateUi(main_window)
        self.add_number_button.clicked.connect(self.add_number)
        self.calculate_numbers_button.clicked.connect(self.calculate_numbers)
        self.clear_all_button.clicked.connect(self.clear)
        self.go_back_button.clicked.connect(self.go_back)
        self.go_forward_button.clicked.connect(self.go_forward)
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
                self.go_back_button.setEnabled(True)
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
        self.go_back_button.setEnabled(False)
        self.go_forward_button.setEnabled(False)
        self.numbers_list_trash.clear()



    def clear(self):
        # Clear everything.
        self.numbers_list.clear()
        self.number_input_text_box.clear()
        self.numbers_text_browser.setPlainText("**  Numbers  **")
        self.averages_text_browser.setPlainText("**  Averages  **\n\n")
        self.counter = 1
        self.number_input_text_box.setFocus()
        self.go_back_button.setEnabled(False)
        self.go_forward_button.setEnabled(False)
        self.numbers_list_trash.clear()

    def go_back(self):
        # If the "go_back_button" was pressed, the program will back to the privius conditions. 
        self.go_forward_button.setEnabled(True)
        if self.numbers_list:
            poped_item = len(self.numbers_list) - 1
            self.numbers_list_trash.append(self.numbers_list.pop())
            self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} numbers added  **\n\n{", ".join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} number added  **\n\n{", ".join(map(str, self.numbers_list))}")
        if not self.numbers_list:
            self.go_back_button.setEnabled(False)
        if not self.numbers_list_trash:
            self.go_forward_button.setEnabled(False)
        self.number_input_text_box.setFocus()


    def go_forward(self):
        # If the "go_back_button" was pressed, the program will back to the last conditions. 
        self.go_back_button.setEnabled(True)
        if self.numbers_list_trash:
            poped_item = self.numbers_list_trash[-1]
            self.numbers_list.append(poped_item)
            if float(poped_item) % 1 == 0:
                self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} numbers added  **\n\n{", ".join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} number added  **\n\n{", ".join(map(str, self.numbers_list))}")
            else:
                self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} numbers added  **\n\n{", ".join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"**  {len(self.numbers_list)} number added  **\n\n{", ".join(map(str, self.numbers_list))}")
            self.numbers_list_trash.pop()
        if not self.numbers_list:
            self.go_back_button.setEnabled(False)
        else:
            self.go_back_button.setEnabled(True)
        if not self.numbers_list_trash:
            self.go_forward_button.setEnabled(False)
        else:
            self.go_forward_button.setEnabled(True)
        self.number_input_text_box.setFocus()


    def retranslateUi(self, MainWindow):
        # Set the text for various UI elements.
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Page", "Average Calculator"))
        self.add_number_button.setText(_translate("Page", "Add"))
        self.add_number_button.setShortcut(_translate("mainWindow", "Return"))
        self.calculate_numbers_button.setText(_translate("Page", "Calculate"))
        self.calculate_numbers_button.setShortcut(_translate("mainWindow", "Ctrl+Return"))
        self.number_input_text_box.setPlaceholderText(_translate("Page", "Enter Number"))
        self.clear_all_button.setText(_translate("Page", "Clear all"))
        self.clear_all_button.setShortcut(_translate("mainWindow", "Ctrl+F10"))
        self.go_back_button.setText(_translate("mainWindow", "<="))
        self.go_back_button.setShortcut(_translate("mainWindow", "Alt+Left"))
        self.go_forward_button.setText(_translate("mainWindow", "=>"))
        self.go_forward_button.setShortcut(_translate("mainWindow", "Alt+Right"))


# Run the program.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QFrame()
    ui = uiPage()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
