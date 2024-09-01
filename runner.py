from PyQt5 import QtWidgets
import gui
import sys


# Run the program.
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QFrame()
    ui = gui.UiPage()
    ui.setup_ui(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
    