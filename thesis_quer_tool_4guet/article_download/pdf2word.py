# !/usr/bin/python
# -*- coding: utf-8 -*-
# 这里要注意中文编码格式是utf-8
import sys
import importlib
"""That's pdf2word.py by 1hz  """
# importlib.reload(sys)
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


# 封装成pdf2word类
# 这里主要使用2个库，你只需要下载pdfminer3k和python-docx 不同版本的pdfminer会存在依赖包互斥和覆盖，使用者需要按照要求进行环境配置


# 解析pdf文件函数
class pdf2word:

    def __init__(self, pdf_path, doc_path):
        self.pdf_path = pdf_path
        self.doc_path = doc_path

    def do(self):
        fp = open(self.pdf_path, 'rb')  # 以二进制只读模式打开
        # 用文件对象来创建一个pdf文档分析器
        parser = PDFParser(fp)
        # 创建一个PDF文档
        doc = PDFDocument()
        # 连接分析器 与文档对象
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize()
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed  # 判断是否提供txt转换
        else:
            # 创建PDf 资源管理器 以此管理共享资源
            rsrcmgr = PDFResourceManager()
            # 创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr, laparams=laparams)
            # 创建一个PDF解释器对象
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            # 用来计数页面，图片，曲线，figure，水平文本框等对象的数量
            num_page, num_image, num_curve, num_figure, num_TextBoxHorizontal = 0, 0, 0, 0, 0

            # 循环遍历列表，每次处理一个page的内容
            for page in doc.get_pages():  # doc.get_pages() 获取page列表
                num_page += 1  # 页面增一
                interpreter.process_page(page)
                # 接受该页面的LTPage对象
                layout = device.get_result()
                for x in layout:
                    if isinstance(x, LTImage):  # 图片对象
                        num_image += 1
                    if isinstance(x, LTCurve):  # 曲线对象
                        num_curve += 1
                    if isinstance(x, LTFigure):  # figure对象
                        num_figure += 1
                    if isinstance(x, LTTextBoxHorizontal):  # 获取文本内容
                        num_TextBoxHorizontal += 1  # 水平文本框对象增一
                        # 保存文本内容
                        with open(self.doc_path, 'a', encoding='utf-8') as f:  # 输入你想生成的doc文件名
                            results = x.get_text()
                            f.write(results)
                            f.write('\n')
            print('对象数量：\n', '页面数：%s\n' % num_page, '图片数：%s\n' % num_image, '曲线数：%s\n' % num_curve, '水平文本框：%s\n'
                  % num_TextBoxHorizontal)
