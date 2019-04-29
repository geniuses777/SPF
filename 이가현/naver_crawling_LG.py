import urllib.request
import bs4

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=lg"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

LG_title_fir = bs_obj.find("ul", {"class":"type01"})
LG_title_sec = LG_title_fir.findAll("dl")


for dl in LG_title_sec:
    LG_title_th = dl.find("a", {"class":"_sp_each_title"})
    print(LG_title_th.text)







