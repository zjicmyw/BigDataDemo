import requests
from pyquery import PyQuery as pq
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

'''
标准的爬虫类：
初始化、获取数据、解析数据、保存数据
可以直接从html上获取数据的
'''


class MyDangDangSpider(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_onePage(self, offset):
        get_url = self.base_url.format(offset)
        response = requests.get(url=get_url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('GBK')
        else:
            return None

    def parse_onePage(self, html):
        pq_html = pq(html)
        ul = pq_html('.bigimg li').items()
        list_name, list_img = [], []
        for li in ul:
            list_name.append(li('.name a').attr('title'))
            if li('.pic img').attr('data-original'):
                list_img.append(li('.pic img').attr('data-original'))
            else:
                list_img.append(li('.pic img').attr('src'))

        list_book = []
        for i in range(0, 10):
            list_index = [list_name[i], list_img[i]]
            list_book.append(list_index)
        return list_book

    def save_txt(self, data):
        for value in data:
            for value_data in value:
                movie_info = ''.join(value_data)
                with open('./BigDataDemo/cache/book_info.txt', 'a', encoding='utf-8') as f:
                    f.write(movie_info + '\n')

    def save_csv(self, data):
        for value in data:
            with open('./BigDataDemo/cache/book_info.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(value)


if __name__ == '__main__':

    base_url = 'http://search.dangdang.com/?key=python&act=input&page_index={}'
    my_spider = MyDangDangSpider(base_url)
    for offset in range(1, 2):
        result_html = my_spider.get_onePage(offset)
        list_book = my_spider.parse_onePage(result_html)
        print(list_book)
        my_spider.save_txt(list_book)
