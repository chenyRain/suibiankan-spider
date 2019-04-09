import pymysql.cursors


class MySQLPipeline(object):
	def __init__(self):
		# 连接数据库
		self.connect = pymysql.connect(
			host='192.168.8.228',#数据库地址
			port=3306,# 数据库端口
			db='suibiankan', # 数据库名
			user = 'root', # 数据库用户名
			passwd='', # 数据库密码
			charset='utf8', # 编码方式
			use_unicode=True)

		# 通过cursor执行增删查改
		self.cursor = self.connect.cursor();

	def process_item(self, item, spider):
		if type(item).__name__ == 'BookContentItem':
			# 内容
			print('================添加 《'+ item['section_name'] +'》 章节中...')

			self.cursor.execute(
				"""insert into sbk_book_section(book_id, section_name, section_content)
				value (%s, %s, %s)""",#纯属python操作mysql知识，不熟悉请恶补
				(item['book_id'],# item里面定义的字段和表字段对应
					item['section_name'],
					item['section_content']))

			# 提交sql语句
			self.connect.commit()
			print('================《'+ item['section_name'] +'》 章节添加完成!')

			return item #必须实现返回
		else:
			print('================正在数据库中添加 《'+ item['title'] +'》 的详情...')

			# 详情
			self.cursor.execute(
				"""insert into sbk_book(book_name, book_desc, book_author, section_sum, book_cover, book_category_id, ctime)
				value (%s, %s, %s, %s, %s, %s, %s)""",#纯属python操作mysql知识，不熟悉请恶补
				(item['title'],# item里面定义的字段和表字段对应
					item['desc'],
					item['author'],
					item['section_sum'],
					item['img_storage_path'],
					item['book_category_id'],
					item['ctime']))

			# 提交sql语句
			self.connect.commit()
			print('================《'+ item['title'] +'》 的详情添加完成!')

			return item #必须实现返回