from unidecode import unidecode
import requests
from bs4 import BeautifulSoup
import re

import locale

# Configurar o local para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#site:   https://www.bocarosadamakeup.com.br/


class Crawler:



    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def extract_from_site(self):
        raw_site = self.request_data("https://www.bocarosadamakeup.com.br/")

        products = raw_site.find_all("div", {"class": "item-container"})

        for product in products:
            image = product.find("img", {"class": "ilazyloaded"})
            title = product.find("div", {"class": "item-name"})
            raw_price = product.find("div", {"class": "item-price"})
         

            if raw_price:
                pattern_price = r"R\$\s*([\d\.]+),(\d+)"
                match = re.search(pattern_price, raw_price.text)

                if match:
                    price = '{:,.2f}'.format(float(match.group(1).replace('.', '').replace(',', '.'))).replace(',', ',')
                else:
                    price = "Preço não encontrado"
            else:
                price = "Preço não encontrado"

            data = {
                "Imagem": image.attrs('src') if image else "Imagem nao encontrada",
                "Titulo": title.text.strip() if title else "Título nao encontrado",
                "Preco R$":  price,
            }

            print("Produto:")
            for key, value in data.items():
                print(f"{key}: {value}")

            print("-" * 50) 

if __name__ == "__main__":
    crawler = Crawler()
    crawler.extract_from_site()
