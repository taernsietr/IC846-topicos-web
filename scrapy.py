import scrapy

class MySpider(scrapy.Spider):
    name = 'linkedinextractor'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c']
            # 'https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c',
            # 'https://www.linkedin.com/jobs/search?keywords=Frontend+Developer&location=Brazil&geoId=&position=1&pageNum=0c']
    
    def parse(self, response):
        # titulo = response.css('.jobs-search__results-list').get()
        titulo = response.css('.google-auth').get()
        print(titulo)
        
if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()

