from PyQt5 import QtCore, QtWidgets, uic
import os,sys

BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))
UI_FOLDER = os.path.join(BASE_FOLDER,"ui")

main_window_ui_file = os.path.join(UI_FOLDER,"hello_world.ui")
main_window_uic = uic.loadUiType(main_window_ui_file)[0] ## Get Ui Class (Form Class)


class Calculator(QtWidgets.QMainWindow,main_window_uic):

    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Calculator()
    main_window.show()
    sys.exit(app.exec_())