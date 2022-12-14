from PyQt5 import uic
from PyQt5.QtWidgets import *
import sys
import functions as f
import main_icons.images as images


class Main(QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        uic.loadUi("ui_files\main.ui", self)
        self.show()


        ############################### CLIENTES ###############################
        #Telas
        cliente = uic.loadUi("ui_files\cliente .ui")
        add_cliente = uic.loadUi("ui_files/add_cliente.ui")
        #Botoes
        btn_cliente = self.findChild(QPushButton, "btn_cliente")
        novo_cliente = cliente.findChild(QPushButton, "novo_cliente")
        salvar_cliente = add_cliente.findChild(QPushButton, "salvar_cliente")
        excluir_cliente = cliente.findChild(QPushButton, "excluir_cliente")
        #Conexão
        btn_cliente.clicked.connect(lambda: cliente.show())                                                      #Abrir Painel Cliente
        novo_cliente.clicked.connect(lambda: add_cliente.show())                                                 #Abrir Tela Adicionar Cliente
        excluir_cliente.clicked.connect(lambda: f.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO CLIENTE")) #Excluir Cliente
        add_cliente.salvar_cliente.clicked.connect(f.cadastro_cliente)                                                  #Adicionar Cliente
        
        
        
        ############################### FORNECEDORES ###############################
        #Botões
        #btn_fornecedor = self.findChild(QPushButton, "btn_fornecedor")
        #Conexão
        #btn_fornecedor.clicked.connect(lambda: cliente.show())                                                   #Abrir Painel Fornecedores


        
        
        
        ############################### USUARIOS ###############################
        #Telas
        usuario = uic.loadUi("ui_files/usuario.ui")
        add_usuario = uic.loadUi("ui_files/add_usuario.ui")
        #Botões
        btn_usuario = self.findChild(QPushButton, "btn_usuarios")
        novo_usuario = usuario.findChild(QPushButton, "novo_usuario")
        editar_usuario = usuario.findChild(QPushButton, "editar_usuario")
        excluir_usuario = usuario.findChild(QPushButton, "excluir_usuario")
        att_usuario = usuario.findChild(QPushButton, "att_usuario")
        #Conexões
        btn_usuario.clicked.connect(lambda: usuario.show())
        usuario.novo_usuario.clicked.connect(lambda: add_usuario.show())
        usuario.excluir_usuario.clicked.connect(lambda: f.show_QIpuntDialog("EXCLUIR", "DIGITE O NOME DO USUARIO"))

        


        
        
        
        
        ############################### PRODUTOS ###############################
        #Telas
        produtos = uic.loadUi("ui_files\produtos.ui")
        novo_produto = uic.loadUi("ui_files/add_produto.ui")
        #Botoões
        btn_produtos = self.findChild(QPushButton, "btn_produtos")
        btn_novo_produto = produtos.findChild(QPushButton, "novo_produto")
        excluir_produto = produtos.findChild(QPushButton, "excluir_produto")
        #Conexão
        btn_produtos.clicked.connect(lambda: produtos.show())                                                       #Abrir Painel Produtos
        btn_novo_produto.clicked.connect(lambda: novo_produto.show())                                                   #Abrir Painel Adicionar Produtos
        excluir_produto.clicked.connect(lambda: f.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DO PRODUTO"))    #Excluir Produto

       
        
        ############################### OS ###############################
        #Telas
        menu_os = uic.loadUi("ui_files\menu_os.ui")
        add_os = uic.loadUi("ui_files/add_os.ui")
        incluir_produto = uic.loadUi("ui_files\incluir_produto.ui")
        #Botões
        btn_menu_os = self.findChild(QPushButton, "btn_menu_os")
        btn_add_os = menu_os.findChild(QPushButton, "btn_add_os")
        btn_finalizar_os = menu_os.findChild(QPushButton, "btn_finalizar_os")
        btn_excluir_os = menu_os.findChild(QPushButton, "btn_excluir_os")
        btn_imprimir_os = menu_os.findChild(QPushButton, "btn_imprimir_os")
        btn_incluir_produto = add_os.findChild(QPushButton, "incluir_produto")
        #Conexão
        btn_menu_os.clicked.connect(lambda: menu_os.show())                                                     #Abrir Painel OS
        btn_add_os.clicked.connect(lambda: add_os.show())                                                       #Abrir Painel Criar OS
        btn_finalizar_os.clicked.connect(lambda: f.show_QIpuntDialog("FINALIZAR", "DIGITE O CODIGO DA OS"))  #Finalizar OS
        btn_excluir_os.clicked.connect(lambda: f.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DA OS"))      #Excluir OS
        btn_imprimir_os.clicked.connect(lambda: f.show_QIpuntDialog("IMRPIMIR", "DIGITE O CODIGO DA OS"))    #Imprimir OS
        btn_incluir_produto.clicked.connect(lambda: incluir_produto.show())
        
        ############################### CAIXA ###############################
        #Telas
        caixa = uic.loadUi("ui_files\caixa.ui")
        add_caixa = uic.loadUi("ui_files/add_caixa.ui")
        #Botões
        btn_caixa = self.findChild(QPushButton, "btn_caixa")
        btn_add_caixa = caixa.findChild(QPushButton, "incluir_caixa")
        #Conexão
        btn_caixa.clicked.connect(lambda: caixa.show()) #AbrirCaixa
        btn_add_caixa.clicked.connect(lambda: add_caixa.show())# Abrir Tela add_Caixa


        ############################### AGENDA ###############################
        #Telas
        agenda = uic.loadUi("ui_files/agenda.ui")
        add_agenda = uic.loadUi("ui_files/add_agenda.ui")
        #Botões
        btn_agenda = self.findChild(QPushButton, "btn_agenda")
        novo_horario = agenda.findChild(QPushButton, "novo_horario")
        excluir_horario = agenda.findChild(QPushButton, "excluir_horario")
        #Conexão
        btn_agenda.clicked.connect(lambda: agenda.show())
        novo_horario.clicked.connect(lambda: add_agenda.show())
        excluir_horario.clicked.connect(lambda: f.show_QIpuntDialog("EXCLUIR", "DIGITE O CODIGO DA AGENDA"))



        
    
    
    
    
    
    
    
    
    
    

       

    

    
app = QApplication(sys.argv)
w = Main()
app.exec_()
