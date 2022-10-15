from fpdf import FPDF
nome = "Vidraçaria JC VIDROS"
endereço = "Rua Visconde De Itauna"
cnpj = "000000000/0000"
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
    pdf.set_font('times','',24)
    pdf.cell(200,10,nome, border=False, align='C')
    
    pdf.set_font('times','',18)
    pdf.cell(200,10,'ORÇAMENTO',border=False, align='C')
    pdf.set_font('times','', 14)
    pdf.ln(6)
    pdf.cell(200,20,cnpj,border=False, align='C' )
    pdf.ln(6)
    pdf.cell(200,20,endereço,border=False, align='C' )
    pdf.ln(6)
    pdf.cell(200,20,telefone,border=False, align='C' )
    pdf.ln(6)
    pdf.cell(200,20,email,border=False, align='C' )

    pdf.line(10,50,200,50)
   


    #Cliente
    pdf.text(10,55,f"Cliente: {cliente}")
    pdf.line(10,59,200,59)
    pdf.text(10,63,f"Endereço: {endereço_cliente}")
    pdf.line(10,67,200,67)
    pdf.text(10,71,f"Cidade:{cidade_cliente}")
    pdf.line(10,75,200,75)
    pdf.text(10,79,f"Tel:{tel_cliente}")
    pdf.line(10,83,200,83)

    #Produtos
    pdf.set_xy(10,90)
    pdf.cell(20,8,"Codigo",border=True)
    pdf.set_xy(30,90)
    pdf.cell(70,8,"Nome", border=True)
    pdf.set_xy(100,90)
    pdf.cell(10,8,"QT", border=True)
    pdf.set_xy(110,90)
    pdf.cell(20,8,"Altura", border=True)
    pdf.set_xy(130,90)
    pdf.cell(20,8,"Largura", border=True)
    pdf.set_xy(150,90)
    pdf.cell(20,8,"Valor Un", border=True)
    pdf.set_xy(170,90)
    pdf.cell(15,8,"Desc", border=True)
    pdf.set_xy(185,90)
    pdf.cell(15,8,"Preço", border=True)

    for i in dados:
        pdf.set_font('Times','', 10)
        pdf.set_xy(10,98)
        pdf.cell(20,8,dados[0],border=True)
        pdf.set_xy(30,98)
        pdf.cell(70,8,dados[1], border=True)
        pdf.set_xy(100,98)
        pdf.cell(10,8,dados[2], border=True)
        pdf.set_xy(110,98)
        pdf.cell(20,8,dados[2], border=True)
        pdf.set_xy(130,98)
        pdf.cell(20,8,dados[3], border=True)
        pdf.set_xy(150,98)
        pdf.cell(20,8,dados[4], border=True)
        #pdf.set_xy(170,75)
        #pdf.cell(15,8,dados[5], border=True)
        #pdf.set_xy(185,75)
        #pdf.cell(15,8,dados[6], border=True)




    print("PDF CRIADO")
    pdf.output('PDF.pdf')# Nome do arquivo a ser salvo

imprimir_os()