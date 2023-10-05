import requests
from bs4 import BeautifulSoup
import re


class Crawler:
    def request_data(self, url: str):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    def extract_from_site(self):
        raw_site = self.request_data("https://www.artshopquadros.com.br/")

        products = raw_site.find_all("div", {"class": "product-image-block"})

        for product in products:
            image = product.find("img", {"class": "product-image-block"})
            title = product.find("h3", {"class": "caption"})
            raw_price = product.find("span", {"class": "price-mob"})

        if raw_price:
            pattern_price = r"R\$\s*([\d\.]+),(\d+)"
            match = re.search(pattern_price, raw_price.text)

            data = {
                "image": image["src"],
                "title": title.text,
                "price": match.group(0) if match else "Preço não encontrado",
                
            }

            print(data)


if __name__ == "__main__":
    crawler = Crawler()
    crawler.extract_from_site()
