# Dev.Rapido-Python-SISTEMA
Trabalho academico desenvolvido em python.  Sistema basico intuitivo.

          
		UNESA - Universidade Estacio de Sa

Gustavo de Oliveira Rio
Ciências da Computação
202202499897



Trabalho acadêmico  “Aplicações Rápidas em Python”



Del Castilho – RJ
2023



Documentação
1. Introdução do Sistema
2. Visão Geral do Sistema
	2.1 Estrutura
	2.2 Principais Funcionalidades 
		2.2.1 Login
		2.2.2 Cadastro e Exclusão de Produtos
		2.2.3 Listagem de Produtos
		2.2.4 Modificar Cadastro
		2.2.5 Cadastrar Usuários
3. Apresentação – Login
	3.1 Login
		3.1.1 Lembrar Login
		3.1.2 Carregar Ultimo Login
4. Apresentação – Menu
	4.1 Menu
		4.1.1 Cadastrar Produto
		4.1.2 Listar Produtos
		4.1.3 Editar Cadastro
		4.1.4 Cadastro Usuário
5. Bibliotecas
	5.1 Tkinter
	5.2 CustomTkinter
	5.3 Subprocess
	5.4 MySQL
6. Diagrama de Caso de Uso



Introdução do Sistema
O sistema foi desenvolvido com objetivo de fornecer uma experiência simples e intuitiva para o cadastro, visualização, exclusão e edição de produtos. Sua estrutura é projetada de maneira simples e modular, facilitando a compreensão do programador e tornando a manutenção e modificação mais simples
Visão Geral do Sistema
Estrutura
O sistema é uma aplicação em python. Ele tem funcionalidades de autenticação por login, criação de novas contas de usuários, cadastro, edição, exclusão e visualização de produtos cadastrados no sistema.
A estrutura do código é caracterizada por sua simplicidade e modularidade, o que proporciona uma compreensão intuitiva. Todos os trechos dos códigos sao comentados.
Alguns processos devem ser feitos para o funcionamento correto do sistema, a importação de bibliotecas como Tkinter,  CustomTkinter e o Subprocess são essenciais, e a utilização do mysql como banco de dados.
Principais Funcionalidades
Login: Oferece autenticação segura para acesso às contas existentes, juntamente com as funções Lembrar Login e Carregar Último Login inclusas.
Cadastro e Exclusão de Produtos: Após o login é possível excluir e cadastrar produtos no banco de dados.
Listagem de Produtos: Permite aos usuários visualizar informações relevantes associadas aos produtos cadastrados no banco de dados.
Modificar Cadastro: O usuário é capaz de modificar os produtos armazenados através do ID.
Cadastrar Usuários: Sistema é capaz de criar novas contas.


Apresentação

Login: O usuário deverá preencher seu “Login” e “Senha”;  clicar no botão “Fazer Login”, para iniciar sua sessão. Lembrando que, se for deixado qualquer campo vazio, o sistema informará erro: “Login ou Senha incorretos”
		
Lembrar Login: Se “Login” e “Senha” inseridos, o usuário poderá clicar na checkbox, para que login e senha sejam lembrados na próxima vez.
	                 
Carregar Último Login: O botao carrega os dados do ultimo Login e Senha salvos no checkbox “Lembrar Login”.
                          
Apresentação – Menu

Menu: Acesso às funções do sistema:
     
Cadastrar Produto: No cadastro de produto o usuário cadastra nome do produto e o seu preço pratica na venda.         

Listar Produtos: mostrará todos os itens cadastrados no sistema
de cadastro de produtos. Sua organização é feita por ID do produto cadastrado. 

Editar Cadastro: Primeiro o usuario devera  inserir o ID do produto a ser modificado, em seguida uma outra janela será aberta mostrando nome e valor do produto a ser editado.
    
Cadastro Usuário: O primeiro login o usuário deverá usar Login e Senha padrão do sistema: Admin / Admin. respectivamente.  no painel MENU o usuario poderá cadastrar novos Logins para acesso ao sistema.  



Bibliotecas

Durante o desenvolvimento, algumas bibliotecas foram necessárias para o bom funcionamento do sistema, sendo elas:
Tkinter: usado para utilização de algumas funções para interface do sistema e messagebox. 
CustomTkinter: é uma biblioteca nova, tem funcionamento parecido e complementar com Tkinter, e foi usado para acelerar o desenvolvimento da aplicação e alem disso da visual mais moderno na interface.
Subprocess: o subprocess foi utilizado para execução da segunda parte do programa conectando os codigos fontes. 
Mysql/Xampp: foi a escolha usada para a criação do banco de dados. Exemplos usados na criação:


Repositório do Código-Fonte
Link repositorio GIT: https://github.com/GustavoRio99/Dev.Rapido-Python-SISTEMA
Composição do conteúdo: 


Conclusão

Ao longo do desenvolvimento deste sistema, adquirimos novas técnicas de modularização, possibilitando o rápido e prático desenvolvimento de uma aplicação em Python. A manipulação da interface gráfica se revelou um desafio que ampliou nossos horizontes e abriu possibilidades para futuros projetos. Enfrentamos dificuldades em algumas etapas, como a transição de janelas utilizando o Toplevel do "CustomTkinter" e a abertura da segunda parte do programa. Cada desafio enfrentado proporcionou aprendizados ímpares no âmbito acadêmico, os quais levaremos como valiosas lições para toda a vida.
Expressamos nossa sincera gratidão ao nosso estimado mestre, Prof. Rafael, por toda a orientação e apoio fornecidos ao longo desse percurso acadêmico.

Referências bibliográficas: documentação CustomTkinter: https://libraries.io/pypi/customtkinter
xampp documentação: https://www.apachefriends.org/docs/ , doc Tkinter: https://docs.python.org/3/library/tk.html ,
 Video de basamento: https://www.youtube.com/watch?v=yDRsbt714WA , https://www.youtube.com/watch?v=rQLO1m8oia4 .

			









Estácio Nova America - 2023

