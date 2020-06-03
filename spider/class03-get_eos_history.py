import requests
from pyquery import PyQuery as pq
import csv
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

'''
标准的爬虫类：
初始化、获取数据、解析数据、保存数据
可以直接从html上获取数据的
'''


class MySpider(object):
    def __init__(self, base_url,save_path,file_name,file_type):
        self.base_url = base_url
        self.save_path=save_path
        self.file_name=file_name
        self.file_path=save_path+file_name
        self.file_type=file_type

    def get_onePage(self, offset):
        get_url = self.base_url.format(offset)
        post_data = {"account_name":"befullcoin33","pos":-1,"offset":-100}
        response = requests.post(url=get_url, data=post_data,headers=headers)
        print(response)
        print(response.text)
        print(response.content)
        if response.status_code == 200:
            print(response)
            print(response.text)
            print(response.content)
            return ''
        else:
            return None

    def parse_onePage(self, html):
        pq_html = pq(html)
        result_list = []
        div = pq_html('#actions')
        print(pq_html)
        list_name, list_img = [], []
        # for item in div:
        #     print(item.text())

        # for i in range(0, 10):
        #     list_index = [list_name[i], list_img[i]]
        #     result_list.append(list_index)
        return result_list

    def save(self,save_data):
        self.file_exist()
        if self.file_type=='txt':
            self.save_txt(save_data)
        elif self.file_type=='csv':
            self.save_csv(save_data)

    def save_txt(self, data):
        with open(self.file_path, 'a', encoding='utf-8') as f:
            for value in data:
                for item in value:
                    str_item=''.join(item)
                    f.write(str_item + '\n')

    def save_csv(self, data):
        for value in data:
            with open(self.file_path, 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(value)

    def file_exist(self):
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                pass
        else:
            with open(self.file_path, 'w') as f:
                f.write('')


    


if __name__ == '__main__':
    base_url = 'https://eos.greymass.com/v1/history/get_actions'
    my_spider = MySpider(base_url,'cache/', 'eos_account.txt','txt')
    for offset in range(1, 2):
        result_html = my_spider.get_onePage('')
        # result_list = my_spider.parse_onePage(result_html)
        # my_spider.save(result_list)
