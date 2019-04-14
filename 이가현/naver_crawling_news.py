import urllib.request
import bs4

url = "http://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

hdline_article_list = bs_obj.find("ul", {"class":"hdline_article_list"})
lis = hdline_article_list.findAll("li")

for li in lis:
    a_tag = li.find("a")
    print(a_tag.text)