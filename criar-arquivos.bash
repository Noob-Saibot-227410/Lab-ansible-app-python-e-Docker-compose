@echo off

REM Criação das pastas
mkdir lab-python-api
cd lab-python-api
mkdir ansible db python html

REM Criação dos arquivos
cd ansible
type nul > ansible.cfg
type nul > hosts
type nul > playbook.yml

cd ../db
type nul > nomes.db

cd ../python
type nul > app.py
type nul > requirements.txt
type nul > Dockerfile

cd ../html
type nul > index.html

cd ..
type nul > docker-compose.yml

echo Estrutura do laboratório criada com sucesso!
pause
