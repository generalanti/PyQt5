from PyQt5 import QtWidgets, QtGui, QtCore
from guidarktheme.widget_template import QDarkPalette

from test_window import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setFont(QtGui.QFont('SansSerif', 14)
                              )  # изменить шрифт виджета label
        self.ui.label.setGeometry(QtCore.QRect(10, 50, 400, 200)
                                  )  # изменить геометрию виджета label
        self.ui.label.setText("Этот текст переделан")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.setStyle('Fusion')



sys.exit(app.exec())
