<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"
		integrity="sha512-EU1/jlG/JI5aaxNWtUpy4nC91V9YBlzO9IQz3PnO+1vgsTMTjCv+vLmiDzgNTvzh4ck3rnGXKpFQc8MRz9I7Og=="
		crossorigin="anonymous" referrerpolicy="no-referrer" />
	<title>Lab Python API</title>
</head>
<body>
	<h1>Lab Python API</h1>
	<p>Este é um laboratório com uma API Python simples e um site que se comunica com a API e armazena dados em um banco de dados local.</p>
	<h2>Tecnologias utilizadas:</h2>
	<ul>
		<li><i class="fab fa-python"></i> Python</li>
		<li><i class="fab fa-docker"></i> Docker</li>
		<li><i class="fab fa-docker"></i> Docker Compose</li>
		<li><i class="fab fa-ansible"></i> Ansible</li>
		<li><i class="fab fa-html5"></i> HTML</li>
		<li><i class="fab fa-css3-alt"></i> CSS</li>
		<li><i class="fab fa-js-square"></i> JavaScript</li>
		<li><i class="fab fa-bootstrap"></i> Bootstrap</li>
		<li><i class="fab fa-font-awesome"></i> Font Awesome</li>
	</ul>
	<h2>Como utilizar:</h2>
	<ol>
		<li>Instale o <a href="https://www.docker.com/get-started">Docker</a> e o <a href="https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html">Ansible</a>.</li>
		<li>Clone o repositório:</li>
		<pre><code>git clone https://github.com/seu-usuario/lab-python-api.git</code></pre>
		<li>Execute o comando para iniciar o ambiente:</li>
		<pre><code>docker-compose up -d</code></pre>
		<li>Execute o comando para executar o playbook do Ansible:</li>
		<pre><code>ansible-playbook -i ansible/hosts ansible/playbook.yml</code></pre>
		<li>Acesse o site em seu navegador:</li>
		<pre><code>http://localhost:5000</code></pre>
	</ol>
	<h2>Descrição dos arquivos e pastas:</h2>
	<ul>
		<li><strong>ansible/</strong>: pasta com os arquivos do Ansible.</li>
		<ul>
			<li><strong>ansible.cfg</strong>: arquivo de configuração do Ansible.</li>
			<li><strong>hosts</strong>: arquivo de inventário do Ansible.</li>
			<li><strong>playbook.yml</strong>: playbook do Ansible que configura o servidor.</li>
		</ul>
		<li><strong>db/</strong>: pasta com o banco de dados.</li>
		<ul>
			<li><strong>nomes.db</strong</li>
		</ul>
	</li>
	<li>
		<strong>python/</strong>: pasta com os arquivos da aplicação em Python.
		<ul>
			<li>
				<strong>app.py</strong>: arquivo principal da aplicação, onde se encontra o código da API.
			</li>
			<li>
				<strong>requirements.txt</strong>: arquivo com as dependências da aplicação em Python.
			</li>
			<li>
				<strong>Dockerfile</strong>: arquivo para a construção da imagem Docker da aplicação em Python.
			</li>
		</ul>
	</li>
	<li>
		<strong>html/</strong>: pasta com o arquivo HTML que serve como interface para a API.
		<ul>
			<li>
				<strong>index.html</strong>: arquivo HTML que contém um formulário para envio de dados para a API.
			</li>
		</ul>
	</li>
	<li>
		<strong>docker-compose.yml</strong>: arquivo com as configurações do Docker Compose para a criação dos containers dos serviços da aplicação.
	</li>
</ul>
Pré-requisitos
Antes de seguir os passos deste tutorial, certifique-se de que possui os seguintes pré-requisitos instalados em sua máquina:

Docker
Docker Compose
Como executar a aplicação
Para executar a aplicação, siga os seguintes passos:

Clone este repositório em sua máquina:

bash
Copy code
git clone https://github.com/seu-usuario/lab-python-api.git
Acesse a pasta do projeto:

bash
Copy code
cd lab-python-api
Execute o comando abaixo para iniciar os serviços da aplicação:

Copy code
docker-compose up -d
Acesse a interface da aplicação em seu navegador através do endereço http://localhost:5000.

Como utilizar a aplicação
Para utilizar a aplicação, siga os seguintes passos:

Acesse a interface da aplicação em seu navegador através do endereço http://localhost:5000.

Preencha o formulário com o nome e a idade da pessoa que deseja cadastrar.

Clique no botão "Cadastrar".

Caso o cadastro seja bem-sucedido, a aplicação retornará uma mensagem de sucesso. Caso contrário, uma mensagem de erro será exibida.

Para visualizar a lista de pessoas cadastradas, acesse o endereço http://localhost:5000/nomes.

Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.