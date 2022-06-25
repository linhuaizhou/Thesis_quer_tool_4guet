"""That's cha_bd_mainword_search_txt.py by 1hz  """
import requests
from bs4 import BeautifulSoup
import urllib


# 该类是对百度学术指定关键词返回内容做txt输出,保存到指定的txt文档并输出，search为待搜索关键词，page_number为可搜索的页数，一般一页10个,此处指定了输出txt，当然也可以按需求改#
class bd_main_word_search:
    def __init__(self, search, page_number):
        self.search = search
        self.page_number = page_number

    def do_search(self):
        kwen = self.search.encode('utf-8')  # 将汉字，用utf格式编码，赋值给gbkkw
        f = open('result_mainword_search.txt', 'w', encoding='utf-8')  # 创建txt格式文件，方便等会存储
        # 添加请求头，模拟浏览器正常访问，避免被反爬虫
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        for x in range(self.page_number):  # 想要爬取多少页数据
            url = 'http://xueshu.baidu.com/s?wd=' + urllib.request.quote(kwen) + '&pn=' + str(
                x * 10) + '&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&sc_hit=1'
            res = requests.get(url, headers=headers)
            print(res.status_code)  # 查看是否能获取数据
            bs1 = BeautifulSoup(res.text, 'html.parser')  # 解析数据
            list_titles = bs1.find_all('div', class_="sc_content")
            for i in list_titles:
                title = i.find('h3', class_="t c_font").text  # 爬到标题
                print(title)
                f.write("题目：" + title.strip())
                f.write('\n')
                # 获取文章跳转链接
                half_link = i.find('h3', class_="t c_font").find('a')['href']
                wholelink = str(half_link)
                print(wholelink)
                f.write("链接： " + wholelink)
                f.write('\r\n')
                re = requests.get(wholelink, headers=headers)  # 爬取该网站内容
                if re.status_code == 200:
                    bs2 = BeautifulSoup(re.text, 'html.parser')  # 解析该网站内容
                    infos = bs2.find('div', class_="main-info").find('div', class_="c_content")
                    papers = bs2.find('div', class_="paper_src_content")
                    try:
                        if infos.find('div', class_="author_wr") is not None:
                            author = infos.find('div', class_="author_wr").find('p', class_="author_text").text.strip()
                            print(author)
                            f.write("作者： " + author)
                            f.write('\r\n')
                        if infos.find('div', class_="abstract_wr") is not None:
                            abstract = infos.find('div', class_="abstract_wr").find('p', class_="abstract").text.strip()
                            print(abstract)
                            f.write("摘要： " + abstract)
                            f.write('\r\n')
                        if infos.find('div', class_="kw_wr") is not None:
                            keywords = infos.find('div', class_="kw_wr").find('p', class_="kw_main").text.strip()
                            print(keywords)
                            f.write("关键词： " + keywords)
                            f.write('\r\n')
                        if infos.find('div', class_="year_wr") is not None:
                            year = infos.find('div', class_="year_wr").find('p', class_="kw_main").text.strip()
                            print(year)
                            f.write("发表时间： " + year)
                            f.write('\r\n')
                        if infos.find('div', class_="doi_wr") is not None:
                            doi = infos.find('div', class_="doi_wr").find('p', class_="kw_main").text.strip()
                            print(doi)
                            f.write("DOI： " + doi)
                            f.write('\r\n')
                        if infos.find('div', class_="ref_wr") is not None:
                            ref = infos.find('div', class_="ref_wr").find('p', class_="ref-wr-num").text.strip()
                            print(ref)
                            f.write("被引量： " + ref)
                            f.write('\r\n')
                        else:
                            print('该文章无该内容, 详情请查看官网：' + wholelink + '\n')
                            f.write('该文章无该内容, 详情请查看官网：' + wholelink)
                            f.write('\r\n')
                    except:
                        print("error!" + '\n')
                        f.write('error!')
                        f.write('\r\n')

                else:
                    print('该文章无链接')
                    f.write('该文章无链接')
                    f.write('\r\n')

        f.close()
