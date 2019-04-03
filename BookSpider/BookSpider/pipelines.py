# -*- coding: utf-8 -*-
import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class BookspiderPipeline(ImagesPipeline):
    def get_media_requests(self, img, info):

    	# meta里面的数据可以从spider获取，然后通过meta传递给下面方法：file_path
        yield Request(img['imgurl'], meta = {'folder_name' : img['folder_name'], 'img_name' : img['img_name']})

    # 重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    def file_path(self, request, response=None, info=None):

    	# 生成随机名称 -- 图片名
    	image_name = request.meta['img_name']

    	# 文件夹名
    	name = request.meta['folder_name']

    	# 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
    	name = re.sub(r'[？\\*|“<>:/]', '', name)

    	# 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
    	filename = u'{0}/{1}'.format(name, image_name)
    	return filename