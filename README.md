## Script em Python para monitoramento de preços de cartas pokemon e outros produtos 

## Como funciona

1. Os links dos produtos a monitorar ficam salvos numa tabela `banco_produtos` (colunas `link` e `preços`).
2. O script busca cada link, faz scraping da página com `requests` + `BeautifulSoup`, e extrai título e preço atual.
3. O preço atual é comparado com o preço salvo no banco — se caiu, o script sinaliza.

## Requisitos

- Python 3.10+
- Dependências:
  ```
  pip install requests beautifulsoup4 lxml
  ```

## Estrutura do projeto

```
main.py        # scraping + comparação de preços
produtos.py     # lista de produtos-alvo
database.py     # conexão e cursor do banco (SQL)
```

## Configuração do banco

Antes de rodar, crie a tabela `banco_produtos` com pelo menos as colunas:

| coluna   | tipo         |
|----------|--------------|
| link     | texto        |
| preco   | numérico     |
| produto   | texto     |

Configure a conexão em `database.py` de acordo com o banco que você está usando (SQLite, PostgreSQL, MySQL etc.).

## Uso

```
python main.py
```

O script percorre todos os links salvos, busca o preço atual de cada um, e imprime os detalhes do produto junto com o resultado da comparação.

## Limitações conhecidas

- Depende da estrutura HTML atual da Amazon (`productTitle`, `a-price-whole`) — pode quebrar se a Amazon mudar o layout.
- Usa `time.sleep(3)` entre requisições pra reduzir risco de bloqueio; não há tratamento de captcha ou rate-limit mais robusto.
- Requer um header de `User-Agent` válido para evitar bloqueio de bot.
  
