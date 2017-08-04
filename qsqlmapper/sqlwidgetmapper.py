import sys
import maindialog
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

class MainDialog(QDialog, maindialog.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.setupmodel()

        self.relModel = self.model.relationModel(self.typeIndex)
        self.typeCombo.setModel(self.relModel)
        self.typeCombo.setModelColumn(self.relModel.fieldIndex(
                                             "description"))

        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(self.model)
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self.mapper))
        self.mapper.addMapping(self.nameEdit, self.model.fieldIndex("name"))
        self.mapper.addMapping(self.addressEdit,
                               self.model.fieldIndex("address"))
        self.mapper.addMapping(self.typeCombo, self.typeIndex)

        self.previousButton.clicked.connect(self.mapper.toPrevious)
        self.nextButton.clicked.connect(self.mapper.toNext)
        self.mapper.currentIndexChanged.connect(self.updateButtons)
        self.mapper.toFirst()

    def setupmodel(self):
        db = QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName("people")

        if not db.open():
            QMessageBox.warning(None, "Combo Box Example",
                                db.lastError().text())
            sys.exit(1)

        self.model = QSqlRelationalTableModel(self)
        self.model.setTable("person")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

        self.typeIndex = self.model.fieldIndex("typeid")
        self.model.setRelation(
            self.typeIndex, QSqlRelation("addresstype", "id", "description"))
        self.model.select()

    def updateButtons(self, row):
        self.previousButton.setEnabled(row > 0)
        self.nextButton.setEnabled(row < self.model.rowCount() - 1)
        if self.model.lastError().isValid():
            print(self.model.lastError().databaseText())

app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()