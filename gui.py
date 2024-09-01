from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os


# TODO (2024-07-27, Mohammad Mahdi Ansarian): Put every widgets in an organized table layout.
# "UiPage" is a class to setup the GUI of the program.
class UiPage():
    def __init__(self) -> None:
        self.counter = 1  # Initialize "counter" to count the number of calculated averages.
        self.numbers_list = []  # Initialize "numbers_list" to store entered numbers.
        self.numbers_list_trash = []  # Initialize "numbers_list_trash" to store deleted numbers.

    def setup_ui(self, main_window: object) -> None:
        # Main window set up with fixed size and an icon.
        main_window.setObjectName("mainWindow")
        main_window.setEnabled(True)
        main_window.resize(900, 589)
        main_window.setMinimumSize(QtCore.QSize(900, 589))
        main_window.setMaximumSize(QtCore.QSize(900, 589))
        main_window.setBaseSize(QtCore.QSize(900, 589))
        if hasattr(sys, '_MEIPASS'):
            icon_path1 = os.path.join(sys._MEIPASS, "Icon.ico")
        else:
            icon_path1 = os.path.join(os.path.dirname(__file__), "Icon.ico")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(icon_path1), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon1)

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
        self.averages_text_browser.setPlaceholderText("Averages")

        # Set up the "Add" button.
        self.add_number_button = QtWidgets.QPushButton(main_window)
        self.add_number_button.setGeometry(QtCore.QRect(40, 90, 230, 60))
        self.add_number_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_number_button.setSizeIncrement(QtCore.QSize(71, 20))
        self.add_number_button.setBaseSize(QtCore.QSize(71, 20))
        self.add_number_button.setFont(font)
        self.add_number_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_number_button.setObjectName("addBtn")
        self.add_number_button.setToolTip("Add(Enter)")

        # Set up the "Calculate" button.
        self.calculate_numbers_button = QtWidgets.QPushButton(main_window)
        self.calculate_numbers_button.setGeometry(QtCore.QRect(40, 180, 231, 61))
        self.calculate_numbers_button.setBaseSize(QtCore.QSize(71, 20))
        self.calculate_numbers_button.setFont(font)
        self.calculate_numbers_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate_numbers_button.setObjectName("calcBtn")
        self.calculate_numbers_button.setToolTip("Calculate(Ctrl+Enter)")

        # Set up the input field for getting numbers.
        self.number_input_text_box = QtWidgets.QLineEdit(main_window)
        self.number_input_text_box.setGeometry(QtCore.QRect(10, 10, 290, 50))
        self.number_input_text_box.setSizeIncrement(QtCore.QSize(0, 0))
        self.number_input_text_box.setBaseSize(QtCore.QSize(110, 20))
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
        self.clear_all_button.setFont(font)
        self.clear_all_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_all_button.setObjectName("clearBtn")
        self.clear_all_button.setToolTip("Clear(Ctrl+F10)")

        # Set up a text browser to display the list of added numbers.
        self.numbers_text_browser = QtWidgets.QTextBrowser(main_window)
        self.numbers_text_browser.setGeometry(QtCore.QRect(10, 420, 880, 161))
        self.numbers_text_browser.setFont(font)
        self.numbers_text_browser.setObjectName("numbers")
        self.numbers_text_browser.setPlaceholderText("Added numbers")

        # Set up the "Go back" button.
        self.go_back_button = QtWidgets.QPushButton(main_window)
        self.go_back_button.setEnabled(False)
        self.go_back_button.setGeometry(QtCore.QRect(40, 350, 111, 61))
        self.go_back_button.setBaseSize(QtCore.QSize(71, 20))
        self.go_back_button.setFont(font)
        self.go_back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_back_button.setToolTip("")
        self.go_back_button.setStatusTip("")
        self.go_back_button.setAccessibleDescription("")
        self.go_back_button.setText("")
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, "Icons", "Back Icon.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "Icons", "Back Icon.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_back_button.setIcon(icon)
        self.go_back_button.setIconSize(QtCore.QSize(24, 24))
        self.go_back_button.setObjectName("goBackBtn")
        self.go_back_button.setToolTip("Back(Alt+LeftArrow)")

        # Set up the "Go forward" button.
        self.go_forward_button = QtWidgets.QPushButton(main_window)
        self.go_forward_button.setEnabled(False)
        self.go_forward_button.setGeometry(QtCore.QRect(160, 350, 111, 61))
        self.go_forward_button.setBaseSize(QtCore.QSize(71, 20))
        self.go_forward_button.setFont(font)
        self.go_forward_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_forward_button.setStatusTip("")
        self.go_forward_button.setAccessibleDescription("")
        if hasattr(sys, '_MEIPASS'):
            icon_path = os.path.join(sys._MEIPASS, "Icons", "Forward Icon.ico")
        else:
            icon_path = os.path.join(os.path.dirname(__file__), "Icons", "Forward Icon.ico")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.go_forward_button.setIcon(icon)
        self.go_forward_button.setIconSize(QtCore.QSize(24, 24))
        self.go_forward_button.setObjectName("goForwardBtn")
        self.go_forward_button.setToolTip("Forward(Alt+RightArrow)")

        # Connect button clicks to their respective methods.
        self.retranslateUi(main_window)
        self.setup_signals()
        QtCore.QMetaObject.connectSlotsByName(main_window)

    # Setup the signals.
    def setup_signals(self) -> None:
        self.add_number_button.clicked.connect(lambda: UiReactions.add_function(self))
        self.calculate_numbers_button.clicked.connect(lambda: UiReactions.calculate_function(self))
        self.clear_all_button.clicked.connect(lambda: UiReactions.clear_function(self))
        self.go_back_button.clicked.connect(lambda: UiReactions.go_back_function(self))
        self.go_forward_button.clicked.connect(lambda: UiReactions.go_forward_function(self))

    # Set the text for various UI elements.
    def retranslateUi(self, MainWindow: object) -> None:
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Page", "Average Calculator"))
        self.add_number_button.setText(_translate("Page", "Add"))
        self.add_number_button.setShortcut(_translate("mainWindow", "Return"))
        self.calculate_numbers_button.setText(_translate("Page", "Calculate"))
        self.calculate_numbers_button.setShortcut(_translate("mainWindow", "Ctrl+Return"))
        self.number_input_text_box.setPlaceholderText(_translate("Page", "Enter Number"))
        self.clear_all_button.setText(_translate("Page", "Clear all"))
        self.clear_all_button.setShortcut(_translate("mainWindow", "Ctrl+F10"))
        self.go_back_button.setShortcut(_translate("mainWindow", "Alt+Left"))
        self.go_forward_button.setShortcut(_translate("mainWindow", "Alt+Right"))


