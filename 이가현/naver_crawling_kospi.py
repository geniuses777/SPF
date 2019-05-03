import urllib.request
import urllib.parse
import bs4

def kospi() :
    kospi_first = bs_obj.find("div", {"class": "heading_area"})
    # print(kospi_first)
    kospi = kospi_first.find("span", {"class": "num"})  # 실시간 코스피값
    kospi_updown_data = kospi_first.find("span", {"class": "num2"})  # 전일대비 상승,하락값
    kospi_percent = kospi_first.find("span", {"class": "num3"})  # 전일대비 상승하락율

    kospi_plusminus = kospi_percent.find("span", {"class": "blind"})
    kospi_plusminus_data = str(kospi_plusminus.text)

    if kospi_plusminus_data == "+":
        kospi_updown_plusminus = "상승"
    else:
        kospi_updown_plusminus = "하락"

    print("코스피 : " + kospi.text + " / " + kospi_updown_data.text + " " + kospi_updown_plusminus + " / " + kospi_percent.text)

def kosdaq() :
    kosdaq_first = bs_obj.find("div", {"class": "kosdaq_area group_quot"})
    # print(kospi_first)
    kosdaq = kosdaq_first.find("span", {"class": "num"})  # 실시간 코스닥값
    kosdaq_updown_data = kosdaq_first.find("span", {"class": "num2"})  # 전일대비 상승,하락값
    kosdaq_percent = kosdaq_first.find("span", {"class": "num3"})  # 전일대비 상승하락율

    kosdaq_plusminus = kosdaq_percent.find("span", {"class": "blind"})
    kosdaq_plusminus_data = str(kosdaq_plusminus.text)

    if kosdaq_plusminus_data == "+":
        kosdaq_updown_plusminus = "상승"
    else:
        kosdaq_updown_plusminus = "하락"

    print("코스닥 : " + kosdaq.text + " / " + kosdaq_updown_data.text + " " + kosdaq_updown_plusminus + " / " + kosdaq_percent.text)


url = "https://finance.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html, "html.parser")

kospi()
kosdaq()
