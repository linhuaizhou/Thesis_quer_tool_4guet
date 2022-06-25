"""That's download_from_elsevier in solo mode  by 1hz  """
import os

import openpyxl
import requests

from article_download.scihub import SciHub
from article_download.pdf2word import pdf2word as p2w
from win32com import client as wc


class download_from_elsevier:
    def __init__(self, doi, txt_out_path):
        self.doi = doi
        self.txt_out_path = txt_out_path

    def do(self):
        header = {'Accept': 'text/plain', 'CR-TDM-Rate-Limit': '4000', 'CR-TDM-Rate-Limit-Remaining': '76',
                  'CR-TDM-Rate-Limit-Reset': '1378072800'}

        url_publisher = "https://api.elsevier.com/content/article/doi/"  # 如果获取全文的话，将abstract替换成article
        APIKey = "爱思唯尔开发者API"  # 爱思唯尔开发者API，自己申请
        arformat = "text/plain"  # text/xml,text/plain

        url = url_publisher + self.doi + "?" + APIKey + "&httpAccept=" + arformat
        r = requests.get(url, headers=header)
        content = r.content.decode()
        path = self.txt_out_path + '/' + 'solo.txt'
        # print(path)
        f = open(path, 'w', encoding='utf-8')
        f.write(content)
        f.close()

        print("Solo_txt is finish!Save at location " + str(path))
