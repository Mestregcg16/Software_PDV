from fpdf import FPDF
nome = "JC VIDROS"
endereço = "Rua Visconde De Itauna"
telefone = "21 96968-4788"
email=  "gfazzi1904@gmail.com"
cliente = "Diego"
endereço_cliente = "Rua Rosalina Maria Barbosa"
cidade_cliente = "São Gonçalo"
tel_cliente = "21 994318900"

dados = ("0020", "PORTA PIVOTANTE", "1", "210", "80", "R$ 800,00")





def imprimir_os():
    pdf = FPDF('P', 'mm', 'Letter')
    pdf.add_page()#Cria O PDF
    pdf.set_text_color(0,0,0)# Define a cor da Fonte

    #Cabeçalho
    pdf.set_font('times','B',24)
    pdf.cell(200,10,nome, border=False, align='L' ) 
    pdf.set_font('times','B',18)
    pdf.text(150,15,'ORÇAMENTO')
    pdf.set_font('times','', 12)
    pdf.text(10,30, endereço)
    pdf.text(10,35, telefone)
    pdf.text(150, 30,email)
    pdf.line(10,40,200,40)


    #Cliente
    pdf.text(10,45,f"Cliente: {cliente}")
    pdf.line(10,49,200,49)
    pdf.text(10,53,f"Endereço: {endereço_cliente}")
    pdf.line(10,57,200,57)
    pdf.text(10,61,f"Cidade:{cidade_cliente}")
    pdf.line(10,65,200,65)
    pdf.text(10,69,f"Tel:{tel_cliente}")
    pdf.line(10,73,200,73)

    #Produtos
    pdf.set_xy(10,75)
    pdf.cell(20,8,"Codigo",border=True)
    pdf.set_xy(30,75)
    pdf.cell(70,8,"Nome", border=True)
    pdf.set_xy(100,75)
    pdf.cell(10,8,"QT", border=True)
    pdf.set_xy(110,75)
    pdf.cell(20,8,"Altura", border=True)
    pdf.set_xy(130,75)
    pdf.cell(20,8,"Largura", border=True)
    pdf.set_xy(150,75)
    pdf.cell(20,8,"Valor Un", border=True)
    pdf.set_xy(170,75)
    pdf.cell(15,8,"Desc", border=True)
    pdf.set_xy(185,75)
    pdf.cell(15,8,"Preço", border=True)

    for i in dados:
        pdf.set_xy(10,83)
        pdf.cell(20,8,dados[0],border=True)
        pdf.set_xy(30,83)
        pdf.cell(70,8,dados[1], border=True)
        pdf.set_xy(100,83)
        pdf.cell(10,8,dados[2], border=True)
        pdf.set_xy(110,83)
        pdf.cell(20,8,dados[2], border=True)
        pdf.set_xy(130,83)
        pdf.cell(20,8,dados[3], border=True)
        pdf.set_xy(150,83)
        pdf.cell(20,8,dados[4], border=True)
        #pdf.set_xy(170,75)
        #pdf.cell(15,8,dados[5], border=True)
        #pdf.set_xy(185,75)
        #pdf.cell(15,8,dados[6], border=True)




    print("PDF CRIADO")
    pdf.output('PDF.pdf')# Nome do arquivo a ser salvo