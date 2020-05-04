import requests
import time
import json
import csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

'''
不可以直接从html上获取数据的，需要从json获取
json 模块的四个方法：dumps(序列化)/loads(反序列化)/dump/load
'''


class MyJsonSpider(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_onePage(self, timestamp, keyword, pageIndex):
        get_url = self.base_url.format(timestamp, keyword, pageIndex)
        response = requests.get(url=get_url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None

    def parse_onePage_json(self, result_json):
        post_list = []
        job_list = []

        dict_result = json.loads(result_json)
        if dict_result['Code'] == 200:
            post_list = dict_result['Data']['Posts']
            for value in post_list:
                job_list.append(
                    [value['RecruitPostName'], value['LocationName'], value['CategoryName'], value['Responsibility'],
                     value['PostURL']])
        else:
            print('访问错误')

        return job_list

    def save_txt(self, data):
        for value in data:
            for value_data in value:
                movie_info = ''.join(value_data)
                with open('./BigDataDemo/cache/tencent_info.txt', 'a', encoding='utf-8') as f:
                    f.write(movie_info + '\n')

    def save_csv(self, data):
        for value in data:
            with open('./BigDataDemo/cache/tencent_info.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(value)


if __name__ == '__main__':

    base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    my_spider = MyJsonSpider(base_url)
    for offset in range(1, 3):
        # 获得时间戳
        timestamp = int(time.time()) * 1000
        result_json = my_spider.get_onePage(timestamp, 'python', offset)

        job_list = my_spider.parse_onePage_json(result_json)

        my_spider.save_csv(job_list)
