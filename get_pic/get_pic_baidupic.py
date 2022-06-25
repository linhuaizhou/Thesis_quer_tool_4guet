"""That's get_pic_from_baidu.py  by 1hz  """
import requests
import os


class get_pic_from_baidu:
    def __init__(self, keyword, pages, localPath):
        self.keyword = keyword
        self.pages = pages
        self.localPath = localPath

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def getManyPages(self, keyword, pages):
        params = []
        for i in range(0, 30 * pages + 30, 30):
            params.append({
                'tn': 'resultjson_com',
                'ipn': 'rj',
                'ct': 201326592,
                'is': '',
                'fp': 'result',
                'queryWord': keyword,
                'cl': 2,
                'lm': -1,
                'ie': 'utf-8',
                'oe': 'utf-8',
                'adpicid': '',
                'st': -1,
                'z': '',
                'ic': 0,
                'word': keyword,
                's': '',
                'se': '',
                'tab': '',
                'width': '',
                'height': '',
                'face': 0,
                'istype': 2,
                'qc': '',
                'nc': 1,
                'fr': '',
                'pn': i,
                'rn': 30,
                'gsm': '1e',
                '1488942260214': ''
            })

        url = 'https://image.baidu.com/search/index'
        urls = []
        for i in params:
            try:

                urls.append(requests.get(url, headers=self.headers, params=i).json().get('data'))
            except:
                pass
        print(urls)
        return urls

    def getImg(self,dataList, localPath):
        if not os.path.exists(localPath):  # 新建文件夹
            os.mkdir(localPath)

        x = 0
        for list in dataList:
            if list:
                for i in list:
                    if i.get('thumbURL') != None:
                        print('正在下载：%s' % i.get('thumbURL'))
                        ir = requests.get(i.get('thumbURL'))
                        open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                        x += 1
                    else:
                        print('图片链接不存在')

    def do(self):
        dataList = self.getManyPages(self.keyword, self.pages)  # 参数1:关键字，参数2:要下载的页数
        self.getImg(dataList, self.localPath)  # 参数2:指定保存的路径
