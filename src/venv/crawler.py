# Importe a função unidecode para lidar com caracteres acentuados
from unidecode import unidecode

# Importe as bibliotecas necessárias
import requests  # Para fazer solicitações HTTP
from bs4 import BeautifulSoup  # Para analisar o HTML
import re  # Para expressões regulares

# Importe a biblioteca locale para configurar o local
import locale

# Configurar o local para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Defina a classe Crawler
class Crawler:

    # Método para fazer solicitação HTTP e retornar o HTML analisado
    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    # Método para extrair dados do site
    def extract_from_site(self):
        # Faça a solicitação HTTP e analise o HTML do site
        raw_site = self.request_data("https://www.bocarosadamakeup.com.br/")

        # Encontre todas as divisões com a classe "item-container"
        products = raw_site.find_all("div", {"class": "item-container"})

        # Itere sobre os produtos encontrados
        for product in products:
            # Encontre a imagem do produto
            image = product.find("img", {"class": "ilazyloaded"})
            
            # Encontre o título do produto
            title = product.find("div", {"class": "item-name"})
            
            # Encontre o preço bruto do produto
            raw_price = product.find("div", {"class": "item-price"})

            # Verifique se há um preço bruto
            if raw_price:
                # Use uma expressão regular para extrair o preço em formato "R$ x,xx"
                pattern_price = r"R\$\s*([\d\.]+),(\d+)"
                match = re.search(pattern_price, raw_price.text)

                # Se houver uma correspondência, formate o preço com duas casas decimais
                if match:
                    price = '{:,.2f}'.format(float(match.group(1).replace('.', '').replace(',', '.'))).replace(',', ',')
                else:
                    price = "Preço não encontrado"
            else:
                price = "Preço não encontrado"

                        # REFERENCIANDO O LINK DO PRODUTO
            link = product.find('a', {'class': 'item-actions m-top-half'})

            # Verifique se o link foi encontrado
            if link:
                # Se o link existe, acesse o atributo 'href'
                link_url = link.get('href')
            else:
                # Se o link não foi encontrado, defina como uma string vazia ou uma mensagem de erro
                link_url = "Link não encontrado"

            # Crie um dicionário de dados com imagem, título, preço e link
            data = {
                "Imagem": image.attrs['src'] if image else "Imagem não encontrada",
                "Título": title.text.strip() if title else "Título não encontrado",
                "Preço R$": price,
                "Link": link_url
}
            # Imprima os dados do produto
            print("Produto:")
            for key, value in data.items():
                print(f"{key}: {value}")

            # Imprima uma linha divisória para separar os produtos
            print("-" * 50) 

# Verifique se o código está sendo executado como um script principal
if __name__ == "__main__":
    # Crie uma instância da classe Crawler
    crawler = Crawler()
    
    # Execute o método para extrair dados do site
    crawler.extract_from_site()