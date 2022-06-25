"""That's cha_bd_assigned_paper_return_doi.py by 1hz  """
import requests
from bs4 import BeautifulSoup
import urllib


# 该类是对百度学术指定论文名称爬取，返回DOI号并print#
class bd_assigned_paper_search_doi:
    def __init__(self, search, list_doi):
        self.search = search
        self.list_doi = list_doi

    def do_search(self):

        kwen = self.search.encode('utf-8')  # 将汉字，用utf格式编码，赋值给gbkkw
        headers = {'Accept': 'text/plain', 'CR-TDM-Rate-Limit': '4000', 'CR-TDM-Rate-Limit-Remaining': '76',
                   'CR-TDM-Rate-Limit-Reset': '1378072800'}
        for x in range(1):  # 想要爬取多少页数据
            url = 'http://xueshu.baidu.com/s?wd=' + urllib.request.quote(kwen) + '&pn=' + str(
                x * 10) + '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1'
            res = requests.get(url, headers=headers)
            # print(res.status_code)  # 查看是否能获取数据
            bs1 = BeautifulSoup(res.text, 'html.parser')  # 解析数据
            list_titles = bs1.find_all('div', class_="sc_content")

            try:
                count_1 = 0
                for i in list_titles:
                    title = i.find('h3', class_="t c_font").text  # 爬到标题
                    print(title)
                    half_link = i.find('h3', class_="t c_font").find('a')['href']
                    wholelink = str(half_link)
                    re = requests.get(wholelink, headers=headers)  # 爬取该网站内容
                    if re.status_code == 200:
                        bs2 = BeautifulSoup(re.text, 'html.parser')  # 解析该网站内容
                        infos = bs2.find('div', class_="main-info").find('div', class_="c_content")
                        papers = bs2.find('div', class_="paper_src_content")
                        if infos.find('div', class_="doi_wr") is not None:
                            doi = infos.find('div', class_="doi_wr").find('p', class_="kw_main").text.strip()
                            print(doi)
                            if count_1 == 0:
                                self.list_doi.append(doi)
                                count_1 += 1
                                flag = True
                                break
            except:
                print("error")
        print(self.list_doi)
