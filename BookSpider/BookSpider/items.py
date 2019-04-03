# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgurl = scrapy.Field() #图片URL
    folder_name = scrapy.Field() #文件夹名称
    title = scrapy.Field() # 小说名称
    desc = scrapy.Field() # 小说详情
    author = scrapy.Field() # 小说作者
    ctime = scrapy.Field() # 创建时间
    img_name = scrapy.Field() # 小说封面图片名
    img_storage_path = scrapy.Field() # 小说封面图片存储路径
    book_category_id = scrapy.Field() # 分类ID
    pass