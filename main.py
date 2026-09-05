import requests
from bs4 import BeautifulSoup
import time 
from produtos import lista_produtos
from database import cursor, conexao



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'
}

def get_product_details_amazon(product_url: str) -> dict:
    product_details = {}
    page = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(page.content, features='lxml')
    try:
        title = soup.find('span', attrs={'id': 'productTitle'}).get_text().strip()
        price = soup.find('span', attrs={'class': 'a-price-whole'}).get_text().strip()

        product_details['title'] = title 
        product_details['price'] = price 
        #product_details['url'] = product_url

        return product_details
    except Exception as e:
        print(f"Error fetching product details: {e}")
  

def limpar_preco(preco_str: str) -> int: 
    preco_limpo = preco_str.replace('.', '').replace(',', '.')
    return int(float(preco_limpo))


cursor.execute('SELECT link, preco, produto FROM banco_produtos')
produtos_db = cursor.fetchall()

if __name__ == "__main__":
    for product in produtos_db: 
        product_url = product[0]
        preco_antigo = int(product[1])
        product_details = get_product_details_amazon(product_url)
        preco_novo = limpar_preco(product_details['price'
        ])
        print(product_details)
        if preco_novo < preco_antigo: 
                    print(f'Desconto no {product[2]} de {preco_antigo} para {preco_novo}')
        time.sleep(3)









