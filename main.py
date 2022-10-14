from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
#import Main_Icons.images as images
import btn_icons as buttons
from os import *


class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        #tela Principal 
        uic.loadUi("ui_files\main.ui", self)
        self.show()


        ############################### CLIENTES ###############################
        #Telas
        cliente = uic.loadUi("ui_files\cliente .ui")
        add_cliente = uic.loadUi("ui_files/add_cliente.ui")
        #Botoes
        btn_cliente = self.findChild(QPushButton, "btn_cliente")
        novo_cliente = cliente.findChild(QPushButton, "novo_cliente")
        #salvar_cliente = add_cliente.findChild(QPushButton, "salvar_cliente")
        excluir_cliente = cliente.findChild(QPushButton, "excluir_cliente")
        #Conexão
        btn_cliente.clicked.connect(lambda: cliente.show())                                                      #Abrir Painel Cliente
        novo_cliente.clicked.connect(lambda: add_cliente.show())                                                 #Abrir Tela Adicionar Cliente
        excluir_cliente.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO CLIENTE")) #Excluir Cliente
        #add_cliente.salvar_cliente.clicked.connect(self.teste)                                                  #Adicionar Cliente
        
        
        
        ############################### FORNECEDORES ###############################
        #Botões
        btn_fornecedor = self.findChild(QPushButton, "btn_fornecedor")
        #Conexão
        btn_fornecedor.clicked.connect(lambda: cliente.show())                                                   #Abrir Painel Fornecedores

        
        
        
        
        ############################### PRODUTOS ###############################
        #Telas
        produtos = uic.loadUi("ui_files\produtos.ui")
        novo_produto = uic.loadUi("ui_files/add_produto.ui")
        #Botoões
        btn_produtos = self.findChild(QPushButton, "btn_produtos")
        novo_produto = produtos.findChild(QPushButton, "novo_produto")
        excluir_produto = produtos.findChild(QPushButton, "excluir_produto")
        #Conexão
        btn_produtos.clicked.connect(lambda: produtos.show())                                                       #Abrir Painel Produtos
        novo_produto.clicked.connect(lambda: novo_produto.show())                                                   #Abrir Painel Adicionar Produtos
        excluir_produto.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO PRODUTO"))    #Excluir Produto

       
        
        ############################### OS ###############################
        #Telas
        menu_os = uic.loadUi("ui_files\menu_os.ui")
        add_os = uic.loadUi("ui_files/add_os.ui")
        #Botões
        btn_menu_os = self.findChild(QPushButton, "btn_menu_os")
        btn_add_os = menu_os.findChild(QPushButton, "btn_add_os")
        btn_finalizar_os = menu_os.findChild(QPushButton, "btn_finalizar_os")
        btn_excluir_os = menu_os.findChild(QPushButton, "btn_excluir_os")
        btn_imprimir_os = menu_os.findChild(QPushButton, "btn_imprimir_os")
        #Conexão
        btn_menu_os.clicked.connect(lambda: menu_os.show())                                                     #Abrir Painel OS
        btn_add_os.clicked.connect(lambda: add_os.show())                                                       #Abrir Painel Criar OS
        btn_finalizar_os.clicked.connect(lambda: self.show_QIpuntDialog("FINALIZAR", "DIGITE O CODIGO DA OS"))  #Finalizar OS
        btn_excluir_os.clicked.connect(lambda: self.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DA OS"))      #Excluir OS
        btn_imprimir_os.clicked.connect(lambda: self.show_QIpuntDialog("IMRPIMIR", "DIGITE O CODIGO DA OS"))    #Imprimir OS
        
        ############################### CAIXA ###############################
        #Telas
        caixa = uic.loadUi("ui_files\caixa.ui")
        #Botões
        btn_caixa = self.findChild(QPushButton, "btn_caixa")
        #Conexão
        btn_caixa.clicked.connect(lambda: caixa.show()) #AbrirCaixa

        
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
w = Main()
app.exec_()
