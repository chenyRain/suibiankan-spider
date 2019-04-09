

import scrapy

class BookContentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 书籍章节入库需要字段
    book_id = scrapy.Field() #书籍ID
    section_name = scrapy.Field() #章节名称
    section_content = scrapy.Field() #章节内容
    pass