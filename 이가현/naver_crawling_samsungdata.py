import urllib.request
import urllib.parse
import bs4

url_naver = "https://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url_naver)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

samsung_first = bs_obj.find("table", {"class": "no_info"})
samsung_sec = samsung_first.findAll("span", {"class": "blind"})

samsung_yesterday = str(samsung_sec[0].text)
samsung_high = str(samsung_sec[1].text)
samsung_volum = str(samsung_sec[3].text)
samsung_siga = str(samsung_sec[4].text)
samsung_low = str(samsung_sec[5].text)
samsung_value = str(samsung_sec[6].text)

print("전일 : " + samsung_yesterday)
print("시가 : " + samsung_siga)
print("고가 : " + samsung_high)
print("저가 : " + samsung_low)
print("거래량 : " + samsung_volum)
print("거래대금 : " + samsung_value + "백만")



