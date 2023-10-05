import requests
from bs4 import BeautifulSoup
import re

#site:    https://www.magazineluiza.com.br/


class Crawler:

    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def extract_from_site(self):
        raw_site = self.request_data("https://pesquisa.marisa.com.br/hotsite/camisetas-polos-e-regatas-masculinas?id=20231005&name=MOSAICO6&position=P02&category=HOMEPAGE&criativo=CAMISETAS_REGATAS")

        products = raw_site.find_all("li", {"class": "nm-product-item"})

        for product in products:
            image = product.find("img", {"class": "nm-product-img"})
            title = product.find("h4", {"class": "nm-product-name"})
            raw_price = product.find("span", {"class": "price-number"})
            

            if raw_price:
                pattern_price = r"R\$\s*([\d\.]+),(\d+)"
                match = re.search(pattern_price, raw_price.text)

                if match:
                    price = match.group(1)
                else:
                    price = "Preço não encontrado"
            else:
                price = "Preço não encontrado"

            data = {
                "image": image["src"] if image else "Imagem não encontrada",
                "title": title.text.strip() if title else "Título não encontrado",
                "price": price,
            }

            print(data)
            break

if __name__ == "__main__":
    crawler = Crawler()
    crawler.extract_from_site()
