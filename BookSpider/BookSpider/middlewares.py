# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from BookSpider.resource import PROXIES, USER_AGENTS  #引入Ip池和ua
import random


class RandomProxy(object): #在settings.py中配置后会被自动执行
    def process_request(self, request, spider): #用random设置随机的代理ip
        proxy = random.choice(PROXIES)
        request.meta['proxy'] = 'http://%s' % proxy


class RandomUser(object):
    def process_request(self, request, spider): #同理设置UA
        UA = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', random.choice(UA))