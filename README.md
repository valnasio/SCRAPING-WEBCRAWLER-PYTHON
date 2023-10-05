# Webcrawler_Curso DOCUMENTAÇÃO  

Executando a Aplicação

Este guia descreve como configurar e executar a aplicação em um ambiente virtual (venv).
Pré-requisitos

    Python 3.x instalado
    Git instalado (opcional)

Configurando o Ambiente Virtual

    Clone o repositório do Git (caso ainda não tenha feito isso):

   

git clone https://github.com/valnasio/Webcrawler_Curso.git

Navegue até o diretório do projeto:



cd seu-repositorio

Crie um ambiente virtual (venv):

python -m venv venv

Ative o ambiente virtual:

    No Windows:

venv\Scripts\activate

No macOS e Linux:



    source venv/bin/activate

Instale as dependências do projeto:

    pip install -r requirements.txt

Executando a Aplicação

    Agora, você pode executar a aplicação. Supondo que seu arquivo principal seja chamado crawler.py, você pode executá-lo com o seguinte comando:

python crawler.py

A aplicação começará a rodar e exibirá os resultados no terminal.
