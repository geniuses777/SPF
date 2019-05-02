import urllib.request
import urllib.parse
import bs4

def yesterday() :
    samsung_yesterday_first = bs_obj.find("table", {"class": "no_info"})
    #print(samsung_yesterday_first)
    samsung_yesterday_sec = samsung_yesterday_first.find("td", {"class": "first"})
    #print(samsung_yesterday_sec)
    samsung_yesterday = samsung_yesterday_sec.find("span", {"class": "blind"})
    print("전일 : " + samsung_yesterday.text)

url = "https://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

yesterday()





