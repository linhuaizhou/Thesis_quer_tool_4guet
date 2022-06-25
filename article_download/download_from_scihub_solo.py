"""That's download_from_scihub in solo mode  by 1hz  """
import os

import openpyxl

from article_download.scihub import SciHub
from article_download.pdf2word import pdf2word as p2w
from win32com import client as wc


class download_from_scihub:
    def __init__(self, doi, pdf_out_path, word_out_path, txt_out_path):
        self.doi = doi
        self.pdf_out_path = pdf_out_path
        self.word_out_path = word_out_path
        self.txt_out_path = txt_out_path

    def Translate(self, input, output):
        # 转换
        wordapp = wc.Dispatch('kwps.Application') # 此处调用WPS解决一些编码问题

        doc = wordapp.Documents.Open(input)
        # 为了让python可以在后续操作中r方式读取txt和不产生乱码，参数为4
        doc.SaveAs(output, 4)
        doc.Close()

    def do(self):
        sh = SciHub()
        result = sh.download(self.doi, path=self.pdf_out_path + "/" + 'solo.pdf')
        print("Solo_pdf is finish!Save at location " + str(self.pdf_out_path) + "/" + 'solo.pdf')
        pdf_path = self.pdf_out_path + "/" + 'solo.pdf'
        doc_path = self.word_out_path + "/" + "solo.docx"
        p1 = p2w(pdf_path, doc_path)
        p2 = p1.do()
        input_file = doc_path
        output_file = self.txt_out_path + "/" + "solo.txt"
        self.Translate(input_file, output_file)
        print(
            "Solo_word and Solo_txt are finish!Save at location " + input_file + " and " + output_file)
