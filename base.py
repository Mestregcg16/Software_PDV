
from login import Ui_Login

from mysql.connector import Error

from datetime import datetime

from connection import Data_base

db = Data_base()

tempo = datetime.now()
data = tempo.strftime("%x")
hora = tempo.strftime("%X")
resumed = data + " " + hora



    

def check_user(self):
user = self.user.text()
senha = self.senha.text()
result = db.select_user(user)

for i in result:
    if i[0].upper() == user.upper() and i[1].upper() == senha.upper() and i[2] == "Administrador":
        return "Admin"
    elif i[0].upper() == user.upper() and i[1].upper() == senha.upper() and i[2] == "Usuario":
        return "User"
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Usuario Nao Cadastrado")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def checkLogin(self):
    autenticacao = self.check_user()
    if autenticacao == "Admin" or autenticacao == "User":
        self.w = MainWindow(autenticacao)
        self.w.show()
        self.close()
    else:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Error")
        msg.setText("Usuario Nao Cadastrado")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()



#########################################   USUARIOS   ####################################################

def cadastro_usuario(self):
    nome = self.lineEdit_6.text()
    email = self.lineEdit_8.text()
    user = self.lineEdit_5.text()
    senha = self.lineEdit_4.text()
    perfil = self.combo_perfil_user_2.currentText()

    try:
        db.insert_user(nome, email, user, senha, perfil)
        self.show_messagebox("Sucesso", "Usuario Cadastrado Com Sucesso")

    except Error as error:
        print(error)
        self.show_messagebox("Error", "Erro Ao Cadastrar Usuario")

def excluir_usuario(self):
    user, okPressed = QtWidgets.QInputDialog.getText(self, "Excluir Usuario", "Digite o Nome Do Usuario")
    c = db.select_one_user(user)
    if c == []:
        self.show_messagebox("Error", "Usuario Nao Existe")
    else:
        db.excluir_user(user)
        self.show_messagebox("Usuario Apagado", "Usuario Apagado Com Sucesso")

def limpar_usuario(self):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle("Confirmar Acao")
    msg.setText("ESTA ACAO EXCLUIRA TODOS OS USUARIOS,"
                "DESEJA CONFIRMAR ACAO??")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    exec = msg.exec_()

    if exec == QtWidgets.QMessageBox.Ok:

        try:
            db.drop_user()
            db.create_user()
        except Error as error:
            self.show_messagebox("Error", error)

        finally:
            self.show_messagebox("Concluido", "Usuarios Apagados com Sucesso")
    else:
        print("Acao Cancelada")

#########################################   CLIENTES  #####################################################

def cadastro_cliente(self):
        # cod = self.box_cliente.value()
        nome = self.line_cliente.text()
        orcamento = self.line_orcamento.text()
        bairro = self.line_bairro.text()
        cidade = self.line_cidade.text()
        endereco = self.line_endereco.text()
        estado = self.line_estado.text()
        # projeto = self.combo_projeto.text()
        telefone = self.line_telefone.text()
        celular = self.line_celular.text()

        try:
            db.insert_cliente(nome, orcamento, bairro, cidade, endereco, estado, telefone, celular, resumed)
            self.mostrar_clientes()
        except Error as error:
            print(f"Erro ao inserir Cliente:{error}")
            self.show_messagebox("Error", "Erro Ao Cadastrar Cliente")
        finally:
            self.show_messagebox("Cliente Cadastrado", "Cliente Cadastrado Com Sucesso")

def exibir_cliente(self):
    cliente = self.filter_cliente.text()
    rows = db.read_one_cliente(cliente)
    self.tabela_cliente.clearContents()
    for i in range(len(rows)): #linha
        for j in range(len(rows[0])): #coluna
            item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
            self.tabela_cliente.setItem(i,j, item)
            
def mostrar_clientes(self):
    clientes = db.select_cliente()
    self.tabela_cliente.clearContents()
    self.tabela_cliente.setRowCount(len(clientes))

    for row, text in enumerate(clientes):
        for column, data in enumerate(text):
            self.tabela_cliente.setItem(
                row, column, QTableWidgetItem(str(data)))
    
