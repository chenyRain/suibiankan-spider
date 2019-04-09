import scrapy
import time
import re
import uuid
from BookSpider.items import BookDescItem
from BookSpider.BookContentItems import BookContentItem
from scrapy.http import Request
# 爬取书籍详情

class BookSpider(scrapy.Spider):
    name = "book" # 蜘蛛名，执行时需要 scrapy crawl book_desc
    allowed_domains = ["www.readnovel.com"]
    start_urls = ["https://www.readnovel.com/book/21988277000642502"]

    def parse(self, response):
        folder_name = '1' # 文件夹名
        storage_path = '/upload/book_cover/' # 存储路径
        book_category_id = 9 # 分类ID
        img_prefix = "http:"
        content_prefix = "https:"

        title = response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/h1/em//text()').extract_first()

        print('================正在获取《 '+ title +' 》详情...')

        author = response.xpath('/html/body/div[1]/div[3]/div[1]/div[2]/h1/a//text()').extract_first()
        desc = response.xpath('string(/html/body/div[1]/div[3]/div[1]/div[2]/p[3])').extract()
        section_sum = response.xpath('//*[@id="J-catalogCount"]//text()').extract_first()
        section_sum = re.findall(r"\d+\.?\d*", section_sum)
        cover = response.xpath('//*[@id="bookImg"]/img//@src').extract_first()
        cover = cover.replace('\r', '')

        book_desc = BookDescItem() # 实例化item
        book_desc['imgurl'] = img_prefix + cover # 爬取图片url        
        book_desc['folder_name'] = folder_name
        book_desc['title'] = title # 小说名称
        book_desc['section_sum'] = section_sum[0] # 小说所有章节
        book_desc['desc'] = desc #小说详情
        book_desc['ctime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) #当前时间
        book_desc['book_category_id'] = book_category_id
        book_desc['author'] = author.split()[0] # 小说作者
        book_desc['img_name'] = '%s.jpg' % uuid.uuid4().hex # 小说封面图片名 -随机32位
        book_desc['img_storage_path'] = storage_path + folder_name + '/' + book_desc['img_name'] # 数据库存储路径

        print('================获取《 '+ title +' 》详情完成!!')

        yield book_desc

        # 获取目录
        chapter_urls = response.xpath('//div[@class="volume"]/ul/li/a//@href').extract()
        for chapter_url in chapter_urls:
            yield Request(content_prefix + chapter_url, callback=self.parse_content)
        

    # 获取内容
    def parse_content(self, response):
        section_name = response.xpath('//h3[@class="j_chapterName"]//text()').extract_first()
        section_content = response.xpath('string(//div[@class="read-content j_readContent"])').extract()
        book_id = 2

        print('================正在获取《 '+ section_name +' 》内容中...')

        content = BookContentItem() # 实例化item
        content['section_name'] = section_name
        content['section_content'] = section_content
        content['book_id'] = book_id

        print('================获取《 '+ section_name +' 》内容完成!!')

        yield content