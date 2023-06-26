import scrapy

class MySpider(scrapy.Spider):
    name = 'linkedinextractor'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c']
            # 'https://www.linkedin.com/jobs/search?keywords=Desenvolvedor&location=Brazil&geoId=&position=1&pageNum=0c',
            # 'https://www.linkedin.com/jobs/search?keywords=Frontend+Developer&location=Brazil&geoId=&position=1&pageNum=0c']
    
    def parse(self, response):
        # jobs = response.css('.base-card').getall()
        jobs = response.css('.base-card')
        # with open("results", "w") as f:
        #     f.write(''.join(titulo))
        # print(titulo)
        for job in jobs:
            print(job.xpath('./div/h3/text()').get())
        
if __name__ == '__main__':
    from scrapy.crawler import CrawlerProcess
    
    process = CrawlerProcess()
    process.crawl(MySpider)
    process.start()

