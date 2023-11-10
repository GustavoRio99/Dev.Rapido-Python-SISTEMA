import tkinter as tk
import customtkinter
from tkinter import messagebox
from banco import Conexao

def cadastrar_produto():
   #Função SALVAR
    def salvar_produto():
        #Entrada de dados
        produto = entry_produto.get()
        preco = entry_preco.get()
        #Entrada de dados - FIM
        
        #Tratativas de Erros esperados
        try:
            
            if produto and preco:
                #String de conexao com Banco
                conexao=Conexao()
                conexao=conexao.banco_dados()
                cursor = conexao.cursor()
                #String de conexao com Banco - FIM
                #Comando SALVAR "entrada de dados" no BD
                sql = f"INSERT INTO vendas (produto, preco) VALUES ('{produto}', '{preco}')" 
                cursor.execute(sql)
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Salvo", "Produto cadastrado com salvos!")
                cadastrar_produto.destroy()
                #Comando SALVAR "entrada de dados" no BD - FIM
            else:
                 messagebox.showerror("Erro", "Insira produto e preço para cadastrar.")
                 

        except Exception as e:
            messagebox.showerror("Erro", str(e))
        #Tratativas de Erros esperados - FIM

     #Painel CADASTRAR PRODUTO - Widgets
    def centralizar_Janela(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) //  6
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    cadastrar_produto=customtkinter.CTkToplevel(app2)
    cadastrar_produto.title("Cadastro Produto")

    janela_width = 280
    janela_height = 230
    centralizar_Janela(cadastrar_produto, janela_width, janela_height)

    cadastrar_produto.maxsize(width=janela_width, height=janela_height)
    cadastrar_produto.minsize(width=janela_width, height=janela_height)

    produto_label = customtkinter.CTkLabel(cadastrar_produto, text="Produto")
    produto_label.pack()

    entry_produto = customtkinter.CTkEntry(cadastrar_produto)
    entry_produto.pack()

    preco_label = customtkinter.CTkLabel(cadastrar_produto, text="Preço")
    preco_label.pack()

    entry_preco = customtkinter.CTkEntry(cadastrar_produto, placeholder_text="R$")
    entry_preco.pack()

    botao = customtkinter.CTkButton(cadastrar_produto, text="Cadastrar", command=salvar_produto)
    botao.pack(side="top", pady=40)
    #Painel CADASTRAR PRODUTO - Widgets FIM
    #Funçoes SALVAR - FIM
    
def listar_Produtos():
    #Botao para atualizar a lista de produtos
    def botao_Atualizar():
        listar_App.destroy()
        listar_Produtos()
    #Painel Listar - Widgets
    def centralizar_Janela(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width)// 6
        y = (screen_height - height)// 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    listar_App=customtkinter.CTkToplevel(app2)
    listar_App.title("Produtos Cadastrados")
    janela_width = 300
    janela_height = 420
    centralizar_Janela(listar_App, janela_width, janela_height)

    listar_App.maxsize(width=janela_width, height=janela_height)
    listar_App.minsize(width=janela_width, height=janela_height)

    boxlista = tk.Listbox(listar_App,activestyle="underline",border= 4,borderwidth= 4,
                           bd=10,height=20, width=40)
    boxlista.pack()
    txt_label1 = customtkinter.CTkLabel(listar_App, text="Produtos ativos")
    txt_label1.pack()
    botao_atualizar = customtkinter.CTkButton(listar_App, text="ATUALIZAR", command=botao_Atualizar)
    botao_atualizar.pack(pady=10)
    #Painel Listar - Widgets - FIM
   
    #String de conexao com Banco

    conexao=Conexao()
    conexao=conexao.banco_dados()

    #String de conexao com Banco - FIM
    
    #COMANDO SQL de Busca por ID comparando com variavel de entrada
    cursor = conexao.cursor()
    sql = f"SELECT * FROM vendas"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexao.close()
    #COMANDO SQL de Busca por ID comparando com variavel de entrada - FIM
   
    #Painel LISTAR - Posiciona Curso do insert para primeira posição do boxlist e insere
    #"ID | PRODUTO    "
    boxlista.insert(0,"ID | PRODUTO    ")
    #PAINEL LISTAR - Posiciona - FIM
    
    #Painel LISTAR- Lista produtos abaixo da string ID PRODUTO
    boxlista.delete(1,tk.END)
    #Painel LISTAR- Lista produtos abaixo da string ID PRODUTO - FIM
    
    #Inteiração para listar PRODUTOS
    for result in resultado:
        boxlista.insert(tk.END, f"{result[0]} | {result[1]} - R$ {result[2]}")
    #Inteiração para listar PRODUTOS - FIM
    
    #Painel Listar - Tamanho Janela Widgets- FIM
    
    #Painel Listar - Tamanha Janela Widgets- FIM
