import scrapy

class MySpider(scrapy.Spider):
    name = 'linkedinextractor'
    # TODO: parametrizar busca e iterar mais resultados
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c']
            # 'https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c',
            # 'https://www.linkedin.com/jobs/search?keywords=Frontend+Developer&location=Brazil&geoId=&position=1&pageNum=0c']
    
    def parse(self, response):
        jobs = response.css('.base-card')

        with open("results.csv", "w") as results:
            results.write('Title,Publisher,Location,Time Posted\n')

            for job in jobs:
                title = job.xpath('./div/h3/text()').get().strip()

                # deve haver solução melhor; na maioria dos resultados o nome da empresa que publicou a vaga é um link
                # escondido; em outros, não, estando fora de um elemento <a>. Assim, é necessário garantir que seja possível
                # pegar o nome independentemente do caso.
                publisher = job.xpath('./div/h4/a/text()')
                if not publisher:
                    publisher = job.xpath('./div/h4/text()')
                publisher = publisher.get().strip()

                location = job.xpath('./div/div/span/text()').get().strip()
                time_posted = job.xpath('./div/div/time/@datetime').get().strip()

                results.write(f'{title},{publisher},{location},{time_posted}\n')
        
if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()

