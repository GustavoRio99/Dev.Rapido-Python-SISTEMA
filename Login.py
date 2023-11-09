import tkinter as tk
import customtkinter
from tkinter import messagebox
import subprocess
from banco import Conexao

def carregar_login():
    #Tratativa de Erros esperados - Função carregar_login()
    try:
        #Abertura de arquivo texto - Lembrar Login e senha
        with open("login_info.txt", "r") as arquivo_login:
            conteudo = arquivo_login.read()
            login.insert(0,conteudo)
            arquivo_login.close()
        with open("senha_info.txt", "r") as arquivo_senha:
            conteudo = arquivo_senha.read()
            senha.insert(0,conteudo)
            arquivo_senha.close()
        #Abertura de arquivo texto - Lembrar Login e senha - FIM
        if not conteudo:
            messagebox.showerror("Erro","Nao foram encontrados login e senha salvos") 
    except Exception as b:
        messagebox.showerror("Erro", str(b))
    #Tratativa de Erros esperados - Função carregar_login() - FIM
def clique():
    #Variaveis de entrada de dados
    usuario = login.get()
    password = senha.get()
    lembrar= checkbox.get()
    #Variaveis de entrada de dados - FIM
    if lembrar:
        #Grava as Variaveis de entrada dados em arquivo - Operação arquivo
        with open("login_info.txt", "w") as arquivo_login:
                arquivo_login.write(usuario)
                arquivo_login.close()
        with open("senha_info.txt", "w") as arquivo_senha:
                arquivo_senha.write(password)
                arquivo_senha.close()
       #Grava as Variaveis de entrada dados em arquivo - Operação arquivo - FIM         
    try:
        #String de conexao com Banco
        conexao=Conexao()
        conexao=conexao.banco_dados()
        #String de conexao com Banco - FIM
        #COMANDO SQL seleciona Login e Senha pelas Variaveis de entrada de dados.
        cursor = conexao.cursor()
        sql = "SELECT * FROM login WHERE login = %s AND senha = %s"
        cursor.execute(sql, (usuario, password))
        resultado = cursor.fetchone()
        conexao.close()
        #COMANDO SQL seleciona Login e Senha pelas Variaveis de entrada de dados.
        
        if resultado:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            app.destroy()
            #Abre o programa princial
            subprocess.Popen(["py", "C:/Users/Gustavo Rio/Documents/Programas/ProjetoFacul/indexsistema.py"])
            #Abre o programa princial - FIM
            
        else:
            messagebox.showerror("Login", "Login ou senha invalidos!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))
    #Tratativa de Erros esperados - FIM


#Painel  Widgets Login
def centralizar_Janela(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    root.geometry(f"{width}x{height}+{x}+{y}")

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("Login")

janela_width = 250
janela_height = 300
centralizar_Janela(app, janela_width, janela_height)

texto = customtkinter.CTkLabel(app, text="Fazer Login")
texto.pack(padx=10, pady=10)

login = customtkinter.CTkEntry(app, placeholder_text="Login")
login.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(app, placeholder_text="Senha", show="*")
senha.pack(padx=10, pady=10)

checkbox= customtkinter.CTkCheckBox(app, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(app, text="Fazer Login", command=clique)
botao.pack(padx=10, pady=10)

botao2 = tk.Label(app, text="carregar ultimo login", fg="blue")
botao2.pack()
botao2.bind("<Button-1>", lambda e: carregar_login())
#Painel  Widgets Login - FIM

app.mainloop()