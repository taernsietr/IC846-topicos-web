'''
- Use uma ferramenta como scrapy ou selenium para realizar uma busca no Instagram ou Twitter.
- Pegue as 10 primeiras publicações que tiverem localização relacionada.
- Para busca, escolha um tema do seu interesse. O termo usado na busca deve ser parametrizável.
- Salve o link da publicação, o texto, a localização, a data de publicação, a quantidade de curtidas e de comentários.
- Você pode salvar em arquivo ou banco de dados.
- No caso do arquivo, defina uma maneira de deixar seu arquivo organizado. Pode usar CSV ou JSON.
- Esse trabalho pode ser feito no mesmo grupo do seu trabalho da disciplina.

O Entregável é: 
    1. o código; e 
    2. a explicação das dependências para o código rodar.

    ---

fazer a busca
para cada post:
    acessa o post pelo href
    verifica se a div de localização tem conteúdo 
      se tiver, coleta as informações e salva 
      senão, retorna aos resultados da busca
    repetir até acessar 10 posts com localização ou caso a busca seja exaurida
'''

import sys, scrapy

saved_posts = []
search_term = sys.argv[1]
search_link = f'https://www.instagram.com/explore/tags/{search_term}/'


class MySpider(scrapy.Spider):
    name = 'igminer'
    start_urls = [search_link]
    
    def parse(self, response):
        href = response.css('a.x1i10hfl::attr(href)').get()
        print(href)

if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()
