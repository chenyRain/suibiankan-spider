import scrapy
from BookSpider.items import BookspiderItem
# 爬取书籍详情

class BookSpider(scrapy.Spider):
    name = "book" # 蜘蛛名，执行时需要 scrapy crawl book_desc
    allowed_domains = ["www.booktxt.net"]
    start_urls = ["https://www.booktxt.net/1_1589/"]

    def parse(self, response):
        book_id = 9
        domain = "https://www.booktxt.net/1_1589/"
        
        section_name = response.xpath('//*[@id="list"]/dl/dd[9]/a//text()').extract_first()
        section_url = response.xpath('//*[@id="list"]/dl/dd[9]/a//@href').extract_first()

        book = BookspiderItem() # 实例化item
        book['section_name'] = section_name

        yield book
        pass