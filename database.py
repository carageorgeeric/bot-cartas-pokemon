import sqlite3

conexao = sqlite3.connect('meubanco.db')  # cria o arquivo se não existir
cursor = conexao.cursor() #objeto que executa comandos sql e devolve os resultados 

cursor.execute('CREATE TABLE IF NOT EXISTS banco_produtos(' \
'id INTEGER PRIMARY KEY AUTOINCREMENT, ' \
'produto TEXT NOT NULL, ' \
'link TEXT NOT NULL, ' \
'preco REAL)') 

# cursor.execute(
#     'INSERT INTO banco_produtos(produto, link, preco) VALUES (?, ?, ?)', 
#     ('Box Alakazam EX 151', 'https://www.amazon.com.br/Pok%C3%A9mon-Trading-Card-Scarlet-Violet151/dp/B0CD7S71WN/ref=sr_1_5?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=VROEZAYLPRM2&dib=eyJ2IjoiMSJ9.4KiGTRpr5TLFhIskkfmDGEzT9hpu42SC74nFbobcQz_q8fHUrCMwZTi4SG32o2xO4DZEv6cLHBXd6OOGLdEks_aCaGOB6d_RjXHxZGRsN2hMVJ2Gd2dm3ac50hlGSTXc1JCKMhVt6k7yB9kbTt70j4eevNjJBJGfVoW3bVBvX04Ux9pR5V_V7emH0vnKqVpZQhiEM_k9D5ykhtLM06ROD_giRRvS1uCunF6NQQM0WBIPflpY7-Yuf-ANcXly_EWTveuPqSe3MMkMQ8ZZMF4lpZXaSQ_qgvbGvps5GaQOK4Y.sv5hQet_71IK1xpFoMwf4j61ghN2bDdcX6gPhEcvy3Y&dib_tag=se&keywords=Pokemon+box+alakazam&qid=1787850298&s=toys&sprefix=pokemon+box+alakazam%2Ctoys%2C178&sr=1-5&ufe=app_do%3Aamzn1.fos.38059ce3-943c-48af-9fc9-22d85542b02c', 1855),
# )


def adicionar_produtos (produto, link, preco): 
    try:
        cursor.execute(
            'INSERT INTO banco_produtos(produto, link, preco) VALUES (?, ?, ?)', \
            (produto, link, preco)
        )
        conexao.commit()
        print(f'Produto {produto} adicionado com sucesso! ') 
    except sqlite3.Error as erro: 
        print(f'Erro ao adicionar o produto!')


adicionar_produtos('Combo Booster Evolucoes Prismaticas','https://www.amazon.com.br/Pok%C3%A9mon-Estampas-Ilustradas-Evolu%C3%A7%C3%B5es-Prism%C3%A1ticas/dp/B0DWT3X5NJ/ref=sr_1_5?crid=3NRK5IIDT3E3O&dib=eyJ2IjoiMSJ9.eAKL5QsSFSDW6JZlA-wj3FKx3nL9LX-BsOU5LveJLp7-YPSyP-QyupMAAN3ivUyJ26tHMZjl7iLYK8DPHYVIG-LRPbCI2B9ygz_8Kqa3B7VsODgkcWCz3KkenqbQXJt12ulWTBF5DKzYnroqbcOuohmB_I95SZZykEmMBCrI2acwjJR0xIlCNiybmp1-St3IkBHDKU01kvG8g_-MKV-jF_p3YLFevYhvYTdegsKMcWv2CiSz_cd4PknSGQY6HLHU136NqPAOrq1FYyILSSKE2EIa_rBc8TN4HFn-ym1CcIFw.2HGVjuSuswKBhupHhLIP1jNrxGxI5Glx8lrfYKNv0i0&dib_tag=se&keywords=pokemon+tcg+evolu%C3%A7%C3%B5es+prism%C3%A1ticas&qid=1787851216&sprefix=Pokemon+TCG+evolu%2Caps%2C223&sr=8-5&ufe=app_do%3Aamzn1.fos.e05b01e0-91a7-477e-a514-15a32325a6d6', 418 )



conexao.close()   # fecha a conexão