def editar_cadastro():
    #Função BUSCAR ID
    def buscar_Produto():
        #Entrada de dados
        id_Produto = entry_id_produto.get()   
        #Entrada de dados - FIM
        
        #Tratativas de Erros esperados
        try:
            if id_Produto:
                #String de conexao com Banco
                conexao=Conexao()
                conexao=conexao.banco_dados()
                #String de conexao com Banco - FIM
                #Comando Procurar por ID comparando com variavel de "entrada de dados"
                cursor = conexao.cursor()
                sql = f"SELECT * FROM vendas WHERE id = '{id_Produto}' "
                cursor.execute(sql)
                resultado = cursor.fetchone()
                conexao.close()
                 #Comando Procurar por ID comparando com variavel de "entrada de dados" - FIM
                if resultado:
                    #String de conexao com Banco
                    conexao=Conexao()
                    conexao=conexao.banco_dados()
                    #String de conexao com Banco - FIM
                    #COMANDO SQL de busca de produto por ID
                    cursor = conexao.cursor()
                    sql = f"SELECT * FROM vendas WHERE id = '{id_Produto}' "
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    conexao.close()
                    #COMANDO SQL de busca de produto por ID - FIM

                    def editar():
                        #Entrada de dados
                        produto=entry_produto.get()
                        preco=entry_preco.get()
                        #Entrada de dados - FIM
                        #Tratativas de Erros esperados
                        try:
                            if produto and preco:
                                #String de conexao com Banco - FIM
                                conexao=Conexao()
                                conexao=conexao.banco_dados()
                                #String de conexao com Banco - FIM
                                #COMANDO SQL de EDIÇÂO de produto por ID
                                cursor = conexao.cursor()
                                sql = f"UPDATE vendas SET produto = '{produto}', preco = '{preco}' WHERE vendas.id = '{id_Produto}'"
                                cursor.execute(sql)
                                conexao.commit()
                                conexao.close()
                                messagebox.showinfo("Edição", "Produto " + produto + " alterado com sucesso!")
                                editar_cadastro2.destroy()
                                
                                #COMANDO SQL de EDIÇÂO de produto por ID - FIM
                            else:
                                messagebox.showerror("Erro", "Nao foi possivel Editar Produto: "+ resultado[1])
                                 

                        except Exception as e:
                            messagebox.showerror("Erro", str(e))
                        #Tratativas de Erros esperados - FIM
                    #Painel EDITAR CADASTRO  Widgets
                    def centralizar_Janela(root, width, height):
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
    
                        x = (screen_width - width) //  6
                        y = (screen_height - height) // 2
    
                        root.geometry(f"{width}x{height}+{x}+{y}")
                    
                    editar_cadastro2=customtkinter.CTkToplevel(app2)
                    editar_cadastro2.title("Editar Cadastro")

                    janela_width = 280
                    janela_height = 230
                    centralizar_Janela(editar_cadastro2, janela_width, janela_height)

                    editar_cadastro2.maxsize(width=janela_width, height=janela_height)
                    editar_cadastro2.minsize(width=janela_width, height=janela_height)

                    txt_label1 = customtkinter.CTkLabel(editar_cadastro2, text="Produto")
                    txt_label1.pack()

                    entry_produto = customtkinter.CTkEntry(editar_cadastro2)
                    entry_produto.pack()

                    txt_label2 = customtkinter.CTkLabel(editar_cadastro2, text="Preço R$")
                    txt_label2.pack()

                    entry_preco = customtkinter.CTkEntry(editar_cadastro2, placeholder_text="R$")
                    entry_preco.pack()

                    botao = customtkinter.CTkButton(editar_cadastro2, text="Editar", command=editar)
                    botao.pack(side="top", pady=40) 
                    entry_produto.insert(0,resultado[1])
                    entry_preco.insert(0,resultado[2])
                    #Painel EDITAR CADASTRO Widgets - FIM

                else:
                    messagebox.showerror("Erro", "ID de produto não encontrado")
            
            else:
                messagebox.showerror("Erro", "ID de produto não inserido")
                
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        #Tratativas de Erros esperados - FIM
    #Painel  Widgets
    def centralizar_Janela(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
    
        x = (screen_width - width) //  2
        y = (screen_height - height) // 15
    
        root.geometry(f"{width}x{height}+{x}+{y}")
    
    editar_cadastro=customtkinter.CTkToplevel(app2)
    editar_cadastro.title("Editar Cadastro")
    janela_width = 280
    janela_height = 150
    centralizar_Janela(editar_cadastro, janela_width, janela_height)
    
    editar_cadastro.maxsize(width=janela_width, height=janela_height)
    editar_cadastro.minsize(width=janela_width, height=janela_height)

    txt1_label=customtkinter.CTkLabel(editar_cadastro, text="Insira ID do Produto")
    txt1_label.pack()
    
    entry_id_produto= customtkinter.CTkEntry(editar_cadastro, placeholder_text="ID")
    entry_id_produto.pack()
    
    botao = customtkinter.CTkButton(editar_cadastro, text="Procurar", command=buscar_Produto)
    botao.pack(side="top", pady=20)
    #Painel  Widgets - FIM
def excluir_Cadastro():

    def buscar_Excluir():
         #Entrada de dados
        id_Produto = entry_id_produto.get()   
         #Entrada de dados - FIM
        #Tratativas de Erros esperados - FIM
        try:
            if id_Produto:
                #String de conexao com Banco
                conexao=Conexao()
                conexao=conexao.banco_dados()
                #String de conexao com Banco - FIM
                #COMANDO SQL de Busca por ID comparando com variavel de entrada
                cursor = conexao.cursor()
                sql = f"SELECT * FROM vendas WHERE id = '{id_Produto}' "
                cursor.execute(sql)
                resultado = cursor.fetchone()
                conexao.close()
                #COMANDO SQL de Busca por ID comparando com variavel de entrada - FIM
                if resultado:
                    #String de conexao com Banco
                    conexao=Conexao()
                    conexao=conexao.banco_dados()
                    #String de conexao com Banco - FIM

                    #COMANDO SQL de Busca por ID comparando com variavel de entrada
                    cursor = conexao.cursor()
                    sql = f"SELECT * FROM vendas WHERE id = '{id_Produto}' "
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    conexao.close()
                    #COMANDO SQL de Busca por ID comparando com variavel de entrada - FIM
                    def excluir():
                        #Entrada de dados 
                        id_Produto = entry_id_produto.get()
                        produto2= entry_produto.get()
                        preco=entry_preco.get()
                        #Entrada de dados - FIM
                        #Tratativa de erros - Exclusao de produto
                        try:
                            if produto2 and preco:
                                #String de conexao com Banco 
                                conexao=Conexao()
                                conexao=conexao.banco_dados()
                                #String de conexao com Banco - FIM
                                #COMANDO SQL Exclusao por ID comparando com a variavel de entrada de dados
                                cursor = conexao.cursor()
                                sql = f"DELETE FROM vendas WHERE vendas.id = '{id_Produto}'"
                                cursor.execute(sql)
                                conexao.commit()
                                conexao.close()
                                messagebox.showinfo("Excluir", "O Produto " + produto2 + " excluido.")
                                
                                excluir_cadastro2.destroy()
                                #COMANDO SQL Exclusao por ID comparando com a variavel de entrada de dados - FIM
                            else:
                                messagebox.showerror("Erro", "Nao foi possivel Excluir Produto: "+ resultado[1]+
                                                     ". Preencha os campos: Produto e Preço para seguir com a EXCLUSAO.")
                                 

                        except Exception as e:
                            messagebox.showerror("Erro", str(e))
                        #Tratativa de erros - Exclusao de produto
                    #Painel EXCLUIR  Widgets
                    def centralizar_Janela(root, width, height):
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
    
                        x = (screen_width - width) //  6
                        y = (screen_height - height) // 2
    
                        root.geometry(f"{width}x{height}+{x}+{y}")

                    excluir_cadastro2=customtkinter.CTkToplevel(app2)
                    excluir_cadastro2.title("Excluir Cadastro")
                    janela_width = 280
                    janela_height = 230
                    centralizar_Janela(excluir_cadastro2, janela_width, janela_height)
                    
                    excluir_cadastro2.maxsize(width=janela_width, height=janela_height)
                    excluir_cadastro2.minsize(width=janela_width, height=janela_height)

                    txt_label1 = customtkinter.CTkLabel(excluir_cadastro2, text="Produto")
                    txt_label1.pack()

                    entry_produto = customtkinter.CTkEntry(excluir_cadastro2)
                    entry_produto.pack()

                    txt_label2 = customtkinter.CTkLabel(excluir_cadastro2, text="Preço R$")
                    txt_label2.pack()

                    entry_preco = customtkinter.CTkEntry(excluir_cadastro2, placeholder_text="R$")
                    entry_preco.pack()
                    botao = customtkinter.CTkButton(excluir_cadastro2, text="EXCLUIR!", command=excluir)
                    botao.pack(side="top", pady=40) 
                    entry_produto.insert(0,resultado[1])
                    entry_preco.insert(0,resultado[2])
                    
                    #Painel EXCLUIR Widgets - FIM

                else:
                    messagebox.showerror("Erro", "ID de produto não encontrado")
            
            else:
                messagebox.showerror("Erro", "ID de produto não inserido")
                
        except Exception as e:
            messagebox.showerror("Erro", str(e))
        #Tratativas de Erros esperados - FIM
    #Painel EXCLUIR CADASTRO  Widgets
    def centralizar_Janela(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()   
        x = (screen_width - width) //  2
        y = (screen_height - height) // 15   
        root.geometry(f"{width}x{height}+{x}+{y}")

    excluir_cadastro=customtkinter.CTkToplevel(app2)
    excluir_cadastro.title("Exclusão de produtos")

    janela_width = 280
    janela_height = 150

    centralizar_Janela(excluir_cadastro, janela_width, janela_height)
    
    excluir_cadastro.minsize(width=janela_width, height=janela_height)
    excluir_cadastro.maxsize(width=janela_width, height=janela_height)

    txt1_label=customtkinter.CTkLabel(excluir_cadastro, text="Insira ID do Produto")
    txt1_label.pack()
    entry_id_produto= customtkinter.CTkEntry(excluir_cadastro, placeholder_text="ID")
    entry_id_produto.pack()
    
    botao = customtkinter.CTkButton(excluir_cadastro, text="Procurar", command=buscar_Excluir)
    botao.pack(side="top", pady=20)
    #Painel EXCLUIR CADASTRO   Widgets - FIM

def cadasdro_usuario():
    def salvar():
        #Variaveis de entrada de dados
        login = entry_login.get()
        senha = entry_senha.get()
        #Variaveis de entrada de dados - FIM
        #Tratativas de Erros esperados
        try:
            
            if login and senha:
                #String de conexao com Banco 
                conexao=Conexao()
                conexao=conexao.banco_dados()
                #String de conexao com Banco - FIM
                #COMANDO SQL Inserção apartir de variaveis de Entrada CADASTRO
                cursor = conexao.cursor()
                sql = f"INSERT INTO login (login, senha) VALUES ('{login}', '{senha}')" 
                cursor.execute(sql)
                conexao.commit()
                conexao.close()
                messagebox.showinfo("Salvo", "Login e Senha salvos!")
                toplogin.destroy()
                #COMANDO SQL Inserção apartir de variaveis de Entrada CADASTRO
            else:
                 messagebox.showerror("Erro", "Nao foi possivel salvar login e senha.")
                 toplogin.destroy() 

        except Exception as e:
            messagebox.showerror("Erro", str(e))
        #Tratativas de Erros esperados - FIM
    #Painel Cadastro USUARIO  Widgets 
    def centralizar_Janela(root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()   
        x = (screen_width - width) //  6
        y = (screen_height - height) // 2  
        root.geometry(f"{width}x{height}+{x}+{y}")
    
    toplogin = customtkinter.CTkToplevel(app2)
    toplogin.title("cadastro")

    janela_width = 250
    janela_height = 300
    centralizar_Janela(toplogin, janela_width, janela_height)

    toplogin.minsize(width=janela_width, height=janela_height)
    toplogin.maxsize(width=janela_width, height=janela_height)

    txt0 = customtkinter.CTkLabel(toplogin, text="Dados Cadastro Usuario")
    txt0.pack(side="top", pady=10)


    txt_login = customtkinter.CTkLabel(toplogin, text="Login:")
    txt_login.pack(padx=10)

    entry_login = customtkinter.CTkEntry(toplogin)
    entry_login.pack()


    txt_senha = customtkinter.CTkLabel(toplogin, text="Senha:")
    txt_senha.pack()

    entry_senha = customtkinter.CTkEntry(toplogin, show="*")
    entry_senha.pack(padx=10)


    botao = customtkinter.CTkButton(toplogin, text="Salvar",command=salvar)
    botao.pack(side="top", pady=40)
    #Painel Cadastro USUARIO  Widgets - FIM

 #Painel - MENU PRINCIAL Widgets   
#Painel MENU PRINCIPAL  Widgets - MENU
def centralizar_Janela(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    root.geometry(f"{width}x{height}+{x}+{y}")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

app2 = customtkinter.CTk()
app2.title("Sistema de Cadastro")

janela_width = 280
janela_height = 300
centralizar_Janela(app2, janela_width, janela_height)
app2.minsize(width=janela_width, height=janela_height)
app2.maxsize(width=janela_width, height=janela_height)
texto = customtkinter.CTkLabel(app2, text="MENU")
texto.pack(padx=10, pady=10)

opc1 = customtkinter.CTkButton(app2, text="Cadastrar Produto", command=cadastrar_produto)
opc1.pack()

opc2 = customtkinter.CTkButton(app2, text="Listar Produtos", command=listar_Produtos)
opc2.pack(padx=10,pady=10)

opc3 = customtkinter.CTkButton(app2, text="Editar Cadastro", command=editar_cadastro)
opc3.pack()

opc4 = customtkinter.CTkButton(app2, text="Excluir Cadastro", command= excluir_Cadastro)
opc4.pack(pady=10)

opcusuario = customtkinter.CTkButton(app2, text="Cadastro Usuario", command=cadasdro_usuario )
opcusuario.pack(pady=20 )
#Painel MENU PRINCIPAL  Widgets CMENU - FIM

app2.mainloop()