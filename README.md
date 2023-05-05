<!DOCTYPE html>
<html>
<head>
	<title>README</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>
	<h1>Projeto XYZ</h1>
	<p>Este é um projeto para demonstrar a utilização de diversas tecnologias em conjunto para criar uma aplicação web.</p>
	
<h2>Tecnologias Utilizadas</h2>
<ul>
	<li>Python</li>
	<li>Flask</li>
	<li>SQLite</li>
	<li>HTML</li>
	<li>CSS</li>
	<li>Docker</li>
	<li>Ansible</li>
</ul>

<h2>Descrição dos arquivos e pastas</h2>
<ul>
	<li><code>ansible/</code>: pasta com os arquivos do Ansible.</li>
	<li><code>ansible.cfg</code>: arquivo de configuração do Ansible.</li>
	<li><code>hosts</code>: arquivo de inventário do Ansible.</li>
	<li><code>playbook.yml</code>: playbook do Ansible que configura o servidor.</li>
	<li><code>db/</code>: pasta com o banco de dados.</li>
	<li><code>nomes.db</code></li>
	<li><code>python/</code>: pasta com os arquivos da aplicação em Python.</li>
	<li><code>app.py</code>: arquivo principal da aplicação, onde se encontra o código da API.</li>
	<li><code>requirements.txt</code>: arquivo com as dependências da aplicação em Python.</li>
	<li><code>Dockerfile</code>: arquivo para a construção da imagem Docker da aplicação em Python.</li>
	<li><code>html/</code>: pasta com o arquivo HTML que serve como interface para a API.</li>
	<li><code>index.html</code>: arquivo HTML que contém um formulário para envio de dados para a API.</li>
	<li><code>docker-compose.yml</code>: arquivo com as configurações do Docker Compose para a criação dos containers dos serviços da aplicação.</li>
</ul>

<h2>Pré-requisitos</h2>
<p>Antes de seguir os passos deste tutorial, certifique-se de que possui os seguintes pré-requisitos instalados em sua máquina:</p>
<ul>
	<li>Docker</li>
	<li>Docker Compose</li>
</ul>

<h2>Como executar a aplicação</h2>
<p>Para executar a aplicação, siga os seguintes passos:</p>
<ol>
	<li>Clone este repositório em sua máquina:</li>
	<code>git clone https://github.com/seu-usuario/lab-python-api.git</code>
	<li>Acesse a pasta do projeto:</li>
	<code>cd lab-python-api</code>
	<li>Execute o comando abaixo para iniciar os serviços da aplicação:</li>
	<code>docker-compose up -d</code>
	<li>Acesse a interface da aplicação em seu navegador através do endereço <a href="http://localhost:5000">http://localhost:5000</a>.</li>

</ol>
<h2>Como utilizar a aplicação</h2>
<ol>
	<li>Acesse a interface da aplicação em seu navegador através do endereço <a href="http://localhost:5000">http://localhost:5000</a>.</li>
	<li>Preencha o formulário com o nome e a idade da pessoa que deseja cadastrar.</li>
	<li>Clique no botão "Cadastrar".</li>
	<li>Caso o cadastro seja bem-sucedido, a aplicação retornará uma mensagem de sucesso. Caso contrário, uma mensagem de erro será exibida.</li>
	<li>Para visualizar a lista de pessoas cadastradas, acesse o endereço <a href="http://localhost:5000/nomes">http://localhost:5000/nomes</a>.</li>
</ol>
<h2>Licença</h2>
<p>Este projeto está licenciado sob a licença MIT. Consulte o arquivo <a href="https://github.com/seu-usuario/lab-python-api/blob/main/LICENSE">LICENSE</a> para obter mais informações.</p>