# "UiReactions" is a class including some methods which specify what should happen if the user takes an action on the main window.
class UiReactions(UiPage):
    # "__init__" method from "UiPage" class.
    def __init__(self) -> None:
        super().__init__(self)

    # "setup_ui" method from "UiPage" class.
    def setup_ui(self, main_window: object) -> None:
        super().setup_ui(self, main_window)

    # The "add_number_function" adds the number from the input field to the "numbers_list" and update the display.
    def add_function(self) -> None:
        if self.number_input_text_box.text() != "":
            try:
                # Display the added numbers in the "numbers" page.
                if float(self.number_input_text_box.text()) % 1 == 0:
                    self.numbers_list.append(int(float(self.number_input_text_box.text())))
                    self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} numbers added\n\n{', '.join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} number added\n\n{', '.join(map(str, self.numbers_list))}")
                else:
                    self.numbers_list.append(float(self.number_input_text_box.text()))
                    self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} numbers added\n\n{', '.join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} number added\n\n{', '.join(map(str, self.numbers_list))}")
                self.go_back_button.setEnabled(True)
            except ValueError:
                # Clear input field if the value is not a number.
                self.number_input_text_box.clear()
        self.number_input_text_box.clear()
        self.number_input_text_box.setFocus()

    # The "calculate_numbers" calculates the average of the numbers in the list and display it.
    def calculate_function(self) -> None:
        try:
            # Calculate the average and display it.
            result = round(sum(self.numbers_list) / len(self.numbers_list), 2)
            self.averages_text_browser.append(f"{self.counter}. Average of {len(self.numbers_list)} numbers ({', '.join(map(str, self.numbers_list))}):  {result}") if len(self.numbers_list) > 1 else self.averages_text_browser.append(f"{self.counter}) Average of {len(self.numbers_list)} number ({', '.join(map(str, self.numbers_list))}):  {result}")
            self.averages_text_browser.append(f"\n")
            # Clear the number list and increment the counter for the next calculation.
            self.numbers_list.clear()
            self.counter += 1
            self.number_input_text_box.clear()
        except ZeroDivisionError:
            pass
        # Clear the displayed numbers and refocus the input field.
        self.numbers_text_browser.clear()
        self.numbers_text_browser.setPlaceholderText("Added numbers")
        self.number_input_text_box.setFocus()
        self.go_back_button.setEnabled(False)
        self.go_forward_button.setEnabled(False)
        self.numbers_list_trash.clear()

    # The "clear_function" clears all the data from the window.
    def clear_function(self) -> None:
        self.numbers_list.clear()
        self.number_input_text_box.clear()
        self.numbers_text_browser.clear()
        self.numbers_text_browser.setPlaceholderText("Added numbers")
        self.averages_text_browser.clear()
        self.averages_text_browser.setPlaceholderText("Averages")
        self.counter = 1
        self.number_input_text_box.setFocus()
        self.go_back_button.setEnabled(False)
        self.go_forward_button.setEnabled(False)
        self.numbers_list_trash.clear()

    # If the "go_back_button" was pressed, the program will back to the previous conditions. 
    def go_back_function(self) -> None:
        self.go_forward_button.setEnabled(True)
        if self.numbers_list:
            removed_item = len(self.numbers_list) - 1
            self.numbers_list_trash.append(self.numbers_list.pop())
            self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} numbers added\n\n{', '.join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} number added\n\n{', '.join(map(str, self.numbers_list))}")
        if not self.numbers_list:
            self.go_back_button.setEnabled(False)
        if not self.numbers_list_trash:
            self.go_forward_button.setEnabled(False)
        self.number_input_text_box.setFocus()
   
    # If the "go_forward_button" was pressed, the program will back to the canceled conditions. 
    def go_forward_function(self) -> None:
        self.go_back_button.setEnabled(True)
        if self.numbers_list_trash:
            removed_item = self.numbers_list_trash[-1]
            self.numbers_list.append(removed_item)
            if float(removed_item) % 1 == 0:
                self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} numbers added\n\n{', '.join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} number added\n\n{', '.join(map(str, self.numbers_list))}")
            else:
                self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} numbers added\n\n{', '.join(map(str, self.numbers_list))}") if len(self.numbers_list) > 1 else self.numbers_text_browser.setPlainText(f"{len(self.numbers_list)} number added\n\n{', '.join(map(str, self.numbers_list))}")
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
