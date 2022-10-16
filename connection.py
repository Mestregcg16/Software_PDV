import mysql.connector
from mysql.connector import Error





class Data_base:
    def __init__(self, name='jc_vidros') -> None:
        self.name = name
        self.con = mysql.connector.connect(host="localhost", database="jc_vidros", user="root", password="")
        if self.con.is_connected():
            db_info = self.con.get_server_info()
            print("conectado ao servidor msql versao", db_info)
            
    def insert_cliente(self, nm , desc, tel1, tel2, tel3, end, brr, cmpl, cep ,cidade, email, data):
        c = self.con.cursor(buffered=True)
        c.execute(f"""insert into clientes (nome, descricao, tel1,tel2,tel3,endereco,bairro,complemento,cep,cidade,email,data)
values
('{nm}', '{desc}', '{tel1}', '{tel2}', '{tel3}', '{end}', '{brr}', '{cmpl}', '{cep}','{cidade}','{email}', '{data}')""")
        
        self.con.commit()

   
   
   
   
   
    def select_all(self, table):
        c = self.con.cursor()
        c.execute(f"select * from '{table}'")
        result = c.fetchall()
        return result

    def excluir(self, table, codigo):
        try:
            c = self.con.cursor(buffered=True)
            sql = (f"DELETE from '{table}' WHERE codigo = %s")
            c.execute(sql, [codigo])
            self.con.commit()
        except Error as error:
            print(error)