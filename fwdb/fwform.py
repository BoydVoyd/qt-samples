import sys
import fwdbui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pypyodbc
from PyQt5.QtSql import *

class MainDialog(QDialog, fwdbui.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName('LocalCHS14')
        if not db.open():
            QMessageBox.warning(None, "Combo Box Example",
                                db.lastError().text())
            sys.exit(1)

        self.comboModel = QSqlTableModel(self)
        self.comboModel.setTable("facility_information")
        self.comboModel.setFilter('facility_primary_code IS NOT NULL')
        print(self.comboModel.selectStatement())
        self.comboModel.select()

        self.facilityBox.setModel(self.comboModel)
        self.facilityBox.setModelColumn(self.comboModel.fieldIndex("facility_primary_code"))
        self.facilityBox.currentIndexChanged.connect(self.box_activated)

    def box_activated(self):
        print(str(self.facilityBox.currentIndex()) + " " + self.facilityBox.currentText())

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()