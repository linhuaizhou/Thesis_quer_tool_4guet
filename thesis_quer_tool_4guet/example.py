"""That's example by 1hz  """
from get_pic import get_pic_baidupic
from search import cha_bd_mainword_search_txt
from search import cha_bd_mainword_search_excel
from search import cha_bd_assigned_paper_return_doi
from search import cha_bd_assigned_paper_return_all
from search import cha_bd_title_list_2_doi_list
from article_download import download_from_elsevier_multy
from article_download import download_from_scihub_multy
from article_download import download_from_scihub_solo
from article_download import download_from_elsevier_solo

# c = cha_bd_mainword_search_txt.bd_main_word_search("The effect of V, VCl3 and VC catalysts on the MgH2 hydrogen sorption properties", 1)
# c.do_search()
# gpb = get_pic_baidupic.get_pic_from_baidu("布匹", 1, "img/")
# gpb.do()
# list_doi = []
# c = cha_bd_assigned_paper_return_doi.bd_assigned_paper_search_doi(
# "The effect of V, VCl3 and VC catalysts on the MgH2 hydrogen sorption properties", list_doi)
# c.do_search()
# print(list_doi)
# c = cha_bd_assigned_paper_return_all.bd_assigned_paper_search("The effect of V, VCl3 and VC catalysts on the MgH2 hydrogen sorption properties")
# c.do_search()
# c = cha_bd_mainword_search_excel.bd_main_word_search("The effect of V, VCl3 and VC catalysts on the MgH2 hydrogen sorption properties", 1, "result.xlsx")
# c.do_search()
# c = cha_bd_title_list_2_doi_list.title2doi(r"do_test.xlsx", 2, 2, 2, 3)
# c.do()
# d = download_from_elsevier_multy.download_from_elsevier(r"output.xlsx", "Sheet1","txt_out")
# d.do()
# d = download_from_scihub_multy.download_from_scihub(r"output.xlsx", "Sheet1",r"word_out",r"txt_out", 2, 2)
# d.do()
# d = download_from_scihub_solo.download_from_scihub("10.1016/j.jallcom.2012.12.131",r"pdf_out", r"word_out",
# r"D:\1_研究生相关文件\26_test\1_test_all\in\txt_out")
# d.do()
# d = download_from_elsevier_solo.download_from_elsevier("10.1016/j.jallcom.2012.12.131",r"txt_out_solo")
# d.do()
