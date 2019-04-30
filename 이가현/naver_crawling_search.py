import urllib.request
import urllib.parse
import bs4

def crawler(maxpage):
    page = 1
    maxpage_t = (int(maxpage)-1)*10+1

    name = input("기업명 : ");
    # 기업명을 입력받음
    while page <= maxpage_t:
        url1 = "https://search.naver.com/search.naver?&where=news&query="
        url2 = urllib.parse.quote_plus(name) # 한글 기업명 입력시 유니코드로 바꿔줌
        url3 = "&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=" + str(page) + "&refresh_start=0"

        FullURL = url1 + url2 + url3
        html = urllib.request.urlopen(FullURL)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LG_title_fir = bs_obj.find("ul", {"class": "type01"})
        LG_title_sec = LG_title_fir.findAll("dl")

        for dl in LG_title_sec:
            LG_title_th = dl.find("a", {"class": "_sp_each_title"})
            print(LG_title_th.text)

        page = page + 10

crawler(2)
# 원하는 페이지 수 만큼 지정하면됨. 현재 2페이지까지 출력