import sys
from PyQt5 import QtWidgets
from ejemplo11 import Ui_MainWindow

def validar_nombre():
    nombre = ui.entrada_nombre.text()
    if nombre == "":
        ui.entrada_nombre.setStyleSheet("border: 1px solid red")
        return False   
    if not nombre.isalpha():
        ui.entrada_nombre.setStyleSheet("border: 1px solid red")
        return False
    if len(nombre) > 20:
        ui.entrada_nombre.setStyleSheet("border: 1px solid red")
        return False
    ui.entrada_nombre.setStyleSheet("border: 1px solid green")
    

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
# ui.enviar.clicked.connect(enviar)
ui.entrada_nombre.textChanged.connect(validar_nombre)

MainWindow.show()
sys.exit(app.exec_())