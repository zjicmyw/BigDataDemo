import requests
from pyquery import PyQuery as pq
import csv

url = 'http://www.qiushibaike.com/hot/page/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}


# # 保存百度图片
# response2 = requests.get(
#     url='https://www.baidu.com/img/bd_logo1.png?where=super',
#     headers=headers)
#
# with open('./BigDataDemo/cache/baidu.png', 'wb') as f:
#     f.write(response2.content)
#
# # 获取猫眼电影
# response = requests.get(url='https://maoyan.com/board/4', headers=headers)
#
# print(response.content.decode('utf-8'))
# print(response.headers)
# print(response.status_code)


# ajax动态获取并渲染问题解决方式：1、分析请求 分类获取 2、from selenium import webdriver 模拟浏览器行为

'''
标准的爬虫类：
初始化、获取数据、解析数据、保存数据
'''


class MySpider(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_onePage(self, offset):
        get_url = self.base_url.format(offset)
        response = requests.get(url=get_url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None

    def parse_onePage(self, html):
        pq_html = pq(html)
        list_no = pq_html('.board-index').text().split()
        list_name = pq_html('.movie-item-info .name a').text().split()
        list_star = pq_html('.movie-item-info .star').text().split()
        list_time = pq_html('.movie-item-info .releasetime').text().split()

        list_movie = []
        for i in range(0, 10):
            list_index = [list_no[i], list_name[i], list_star[i], list_time[i]]
            list_movie.append(list_index)
        return list_movie

    def save_txt(self, data):
        for value in data:
            for value_data in value:
                movie_info = ''.join(value_data)
                with open('./BigDataDemo/cache/movie.info.txt', 'a', encoding='utf-8') as f:
                    f.write(movie_info + '\n')

    def save_csv(self, data):
        for value in data:
            with open('./BigDataDemo/cache/movie.info.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(value)


if __name__ == '__main__':

    base_url = 'https://maoyan.com/board/4?offset={}'
    my_spider = MySpider(base_url)
    for offset in range(0, 30, 10):
        result_html = my_spider.get_onePage(offset)
        list_movie = my_spider.parse_onePage(result_html)
        my_spider.save_csv(list_movie)
