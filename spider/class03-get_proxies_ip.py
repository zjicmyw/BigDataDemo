import requests
from pyquery import PyQuery as pq
import os
import time
import telnetlib

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}


class MyIPSpider(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def get_onePage(self, offset):
        get_url = self.base_url.format(offset)
        response = requests.get(url=get_url, headers=headers)
        if response.status_code == 200:
            return response.content.decode('UTF-8')
        else:
            return None

    def parse_onePage(self, html, url_index):
        pq_html = pq(html)
        list_IP = []
        if url_index == 0:
            # https://www.kuaidaili.com
            tr = pq_html('.table-striped tbody tr').items()
            for item in tr:
                ip = item.find('td').eq(0).html()
                port = item.find('td').eq(1).html()
                if test_ip(ip, port):
                    list_IP.append(ip+':'+port)
        elif url_index == 1:
            # https://ip.ihuan.me/
            tr = pq_html('.table-bordered tbody tr').items()
            for item in tr:
                str_ip = item.find('td').eq(0).find('a').html()
                ip = str_ip.split('/>')
                port = item.find('td').eq(1).html()
                http = 'http://' if item.find('td').eq(
                    4).html() == '不支持' else 'https://'
                # print(http+ip[1]+':'+port)
                if test_ip(ip[1], port):
                    list_IP.append(http+ip[1]+':'+port)
        return list_IP

    def save_txt(self, list_IP, save_path):
        for item in list_IP:
            with open(save_path, 'a', encoding='utf-8') as f:
                f.write(item + '\n')


def dir_exist(dir_exist):
    if not os.path.exists(dir_exist):
        os.makedirs(dir_exist)


def file_exist(file_path):
    with open(file_path, 'w') as f:
        if not os.path.exists(file_path):
            pass
        else:
            f.write('')


def test_ip(ip, port):
    try:
        telnetlib.Telnet(ip, port, timeout=2)
        return True
    except:
        print("{}:{}无效".format(ip, port))
        return False


if __name__ == '__main__':
    cache_path = 'cache/'
    dir_exist(cache_path)
    file_path = 'cache/ip.txt'
    file_exist(file_path)
    base_url = ['https://www.kuaidaili.com/free/inha/{}/',
                'https://ip.ihuan.me/']
    url_index = 1
    my_spider = MyIPSpider(base_url[url_index])
    if url_index == 0:
        for offset in range(1, 3):
            result_html = my_spider.get_onePage(offset)
            list_IP = my_spider.parse_onePage(result_html)
            print(list_IP)
            my_spider.save_txt(list_IP, file_path)
            time.sleep(2)
    elif url_index == 1:
        result_html = my_spider.get_onePage('')
        list_IP = my_spider.parse_onePage(result_html, url_index)
        print(list_IP)
        my_spider.save_txt(list_IP, file_path)


# 测试：
    # proxy = {
    #     'http': 'http://174.138.42.112:8080',
    #     'https': 'https://134.122.31.84:8080',
    # }

    # p = requests.get('http://icanhazip.com', headers=headers, proxies=proxy)
    # print(p.text)
