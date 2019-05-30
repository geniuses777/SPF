import pymysql.cursors
import urllib.request
import urllib.parse
import bs4
from datetime import datetime
from time import sleep

while True :

    conn = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777', password='stock7840', db='geniuses777', charset='utf8')

    now = datetime.now()

    time = '%s-%s-%s %s:%s:%s'% (now.year, now.month, now.day, now.hour, now.minute, now.second)

    if now.hour >= 9 and now.hour < 16 :
        # CJ
        url_naver = "https://finance.naver.com/item/main.nhn?code=001040"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        CJ_data = bs_obj.find("div", {"class": "today"})
        CJ_data_first = CJ_data.find("span", {"class": "blind"})
        CJ_data_realTime = CJ_data_first.text  # 실시간 가격
        print(CJ_data_realTime)

        CJ_data_first = CJ_data.find("p", {"class": "no_exday"})
        CJ_data_first_str = str(CJ_data_first)

        if CJ_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            CJ_data_updown_fir = CJ_data_first.findAll("span", {"class": "blind"})
            CJ_data_updown_sec = CJ_data_updown_fir[0].text
            CJ_data_percent = "-" + CJ_data_updown_fir[1].text + "%"  # 전일대비
            CJ_data_updown = "-" + CJ_data_updown_sec  # 퍼센트
            print(CJ_data_updown)
            print(CJ_data_percent)


        else:  # 문자열에 no_up이 존재하면
            CJ_data_updown_fir = CJ_data_first.findAll("span", {"class": "blind"})
            CJ_data_updown_sec = CJ_data_updown_fir[0].text
            CJ_data_percent = "+" + CJ_data_updown_fir[1].text + "%"  # 전일대비
            CJ_data_updown = "+" + CJ_data_updown_sec  # 퍼센트
            print(CJ_data_updown)
            print(CJ_data_percent)

        CJ_first = bs_obj.find("table", {"class": "no_info"})
        CJ_sec = CJ_first.findAll("span", {"class": "blind"})

        CJ_yesterday = str(CJ_sec[0].text)
        CJ_high = str(CJ_sec[1].text)
        CJ_volum = str(CJ_sec[3].text)
        CJ_siga = str(CJ_sec[4].text)
        CJ_low = str(CJ_sec[5].text)
        CJ_value = str(CJ_sec[6].text) + "백만"  # 수정

        # LG
        url_naver = "https://finance.naver.com/item/main.nhn?code=003550"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LG_data = bs_obj.find("div", {"class": "today"})
        LG_data_first = LG_data.find("span", {"class": "blind"})
        LG_data_realTime = LG_data_first.text  # 실시간 가격
        print(LG_data_realTime)

        LG_data_first = LG_data.find("p", {"class": "no_exday"})
        LG_data_first_str = str(LG_data_first)
        # print(LG_data_first)

        if LG_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            LG_data_updown_fir = LG_data_first.findAll("span", {"class": "blind"})
            LG_data_updown_sec = LG_data_updown_fir[0].text
            LG_data_percent = "-" + LG_data_updown_fir[1].text + "%"
            LG_data_updown = "-" + LG_data_updown_sec
            print(LG_data_updown)
            print(LG_data_percent)

        else:  # 문자열에 no_up이 존재하면
            LG_data_updown_fir = LG_data_first.findAll("span", {"class": "blind"})
            LG_data_updown_sec = LG_data_updown_fir[0].text
            LG_data_percent = "+" + LG_data_updown_fir[1].text + "%"
            LG_data_updown = "+" + LG_data_updown_sec
            print(LG_data_updown)
            print(LG_data_percent)

        LG_first = bs_obj.find("table", {"class": "no_info"})
        LG_sec = LG_first.findAll("span", {"class": "blind"})

        LG_yesterday = str(LG_sec[0].text)
        LG_high = str(LG_sec[1].text)
        LG_volum = str(LG_sec[3].text)
        LG_siga = str(LG_sec[4].text)
        LG_low = str(LG_sec[5].text)
        LG_value = str(LG_sec[6].text) + "백만"  # 수정

        # SK
        url_naver = "https://finance.naver.com/item/main.nhn?code=034730"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        SK_data = bs_obj.find("div", {"class": "today"})
        SK_data_first = SK_data.find("span", {"class": "blind"})
        SK_data_realTime = SK_data_first.text  # 실시간 가격
        print(SK_data_realTime)

        SK_data_first = SK_data.find("p", {"class": "no_exday"})
        SK_data_first_str = str(SK_data_first)

        if SK_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            SK_data_updown_fir = SK_data_first.findAll("span", {"class": "blind"})
            SK_data_updown_sec = SK_data_updown_fir[0].text
            SK_data_percent = "-" + SK_data_updown_fir[1].text + "%"
            SK_data_updown = "-" + SK_data_updown_sec
            print(SK_data_updown)
            print(SK_data_percent)

        else:  # 문자열에 no_up이 존재하면
            SK_data_updown_fir = SK_data_first.findAll("span", {"class": "blind"})
            SK_data_updown_sec = SK_data_updown_fir[0].text
            SK_data_percent = "+" + SK_data_updown_fir[1].text + "%"
            SK_data_updown = "+" + SK_data_updown_sec
            print(SK_data_updown)
            print(SK_data_percent)

        SK_first = bs_obj.find("table", {"class": "no_info"})
        SK_sec = SK_first.findAll("span", {"class": "blind"})

        SK_yesterday = str(SK_sec[0].text)
        SK_high = str(SK_sec[1].text)
        SK_volum = str(SK_sec[3].text)
        SK_siga = str(SK_sec[4].text)
        SK_low = str(SK_sec[5].text)
        SK_value = str(SK_sec[6].text) + "백만"  # 수정

        # DOOSAN
        url_naver = "https://finance.naver.com/item/main.nhn?code=000150"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        DOOSAN_data = bs_obj.find("div", {"class": "today"})
        DOOSAN_data_first = DOOSAN_data.find("span", {"class": "blind"})
        DOOSAN_data_realTime = DOOSAN_data_first.text  # 실시간 가격
        print(DOOSAN_data_realTime)

        DOOSAN_data_first = DOOSAN_data.find("p", {"class": "no_exday"})
        DOOSAN_data_first_str = str(DOOSAN_data_first)

        if DOOSAN_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            DOOSAN_data_updown_fir = DOOSAN_data_first.findAll("span", {"class": "blind"})
            DOOSAN_data_updown_sec = DOOSAN_data_updown_fir[0].text
            DOOSAN_data_percent = "-" + DOOSAN_data_updown_fir[1].text + "%"
            DOOSAN_data_updown = "-" + DOOSAN_data_updown_sec
            print(DOOSAN_data_updown)
            print(DOOSAN_data_percent)

        else:  # 문자열에 no_up이 존재하면
            DOOSAN_data_updown_fir = DOOSAN_data_first.findAll("span", {"class": "blind"})
            DOOSAN_data_updown_sec = DOOSAN_data_updown_fir[0].text
            DOOSAN_data_percent = "+" + DOOSAN_data_updown_fir[1].text + "%"
            DOOSAN_data_updown = "+" + DOOSAN_data_updown_sec
            print(DOOSAN_data_updown)
            print(DOOSAN_data_percent)

        DOOSAN_first = bs_obj.find("table", {"class": "no_info"})
        DOOSAN_sec = DOOSAN_first.findAll("span", {"class": "blind"})

        DOOSAN_yesterday = str(DOOSAN_sec[0].text)
        DOOSAN_high = str(DOOSAN_sec[1].text)
        DOOSAN_volum = str(DOOSAN_sec[3].text)
        DOOSAN_siga = str(DOOSAN_sec[4].text)
        DOOSAN_low = str(DOOSAN_sec[5].text)
        DOOSAN_value = str(DOOSAN_sec[6].text) + "백만"  # 수정

        # SAMSUNG
        url_naver = "https://finance.naver.com/item/main.nhn?code=005930"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        samsung_data = bs_obj.find("div", {"class": "today"})
        samsung_data_first = samsung_data.find("span", {"class": "blind"})
        samsung_data_realTime = samsung_data_first.text  # 실시간 가격
        print(samsung_data_realTime)

        samsung_data_first = samsung_data.find("p", {"class": "no_exday"})
        samsung_data_first_str = str(samsung_data_first)

        if samsung_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            samsung_data_updown_fir = samsung_data_first.findAll("span", {"class": "blind"})
            samsung_data_updown_sec = samsung_data_updown_fir[0].text
            samsung_data_percent = "-" + samsung_data_updown_fir[1].text + "%"
            samsung_data_updown = "-" + samsung_data_updown_sec
            print(samsung_data_updown)
            print(samsung_data_percent)

        else:  # 문자열에 no_up이 존재하면
            samsung_data_updown_fir = samsung_data_first.findAll("span", {"class": "blind"})
            samsung_data_updown_sec = samsung_data_updown_fir[0].text
            samsung_data_percent = "+" + samsung_data_updown_fir[1].text + "%"
            samsung_data_updown = "+" + samsung_data_updown_sec
            print(samsung_data_updown)
            print(samsung_data_percent)

        samsung_first = bs_obj.find("table", {"class": "no_info"})
        samsung_sec = samsung_first.findAll("span", {"class": "blind"})

        samsung_yesterday = str(samsung_sec[0].text)
        samsung_high = str(samsung_sec[1].text)
        samsung_volum = str(samsung_sec[3].text)
        samsung_siga = str(samsung_sec[4].text)
        samsung_low = str(samsung_sec[5].text)
        samsung_value = str(samsung_sec[6].text) + "백만"  # 수정

        # ASIANA
        url_naver = "https://finance.naver.com/item/main.nhn?code=020560"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        ASIANA_data = bs_obj.find("div", {"class": "today"})
        ASIANA_data_first = ASIANA_data.find("span", {"class": "blind"})
        ASIANA_data_realTime = ASIANA_data_first.text  # 실시간 가격
        print(ASIANA_data_realTime)

        ASIANA_data_first = ASIANA_data.find("p", {"class": "no_exday"})
        ASIANA_data_first_str = str(ASIANA_data_first)

        if ASIANA_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            ASIANA_data_updown_fir = ASIANA_data_first.findAll("span", {"class": "blind"})
            ASIANA_data_updown_sec = ASIANA_data_updown_fir[0].text
            ASIANA_data_percent = "-" + ASIANA_data_updown_fir[1].text + "%"
            ASIANA_data_updown = "-" + ASIANA_data_updown_sec
            print(ASIANA_data_updown)
            print(ASIANA_data_percent)

        else:  # 문자열에 no_up이 존재하면
            ASIANA_data_updown_fir = ASIANA_data_first.findAll("span", {"class": "blind"})
            ASIANA_data_updown_sec = ASIANA_data_updown_fir[0].text
            ASIANA_data_percent = "+" + ASIANA_data_updown_fir[1].text + "%"
            ASIANA_data_updown = "+" + ASIANA_data_updown_sec
            print(ASIANA_data_updown)
            print(ASIANA_data_percent)

        ASIANA_first = bs_obj.find("table", {"class": "no_info"})
        ASIANA_sec = ASIANA_first.findAll("span", {"class": "blind"})

        ASIANA_yesterday = str(ASIANA_sec[0].text)
        ASIANA_high = str(ASIANA_sec[1].text)
        ASIANA_volum = str(ASIANA_sec[3].text)
        ASIANA_siga = str(ASIANA_sec[4].text)
        ASIANA_low = str(ASIANA_sec[5].text)
        ASIANA_value = str(ASIANA_sec[6].text) + "백만"  # 수정

        # KAKAO
        url_naver = "https://finance.naver.com/item/main.nhn?code=035720"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        KAKAO_data = bs_obj.find("div", {"class": "today"})
        KAKAO_data_first = KAKAO_data.find("span", {"class": "blind"})
        KAKAO_data_realTime = KAKAO_data_first.text  # 실시간 가격
        print(KAKAO_data_realTime)

        KAKAO_data_first = KAKAO_data.find("p", {"class": "no_exday"})
        KAKAO_data_first_str = str(KAKAO_data_first)

        if KAKAO_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            KAKAO_data_updown_fir = KAKAO_data_first.findAll("span", {"class": "blind"})
            KAKAO_data_updown_sec = KAKAO_data_updown_fir[0].text
            KAKAO_data_percent = "-" + KAKAO_data_updown_fir[1].text + "%"
            KAKAO_data_updown = "-" + KAKAO_data_updown_sec
            print(KAKAO_data_updown)
            print(KAKAO_data_percent)

        else:  # 문자열에 no_up이 존재하면
            KAKAO_data_updown_fir = KAKAO_data_first.findAll("span", {"class": "blind"})
            KAKAO_data_updown_sec = KAKAO_data_updown_fir[0].text
            KAKAO_data_percent = "+" + KAKAO_data_updown_fir[1].text + "%"
            KAKAO_data_updown = "+" + KAKAO_data_updown_sec
            print(KAKAO_data_updown)
            print(KAKAO_data_percent)

        KAKAO_first = bs_obj.find("table", {"class": "no_info"})
        KAKAO_sec = KAKAO_first.findAll("span", {"class": "blind"})

        KAKAO_yesterday = str(KAKAO_sec[0].text)
        KAKAO_high = str(KAKAO_sec[1].text)
        KAKAO_volum = str(KAKAO_sec[3].text)
        KAKAO_siga = str(KAKAO_sec[4].text)
        KAKAO_low = str(KAKAO_sec[5].text)
        KAKAO_value = str(KAKAO_sec[6].text) + "백만"  # 수정

        # JINRO
        url_naver = "https://finance.naver.com/item/main.nhn?code=000080"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        JINRO_data = bs_obj.find("div", {"class": "today"})
        JINRO_data_first = JINRO_data.find("span", {"class": "blind"})
        JINRO_data_realTime = JINRO_data_first.text  # 실시간 가격
        print(JINRO_data_realTime)

        JINRO_data_first = JINRO_data.find("p", {"class": "no_exday"})
        JINRO_data_first_str = str(JINRO_data_first)

        if JINRO_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            JINRO_data_updown_fir = JINRO_data_first.findAll("span", {"class": "blind"})
            JINRO_data_updown_sec = JINRO_data_updown_fir[0].text
            JINRO_data_percent = "-" + JINRO_data_updown_fir[1].text + "%"
            JINRO_data_updown = "-" + JINRO_data_updown_sec
            print(JINRO_data_updown)
            print(JINRO_data_percent)

        else:  # 문자열에 no_up이 존재하면
            JINRO_data_updown_fir = JINRO_data_first.findAll("span", {"class": "blind"})
            JINRO_data_updown_sec = JINRO_data_updown_fir[0].text
            JINRO_data_percent = "+" + JINRO_data_updown_fir[1].text + "%"
            JINRO_data_updown = "+" + JINRO_data_updown_sec
            print(JINRO_data_updown)
            print(JINRO_data_percent)

        JINRO_first = bs_obj.find("table", {"class": "no_info"})
        JINRO_sec = JINRO_first.findAll("span", {"class": "blind"})

        JINRO_yesterday = str(JINRO_sec[0].text)
        JINRO_high = str(JINRO_sec[1].text)
        JINRO_volum = str(JINRO_sec[3].text)
        JINRO_siga = str(JINRO_sec[4].text)
        JINRO_low = str(JINRO_sec[5].text)
        JINRO_value = str(JINRO_sec[6].text) + "백만"  # 수정

        # HANWHA
        url_naver = "https://finance.naver.com/item/main.nhn?code=000880"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HANWHA_data = bs_obj.find("div", {"class": "today"})
        HANWHA_data_first = HANWHA_data.find("span", {"class": "blind"})
        HANWHA_data_realTime = HANWHA_data_first.text  # 실시간 가격
        print(HANWHA_data_realTime)

        HANWHA_data_first = HANWHA_data.find("p", {"class": "no_exday"})
        HANWHA_data_first_str = str(HANWHA_data_first)

        if HANWHA_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            HANWHA_data_updown_fir = HANWHA_data_first.findAll("span", {"class": "blind"})
            HANWHA_data_updown_sec = HANWHA_data_updown_fir[0].text
            HANWHA_data_percent = "-" + HANWHA_data_updown_fir[1].text + "%"
            HANWHA_data_updown = "-" + HANWHA_data_updown_sec
            print(HANWHA_data_updown)
            print(HANWHA_data_percent)

        else:  # 문자열에 no_up이 존재하면
            HANWHA_data_updown_fir = HANWHA_data_first.findAll("span", {"class": "blind"})
            HANWHA_data_updown_sec = HANWHA_data_updown_fir[0].text
            HANWHA_data_percent = "+" + HANWHA_data_updown_fir[1].text + "%"
            HANWHA_data_updown = "+" + HANWHA_data_updown_sec
            print(HANWHA_data_updown)
            print(HANWHA_data_percent)

        HANWHA_first = bs_obj.find("table", {"class": "no_info"})
        HANWHA_sec = HANWHA_first.findAll("span", {"class": "blind"})

        HANWHA_yesterday = str(HANWHA_sec[0].text)
        HANWHA_high = str(HANWHA_sec[1].text)
        HANWHA_volum = str(HANWHA_sec[3].text)
        HANWHA_siga = str(HANWHA_sec[4].text)
        HANWHA_low = str(HANWHA_sec[5].text)
        HANWHA_value = str(HANWHA_sec[6].text) + "백만"  # 수정

        # HYUNDAI
        url_naver = "https://finance.naver.com/item/main.nhn?code=005380"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HYUNDAI_data = bs_obj.find("div", {"class": "today"})
        HYUNDAI_data_first = HYUNDAI_data.find("span", {"class": "blind"})
        HYUNDAI_data_realTime = HYUNDAI_data_first.text  # 실시간 가격
        print(HYUNDAI_data_realTime)

        HYUNDAI_data_first = HYUNDAI_data.find("p", {"class": "no_exday"})
        HYUNDAI_data_first_str = str(HYUNDAI_data_first)

        if HYUNDAI_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            HYUNDAI_data_updown_fir = HYUNDAI_data_first.findAll("span", {"class": "blind"})
            HYUNDAI_data_updown_sec = HYUNDAI_data_updown_fir[0].text
            HYUNDAI_data_percent = "-" + HYUNDAI_data_updown_fir[1].text + "%"
            HYUNDAI_data_updown = "-" + HYUNDAI_data_updown_sec
            print(HYUNDAI_data_updown)
            print(HYUNDAI_data_percent)

        else:  # 문자열에 no_up이 존재하면
            HYUNDAI_data_updown_fir = HYUNDAI_data_first.findAll("span", {"class": "blind"})
            HYUNDAI_data_updown_sec = HYUNDAI_data_updown_fir[0].text
            HYUNDAI_data_percent = "+" + HYUNDAI_data_updown_fir[1].text + "%"
            HYUNDAI_data_updown = "+" + HYUNDAI_data_updown_sec
            print(HYUNDAI_data_updown)
            print(HYUNDAI_data_percent)

        HYUNDAI_first = bs_obj.find("table", {"class": "no_info"})
        HYUNDAI_sec = HYUNDAI_first.findAll("span", {"class": "blind"})

        HYUNDAI_yesterday = str(HYUNDAI_sec[0].text)
        HYUNDAI_high = str(HYUNDAI_sec[1].text)
        HYUNDAI_volum = str(HYUNDAI_sec[3].text)
        HYUNDAI_siga = str(HYUNDAI_sec[4].text)
        HYUNDAI_low = str(HYUNDAI_sec[5].text)
        HYUNDAI_value = str(HYUNDAI_sec[6].text) + "백만"  # 수정

        # NAVER
        url_naver = "https://finance.naver.com/item/main.nhn?code=035420"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        NAVER_data = bs_obj.find("div", {"class": "today"})
        NAVER_data_first = NAVER_data.find("span", {"class": "blind"})
        NAVER_data_realTime = NAVER_data_first.text  # 실시간 가격
        print(NAVER_data_realTime)


        NAVER_data_first = NAVER_data.find("p", {"class": "no_exday"})
        NAVER_data_first_str = str(NAVER_data_first)

        if NAVER_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            NAVER_data_updown_fir = NAVER_data_first.findAll("span", {"class": "blind"})
            NAVER_data_updown_sec = NAVER_data_updown_fir[0].text
            NAVER_data_percent = "-" + NAVER_data_updown_fir[1].text + "%"
            NAVER_data_updown = "-" + NAVER_data_updown_sec
            print(NAVER_data_updown)
            print(NAVER_data_percent)

        else:  # 문자열에 no_up이 존재하면
            NAVER_data_updown_fir = NAVER_data_first.findAll("span", {"class": "blind"})
            NAVER_data_updown_sec = NAVER_data_updown_fir[0].text
            NAVER_data_percent = "+" + NAVER_data_updown_fir[1].text + "%"
            NAVER_data_updown = "+" + NAVER_data_updown_sec
            print(NAVER_data_updown)
            print(NAVER_data_percent)

        NAVER_first = bs_obj.find("table", {"class": "no_info"})
        NAVER_sec = NAVER_first.findAll("span", {"class": "blind"})

        NAVER_yesterday = str(NAVER_sec[0].text)
        NAVER_high = str(NAVER_sec[1].text)
        NAVER_volum = str(NAVER_sec[3].text)
        NAVER_siga = str(NAVER_sec[4].text)
        NAVER_low = str(NAVER_sec[5].text)
        NAVER_value = str(NAVER_sec[6].text) + "백만"  # 수정

        #LGD
        url_naver = "https://finance.naver.com/item/main.nhn?code=034220"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LGD_data = bs_obj.find("div", {"class": "today"})
        LGD_data_first = LGD_data.find("span", {"class": "blind"})
        LGD_data_realTime = LGD_data_first.text  # 실시간 가격
        print(LGD_data_realTime)

        LGD_data_first = LGD_data.find("p", {"class": "no_exday"})
        LGD_data_first_str = str(LGD_data_first)

        if LGD_data_first_str.find("no_down") != -1:  # 문자열에 no_down이 존재하면
            LGD_data_updown_fir = LGD_data_first.findAll("span", {"class": "blind"})
            LGD_data_updown_sec = LGD_data_updown_fir[0].text
            LGD_data_percent = "-" + LGD_data_updown_fir[1].text + "%"
            LGD_data_updown = "-" + LGD_data_updown_sec
            print(LGD_data_updown)
            print(LGD_data_percent)

        else:  # 문자열에 no_up이 존재하면
            LGD_data_updown_fir = LGD_data_first.findAll("span", {"class": "blind"})
            LGD_data_updown_sec = LGD_data_updown_fir[0].text
            LGD_data_percent = "+" + LGD_data_updown_fir[1].text + "%"
            LGD_data_updown = "+" + LGD_data_updown_sec
            print(LGD_data_updown)
            print(LGD_data_percent)

        LGD_first = bs_obj.find("table", {"class": "no_info"})
        LGD_sec = LGD_first.findAll("span", {"class": "blind"})

        LGD_yesterday = str(LGD_sec[0].text)
        LGD_high = str(LGD_sec[1].text)
        LGD_volum = str(LGD_sec[3].text)
        LGD_siga = str(LGD_sec[4].text)
        LGD_low = str(LGD_sec[5].text)
        LGD_value = str(LGD_sec[6].text) + "백만"  # 수정

        try:
            with conn.cursor() as cursor:
                # CJ 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_yesterday, 'CJ'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_siga, 'CJ'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_high, 'CJ'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_low, 'CJ'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_volum, 'CJ'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_value, 'CJ'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_data_realTime, 'CJ'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_data_updown, 'CJ'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (CJ_data_percent, 'CJ'))

                # LG 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_yesterday, 'LG'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_siga, 'LG'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_high, 'LG'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_low, 'LG'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_volum, 'LG'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_value, 'LG'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_data_realTime, 'LG'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_data_updown, 'LG'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (LG_data_percent, 'LG'))

                # SK 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_yesterday, 'SK'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_siga, 'SK'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_high, 'SK'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_low, 'SK'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_volum, 'SK'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_value, 'SK'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_data_realTime, 'SK'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_data_updown, 'SK'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (SK_data_percent, 'SK'))

                # DOOSAN 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_yesterday, '두산'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_siga, '두산'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_high, '두산'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_low, '두산'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_volum, '두산'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_value, '두산'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_data_realTime, '두산'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_data_updown, '두산'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (DOOSAN_data_percent, '두산'))

                # SAMSUNG 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_yesterday, '삼성'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_siga, '삼성'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_high, '삼성'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_low, '삼성'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_volum, '삼성'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_value, '삼성'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_data_realTime, '삼성'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_data_updown, '삼성'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (samsung_data_percent, '삼성'))

                # ASIANA 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_yesterday, '아시아나항공'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_siga, '아시아나항공'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_high, '아시아나항공'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_low, '아시아나항공'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_volum, '아시아나항공'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_value, '아시아나항공'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_data_realTime, '아시아나항공'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_data_updown, '아시아나항공'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (ASIANA_data_percent, '아시아나항공'))

                # KAKAO 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_yesterday, '카카오'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_siga, '카카오'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_high, '카카오'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_low, '카카오'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_volum, '카카오'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_value, '카카오'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_data_realTime, '카카오'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_data_updown, '카카오'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (KAKAO_data_percent, '카카오'))

                # HANWHA 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_yesterday, '한화'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_siga, '한화'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_high, '한화'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_low, '한화'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_volum, '한화'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_value, '한화'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_data_realTime, '한화'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_data_updown, '한화'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (HANWHA_data_percent, '한화'))

                # HYUNDAI 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_yesterday, '현대'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_siga, '현대'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_high, '현대'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_low, '현대'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_volum, '현대'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_value, '현대'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_data_realTime, '현대'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_data_updown, '현대'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (HYUNDAI_data_percent, '현대'))

                # JINRO 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_yesterday, '하이트진로'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_siga, '하이트진로'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_high, '하이트진로'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_low, '하이트진로'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_volum, '하이트진로'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_value, '하이트진로'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_data_realTime, '하이트진로'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_data_updown, '하이트진로'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (JINRO_data_percent, '하이트진로'))

                # NAVER 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_yesterday, '네이버'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_siga, '네이버'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_high, '네이버'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_low, '네이버'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_volum, '네이버'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_value, '네이버'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_data_realTime, '네이버'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_data_updown, '네이버'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (NAVER_data_percent, '네이버'))

                # LGD 디비넣기
                sql = 'UPDATE stockdata SET yesterday = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_yesterday, 'LGD'))
                sql = 'UPDATE stockdata SET siga = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_siga, 'LGD'))
                sql = 'UPDATE stockdata SET high = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_high, 'LGD'))
                sql = 'UPDATE stockdata SET low = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_low, 'LGD'))
                sql = 'UPDATE stockdata SET volum = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_volum, 'LGD'))
                sql = 'UPDATE stockdata SET value = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_value, 'LGD'))
                sql = 'UPDATE stockdata SET today = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_data_realTime, 'LGD'))
                sql = 'UPDATE stockdata SET updown = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_data_updown, 'LGD'))
                sql = 'UPDATE stockdata SET percent = %s WHERE company_name = %s'
                cursor.execute(sql, (LGD_data_percent, 'LGD'))

            conn.commit()

        finally:
            conn.close()

        sleep(60)

    else :
        sleep(600)