def limpar_clientes(self):
    
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setWindowTitle("Confirmar Acao")
    msg.setText("ESTA ACAO EXCLUIRA TODOS OS ITENS DA TABELA,"
                "DESEJA CONFIRMAR ACAO??")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    exec = msg.exec_()
    if exec == QtWidgets.QMessageBox.Ok:
        try:
            db.drop_clientes()
            db.create_clientes()
            self.mostrar_clientes()
        except Error as error:
            self.show_messagebox("Error", error)
        finally:
            self.show_messagebox("Clientes Apagados", "Clientes Apagados Com Sucesso")
    else:
        print("Acao Cancelada")

def excluir_cliente(self):

    cliente, okPressed = QtWidgets.QInputDialog.getText(self, "Excluir Cliente", "Digite o Nome Do Cliente")
    c = db.read_one_cliente(cliente)
    if c == []:
        self.show_messagebox("Error", "Cliente Nao Existe")
    else:
        db.excluir_cliente(cliente)
        self.show_messagebox("Cliente Apagado", "Cliente Apagado Com Sucesso")
        self.mostrar_clientes()

def cancelar_cliente(self):
    self.box_cliente.clear()
    self.line_cliente.clear()
    self.line_bairro.clear()
    self.line_cidade.clear()
    self.line_celular.clear()
    self.line_telefone.clear()
    self.line_estado.clear()
    self.line_endereco.clear()
    self.line_orcamento.clear()

#########################################   PRODUTOS     ##################################################

def cadastro_produto(self):

        cod = self.box_codigo_produto.value()
        produto = self.line_produto.text()
        desc = self.line_descricao.text()
        alt = self.box_altura_produto.value()
        lar = self.box_largura_produto.value()
        com = self.box_comprimento_produto.value()
        val = self.box_valor_produto.value()
        try:
            db.insert_produto(cod, produto, desc, alt, lar, val, com)
            self.show_messagebox("Concluido", "Produto Cadastrado Com Sucesso")
            self.mostrar_produtos()
        except Error as error:
            self.show_messagebox("Erro", error)

def mostrar_produtos(self):
    produtos = db.select_all_produto()

    self.tabela_prodtuos.clearContents()
    self.tabela_prodtuos.setRowCount(len(produtos))

    for row, text in enumerate(produtos):
        for column, data in enumerate(text):
            self.tabela_prodtuos.setItem(
                row, column, QTableWidgetItem(str(data)))

def select_produto(self):
    cod = self.box_produto.value()
    produto = db.select_one_produto(cod)
    if produto == None:
        produto = ["PRODUTO INDEFINIDO"]
        for i in produto:
            self.combo_produto.clear()
            self.combo_produto.addItem(produto[0])
    #print(f"resultado da funcao:{produto}")
        
    else:
        for i in produto:
            #i = "".join(str(i))
            self.combo_produto.clear()
            self.combo_produto.addItem(i[0])
        
        
def excluir_produtos(self):
    produto, okPressed = QtWidgets.QInputDialog.getText(self, "Excluir Produto", "Digite o Codigo Do Produto")
    c = db.select_one_produto(produto)
    if c == []:
        self.show_messagebox("Error", "Produto Nao Existe")
    else:
        db.excluir_produto(produto)
        self.show_messagebox("Produto Apagado", "Produto Apagado Com Sucesso")
        self.mostrar_produtos()

