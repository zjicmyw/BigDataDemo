import requests
from pyquery import PyQuery as pq
import csv
import os
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}


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
        ul = pq_html('.grid_view li').items()
        list_li, list_no, list_url, list_name, list_img, list_star, list_star_num, list_desc = [
        ], [], [], [], [], [], [], []
        for li in ul:
            list_no = li('.pic em').text()
            list_url = li('.pic a').attr('href')
            list_img = li('.pic a img').attr('src')
            list_name = trim(li('.info .hd a').text())
            list_star = li('.bd .star .rating_num').text()
            list_star_num = li('.bd .star span').text().split()
            list_desc = li('.bd .quote span').text()
            list_info = li('.bd p').eq(0).text().split(
                '\xa0\xa0\xa0')  # 用空格空格空格分割
            list_director = list_info[0][3:]
            list_temp1 = []
            list_actor = ''
            # 有的电影没有写主演
            if (li('.bd p').eq(0).text().find('主')) > 0:
                list_temp1 = list_info[1].split('\xa0/\xa0')  # 用空格/空格分割
                list_actor = list_temp1[0].split('\n')[0][3:]  # 用换行符分割，年份在第二行
            else:
                list_temp1 = list_info[0].split('\xa0/\xa0')
            list_year = list_temp1[0].split('\n')[1]
            list_area = list_temp1[1]
            list_type = list_temp1[2]
            list_li.append([list_no, list_name, list_star_num[0], list_star_num[1][:-3], list_desc,
                            list_director, list_actor, list_year, list_area, list_type, list_url, list_img])
        return list_li

    def save_csv(self, data, save_path):
        for value in data:
            with open(save_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(value)


def dir_exist(dir_exist):
    if not os.path.exists(dir_exist):
        os.makedirs(dir_exist)


def file_exist(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['排名', '片名', '分数', '评价人数', '简评',
                             '导演', '主演', '年份 ', '国家/地区', '类型', '详情页链接', '海报链接'])


def trim(str):
    return "".join(str.split())  # 去重空格\xa0


if __name__ == '__main__':

    cache_path = 'cache/'
    dir_exist(cache_path)
    file_path = 'cache/movie_info_dbtop250.csv'
    file_exist(file_path)

    base_url = 'https://movie.douban.com/top250?start={}&filter='
    my_spider = MySpider(base_url)
    for offset in range(0, 250, 25):
        result_html = my_spider.get_onePage(offset)
        list_movie = my_spider.parse_onePage(result_html)
        my_spider.save_csv(list_movie, file_path)
        print('读取完成'+str(offset+25)+'条')
        time.sleep(3)
    print('豆瓣top250电影读取全部完成')
