"""
@author: tony-tan
@time: 2019/6/21 16:32
@file: aio_http_spider.py
@site: 
@describe: 基于aio_http 实现的 高并发的爬虫
"""
# async-io爬虫: 去重、入库
import asyncio
import aiohttp
import aiomysql

from pyquery import PyQuery

start_url = "http://www.jobbole.com"


async def fetch():
	async with aiohttp.ClientSession() as session:
		try:
			async with session.get(start_url) as resp:
				print("url status {}".format(resp.status))
				if resp.status in [200, 201]:
					data = await resp.text()
					return data
		except Exception as e:
			print(e)


async def main(loop):
	# 等待mysql 建立连接
	pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
									  user='root', password='',
									  db='mysql', loop=loop,
									  charset="utf8", autocommit=True)
