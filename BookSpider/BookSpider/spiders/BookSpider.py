import scrapy
import time
import uuid
from BookSpider.items import BookspiderItem
# 爬取书籍详情

class BookSpider(scrapy.Spider):
    name = "book" # 蜘蛛名，执行时需要 scrapy crawl book_desc
    allowed_domains = ["www.booktxt.net"]
    start_urls = ["https://www.booktxt.net/1_1589/"]

    def parse(self, response):
        domain = "https://www.booktxt.net"
        folder_name = '1' # 文件夹名
        storage_path = '/upload/book_cover/' # 存储路径
        book_category_id = 9 # 分类ID

        title = response.xpath('//*[@id="info"]/h1//text()').extract_first()
        author = response.xpath('//*[@id="info"]/p[1]//text()').extract_first()
        desc = response.xpath('//*[@id="intro"]/p//text()').extract_first()

        img = BookspiderItem() # 实例化item
        cover = response.xpath('//*[@id="fmimg"]/img//@src').extract_first()
        img['imgurl'] = domain + cover # 爬取图片url
        img['folder_name'] = folder_name
        img['title'] = title # 小说名称
        img['desc'] = desc #小说详情
        img['ctime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) #当前时间
        img['book_category_id'] = book_category_id
        img['author'] = author.split('：')[-1] # 小说作者
        img['img_name'] = '%s.jpg' % uuid.uuid4().hex # 小说封面图片名 -随机32位
        img['img_storage_path'] = storage_path + folder_name + '/' + img['img_name'] # 数据库存储路径
        yield img
        pass