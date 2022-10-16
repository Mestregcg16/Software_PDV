#Imports
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets , QtGui ,QtCore ,uic
from PyQt5.QtWidgets import *
from connection import Data_base
from mysql.connector import Error
from datetime import datetime
import sys 
db = Data_base()

app = QApplication(sys.argv)

add_cliente = uic.loadUi("ui_files/add_cliente.ui")
cliente = uic.loadUi("ui_files\cliente .ui")




########################   CLIENTES  ########################

tempo = datetime.now()
data = tempo.strftime("%x")
hora = tempo.strftime("%X")
dt = data + " " + hora

def cadastro_cliente():
    line = add_cliente.nome.text()
    print(line)

  
        

def mostrar_cliente():
    clientes = db.select_all('cliente')
    cliente.tabela_cliente.clearContents()
    cliente.tabela_cliente.setRowCount(len(clientes))

    for row, text in enumerate(clientes):
        for column, data in enumerate(text):
            cliente.tabela_cliente.setItem(
                row, column, QTableWidgetItem(str(data)))




def show_messagebox(title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(str(text))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setModal(True)
        exec = msg.exec_()
        return exec

def show_QIpuntDialog(title,text):
    dlg =  QInputDialog()                 
    dlg.setInputMode( QInputDialog.TextInput) 
    dlg.setLabelText(text) 
    dlg.setWindowTitle(title)                   
    dlg.resize(300,300)                             
    dlg.setFont(QFont('Arial', 10))
    dlg.setWindowIcon(QtGui.QIcon('btn_icons\setting.png'))
    dlg.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint,False)
    dlg.setModal(True)
    
    ok = dlg.exec_()
    if ok:                                
        text = dlg.getText()
        return text
    else:
        return None