def limpar_produtos(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Confirmar Acao")
        msg.setText("ESTA ACAO EXCLUIRA TODOS OS ITENS DA TABELA,"
                    "DESEJA CONFIRMAR ACAO??")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        exec = msg.exec_()

        if exec == QtWidgets.QMessageBox.Ok:
            try:
                db.drop_produto()
                db.create_produto()
                self.show_messagebox("Concluido", "Produtos Apagados Com Sucesso")
                self.mostrar_produtos()
            except Error as error:
                self.show_messagebox("Error", error)
        else:
            print("Acao Cancelada")

def exibir_produto(self):
    produto = self.filter_produto.text()
    rows = db.read_one_produto(produto)
    self.tabela_prodtuos.clearContents()
    for i in range(len(rows)): #linha
        for j in range(len(rows[0])): #coluna
            item = QtWidgets.QTableWidgetItem(f"{rows[i][j]}")
            self.tabela_prodtuos.setItem(i,j, item)

#########################################   OUTROS     #########################################

def imageUpdate(self):
    imagePath = "C:/Users/Master/Desktop/Software-PDV/resized"
    currentItem = str(self.combo_modelo.currentText())
    currentImage = '%s/%s.png' % (imagePath, currentItem)
    self.img_projeto.setPixmap(QtGui.QPixmap(currentImage))

def path_arquivos(self):
    for _, _, arquivo in os.walk('C:/Users/Master/Desktop/Software-PDV/resized'):
        for i in arquivo:
            final = i[:-4]
            lista = [final]
            self.combo_modelo.addItems(lista)

def openFile(self):
    directory = QtWidgets.QFileDialog.getExistingDirectory()
    for _, _, arquivo in os.walk(directory):
        for items in arquivo:
            final = items[:-4]
            lista = [final]
            print(lista)
            self.combo_modelo.addItems(lista)

def select_itens(self):
    codigo = self.box_produto.value()
    produto = self.combo_produto.currentText()
    qt = self.box_quantidade.value()
    alt = self.box_altura.value()
    lar = self.box_largura.value()
    lucro = self.box_lucro.value()
    desconto = self.box_desconto.value()

    valor_un = db.select_valor(codigo)
    
    
    if valor_un == None:
        valor_un = [0]
        self.line_valor_bruto.setText("0")

    valor = "".join(str(valor_un[0]))
    if qt != 0:
        bruto = float(valor) * alt * lar * qt
    else:
        bruto = float(valor) * alt * lar


    total = bruto + float(bruto * lucro/100)

    if desconto != 0.0:
        total = total - (total * desconto/100)

    
    lucro = total - bruto 

    
    self.line_Valor_unit.setText(str(valor_un[0]))
    self.line_valor_bruto.setText(str("{:.2f}".format(bruto)))
    self.line_lucro.setText(str("{:.2f}".format(lucro)))
    self.line_total.setText(str("{:.2f}".format(total)))
    self.selecao = self.tabela_selecao_itens

    lista = [codigo, produto, qt, alt, lar, valor_un[0]]
    l = self.tabela_selecao_itens.rowCount()

    for column, text in enumerate(lista):
        self.tabela_selecao_itens.setItem(l -1 , column, QTableWidgetItem(str(text)))
    
    l = self.tabela_selecao_itens.insertRow(l)
    
    self.cancelar_orcamento()

def read_itens(self):
    i = []
    row = self.tabela_selecao_itens.rowCount()
    column = self.tabela_selecao_itens.columnCount()
    for row in range(row):
            for column in range(column):
            item = self.tabela_selecao_itens.item(row, column)
            if item and item.text():
                
                i.append([item.text()])

    lista = i[:6] + [i]
    
    #print(i)
    print(lista[6]) 


def cancelar_orcamento(self):
    self.box_produto.setValue(0)
    self.combo_produto.clear()
    self.box_quantidade.setValue(0)
    self.box_altura.setValue(0.00)
    self.box_largura.setValue(0.00)
    self.box_lucro.setValue(0.00)
    self.box_desconto.setValue(0.00)
    self.line_Valor_unit.clear()
    
def cancelar_produto(self):
    self.Produtos.QLineEdit.clear()
    self.box_codigo_produto.clear()
    self.line_produto.clear()
    self.line_descricao.clear()
    self.box_altura_produto.clear()
    self.box_largura_produto.clear()
    self.box_comprimento_produto.clear()

def atalho(self, p, f):
    QShortcut("Return" , p).activated.connect(f)    

def remove_selecao(self):
    #self.tabela_selecao_itens.clear()
    self.tabela_selecao_itens.clearContents()
    self.tabela_selecao_itens.setRowCount(1)
