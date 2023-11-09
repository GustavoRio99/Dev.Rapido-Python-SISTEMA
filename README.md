# Dev.Rapido-Python-SISTEMA
Trabalho academico desenvolvido em python.  Sistema basico intuitivo.

          
		UNESA - Universidade Estacio de Sa

Gustavo de Oliveira Rio
202202499897


Trabalho de Aplicações Rápidas em Python


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
O sistema foi desenvolvido com objetivo de fornecer uma experiência simples e intuitiva para o cadastro, visualização e exclusão de produtos. Sua estrutura é projetada de maneira simples e modular, facilitando a compreensão do programador e tornando a manutenção e modificação mais acessíveis.
Visão Geral do Sistema
Estrutura
O sistema é uma aplicação em python usado para gestão de contas de usuários e manipulação do banco de dados. Ele tem funcionalidades de criação de novas contas, autenticação por login, visualização, inclusão e exclusão de itens no banco de dados.
A estrutura do sistema é caracterizada por sua simplicidade e modularidade, o que proporciona aos programadores uma compreensão intuitiva para realizar manutenções e implementar modificações com facilidade.
Alguns processos devem ser feitos para o funcionamento correto do sistema, a importação de bibliotecas como Tkinter,  CustomTkinter e o Subprocess são essenciais, e a utilização do mysql como banco de dados.
Principais Funcionalidades
Login: Oferece autenticação segura para acesso às contas existentes, juntamente com as funções Lembrar Login e Carregar Último Login inclusas.
Cadastro e Exclusão de Produtos: Após o login é possível excluir e cadastrar produtos no banco de dados.
Listagem de Produtos: Permite aos usuários visualizar informações relevantes associadas aos produtos cadastrados no banco de dados.
Modificar Cadastro: O usuário é capaz de modificar os produtos armazenados através do ID.
Cadastrar Usuários: Sistema é capaz de criar novas contas.


Apresentação – Login
Login: Na aba de login, o usuário deverá colocar seu Login e Senha; e clicar no botão Fazer Login, para iniciar sua sessão. Lembrando que, se for deixado alguma das pendências vazias, aparecerá uma caixa de mensagem mencionando o erro.
	

Lembrar Login: Enquanto for colocado seu Login e Senha, o usuário poderá clicar na checkbox, para que seu último login seja salvo. O salvamento é feito através da criação de um arquivo texto no computador do usuário.
	                 

                         	              
Carregar Último Login: Abaixo da checkbox ,Lembrar Login, haverá um link, esse link carrega os dados do arquivo texto, assim completando as lacunas com seu login passado.
                           

Apresentação – Menu

Menu: Na aba menu, o usuário tem acesso a várias opções de execução. Sendo elas:
     Cadastrar Produto: No cadastro de produto o usuário é capaz de interagir com banco de dados através da outra tela que aparece ao apertar tal botão. Nesta nova tela o usuário consegue inserir o nome e o valor do produto a ser armazenado.      

Se o usuário não colocar nada e mesmo assim tentar cadastrar aparecerá um erro na tela.

Listar Produtos: Quando clicado na seleção Listar Produto, uma nova aba aparecerá e mostrará todos os itens armazenados
no banco de dados. Sendo organizado através do Id do produto. 

Editar Cadastro: Nesta seleção uma nova aba será aberta, mostrando uma pequena janela, para inserir o id do produto a ser modificado, e quando posto o ID, uma outra janela será aberta, agora mostrando o nome e valor do item, que poderá ser modificado, e após a conclusão; clicar no Atualizar.      

Cadastro Usuário: O cadastro só pode ser feito, se um outro usuário já tiver uma conta, com isso em mente, este outro usuário abrirá a seleção: Cadastro Usuário, assim abrindo uma tela de cadastro, muito parecida com a de login, ali deverá ser colocado seu login e senha. Após isso, só clicar em salvar.     




Bibliotecas

Durante o desenvolvimento, algumas bibliotecas foram necessárias para o bom funcionamento do sistema, sendo elas:
Tkinter: usado para utilização de algumas funções para interface do sistema, como o messagebox. 
CustomTkinter: é uma biblioteca nova, tem funcionamento parecido e complementar com Tkinter, e foi usado para uma aplicação mais moderna da interface.
Subprocess: o subprocess foi utilizado para inicialização de um comando externo.
Mysql: foi a escolha usada para a criação do banco de dados. Exemplos usados:




