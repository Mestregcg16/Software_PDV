from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import Main_Icons.images as images
import Btn_Icons.buttons as buttons
from os import *


class main(QMainWindow):
    def __init__(self):
        super(main,self).__init__()

        #tela Principal 
        uic.loadUi("ui_files\main.ui", self)
        #Painel Cliente
        self.cliente = uic.loadUi("ui_files/cliente.ui")
        #Tela Menu_Os
        self.menu_os = uic.loadUi("ui_files/Menu_os.ui")
        #Tela Produtos
        self.produtos = uic.loadUi("ui_files/produtos.ui")
        #tela Menu Caixa
        self.menu_caixa = uic.loadUi("ui_files/menu_caixa.ui")


        #Tela add_Cliente
        self.abrir_add_cliente = uic.loadUi("ui_files/add_cliente.ui")
        #Tela add_produtos
        self.abrir_novo_produto = uic.loadUi("ui_files/add_produto.ui")
        #Tela add_OS
        self.add_os = uic.loadUi("ui_files/add_os.ui")
        

        
        
        #Abrir Painel Cliente
        self.btn_cliente = self.findChild(QPushButton, "btn_cliente")
        self.btn_cliente.clicked.connect(lambda: self.cliente.show())
        #Adicionar Cliente
        self.novo_cliente = self.cliente.findChild(QPushButton, "novo_cliente")
        self.cliente.novo_cliente.clicked.connect(lambda: self.abrir_add_cliente.show())
        #Excluir Cliente
        self.excluir_cliente = self.cliente.findChild(QPushButton, "excluir_cliente")
        self.cliente.excluir_cliente.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO CLIENTE"))

        #Abrir Painel Fornecedores
        self.btn_fornecedor = self.findChild(QPushButton, "btn_fornecedor")
        self.btn_fornecedor.clicked.connect(lambda: self.cliente.show())

        
        #Abrir Painel Produtos
        self.btn_produtos = self.findChild(QPushButton, "btn_produtos")
        self.btn_produtos.clicked.connect(lambda: self.produtos.show())
        #Abrir Painel Adicionar Produtos
        self.novo_produto = self.produtos.findChild(QPushButton, "novo_produto")
        self.produtos.novo_produto.clicked.connect(lambda: self.abrir_novo_produto.show())
        #Excluir Produto
        self.excluir_produto = self.produtos.findChild(QPushButton, "excluir_produto")
        self.produtos.excluir_produto.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO PRODUTO"))


        
        


        #Abrir Painel OS
        self.btn_menu_os = self.findChild(QPushButton, "btn_menu_os")
        self.btn_menu_os.clicked.connect(lambda: self.menu_os.show())
        #Abrir Painel Criar OS
        self.btn_add_os = self.menu_os.findChild(QPushButton, "btn_add_os")
        self.menu_os.btn_add_os.clicked.connect(lambda: self.add_os.show())
        #Finalizar OS
        self.btn_finalizar_os = self.menu_os.findChild(QPushButton, "btn_finalizar_os")
        self.menu_os.btn_finalizar_os.clicked.connect(lambda: self.show_QIpuntDialog("FINALIZAR", "DIGITE O CODIGO DA OS"))
        #Excluir OS
        self.btn_excluir_os = self.menu_os.findChild(QPushButton, "btn_excluir_os")
        self.menu_os.btn_excluir_os.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DA OS"))
        #Imprimir OS
        self.btn_imprimir_os = self.menu_os.findChild(QPushButton, "btn_imprimir_os")
        self.menu_os.btn_imprimir_os.clicked.connect(lambda: self.show_QIpuntDialog("IMRPIMIR", "DIGITE O CODIGO DA OS"))

        #Abrir Menu Caixa
        self.btn_caixa = self.findChild(QPushButton, "btn_caixa")
        self.btn_caixa.clicked.connect(lambda: self.menu_caixa.show())



        
        self.show()
    def show_QIpuntDialog(self,title,text):
        user, ok = QInputDialog.getText(self,title, text)
        if ok and user == "":
            self.show_messagebox("Error", "Digite Um Codigo Valido")
            
        elif ok and user != "":
            self.show_messagebox("Concluido", "Concluido Com Sucesso")

       

    def show_messagebox(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle(title)
        msg.setText(str(text))
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exec = msg.exec_()

    
app = QApplication(sys.argv)
w = main()
app.exec_()
