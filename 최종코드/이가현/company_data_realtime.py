import pymysql.cursors
import urllib.request
import urllib.parse
import bs4
from datetime import datetime
from time import sleep

while True :

    conn = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777', password='stock7840', db='geniuses777',
                           charset='utf8')

    now = datetime.now()

    # time = '%s-%s-%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    time = now.strftime('%Y-%m-%d %H:%M:%S')

    print(time)
    print(now.hour)

    if now.hour >= 9 and now.hour < 16 :

        # CJ
        url_naver = "https://finance.naver.com/item/main.nhn?code=001040"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        CJ_data = bs_obj.find("div", {"class": "today"})
        CJ_data_first = CJ_data.find("span", {"class": "blind"})
        CJ_data_realTime = CJ_data_first.text  # 실시간 가격
        CJ_data_realTime_result = CJ_data_realTime.replace(",", "")
        CJ_data_realTime_int = int(CJ_data_realTime_result)

        print(CJ_data_realTime_int)
        print(CJ_data_realTime)

        # LG
        url_naver = "https://finance.naver.com/item/main.nhn?code=003550"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LG_data = bs_obj.find("div", {"class": "today"})
        LG_data_first = LG_data.find("span", {"class": "blind"})
        LG_data_realTime = LG_data_first.text  # 실시간 가격
        LG_data_realTime_result = LG_data_realTime.replace(",", "")
        LG_data_realTime_int = int(LG_data_realTime_result)
        print(LG_data_realTime_int)
        print(LG_data_realTime)

        # SK
        url_naver = "https://finance.naver.com/item/main.nhn?code=034730"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        SK_data = bs_obj.find("div", {"class": "today"})
        SK_data_first = SK_data.find("span", {"class": "blind"})
        SK_data_realTime = SK_data_first.text  # 실시간 가격
        SK_data_realTime_result = SK_data_realTime.replace(",", "")
        SK_data_realTime_int = int(SK_data_realTime_result)
        print(SK_data_realTime_int)
        print(SK_data_realTime)

        # DOOSAN
        url_naver = "https://finance.naver.com/item/main.nhn?code=000150"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        DOOSAN_data = bs_obj.find("div", {"class": "today"})
        DOOSAN_data_first = DOOSAN_data.find("span", {"class": "blind"})
        DOOSAN_data_realTime = DOOSAN_data_first.text  # 실시간 가격
        DOOSAN_data_realTime_result = DOOSAN_data_realTime.replace(",", "")
        DOOSAN_data_realTime_int = int(DOOSAN_data_realTime_result)
        print(DOOSAN_data_realTime_int)
        print(DOOSAN_data_realTime)

        # SAMSUNG
        url_naver = "https://finance.naver.com/item/main.nhn?code=005930"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        samsung_data = bs_obj.find("div", {"class": "today"})
        samsung_data_first = samsung_data.find("span", {"class": "blind"})
        samsung_data_realTime = samsung_data_first.text  # 실시간 가격
        samsung_data_realTime_result = samsung_data_realTime.replace(",", "")
        samsung_data_realTime_int = int(samsung_data_realTime_result)
        print(samsung_data_realTime_int)
        print(samsung_data_realTime)

        # ASIANA
        url_naver = "https://finance.naver.com/item/main.nhn?code=020560"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        ASIANA_data = bs_obj.find("div", {"class": "today"})
        ASIANA_data_first = ASIANA_data.find("span", {"class": "blind"})
        ASIANA_data_realTime = ASIANA_data_first.text  # 실시간 가격
        ASIANA_data_realTime_result = ASIANA_data_realTime.replace(",", "")
        ASIANA_data_realTime_int = int(ASIANA_data_realTime_result)
        print(ASIANA_data_realTime_int)
        print(ASIANA_data_realTime)

        # KAKAO
        url_naver = "https://finance.naver.com/item/main.nhn?code=035720"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        KAKAO_data = bs_obj.find("div", {"class": "today"})
        KAKAO_data_first = KAKAO_data.find("span", {"class": "blind"})
        KAKAO_data_realTime = KAKAO_data_first.text  # 실시간 가격
        KAKAO_data_realTime_result = KAKAO_data_realTime.replace(",", "")
        KAKAO_data_realTime_int = int(KAKAO_data_realTime_result)
        print(KAKAO_data_realTime_int)
        print(KAKAO_data_realTime)

        # JINRO
        url_naver = "https://finance.naver.com/item/main.nhn?code=000080"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        JINRO_data = bs_obj.find("div", {"class": "today"})
        JINRO_data_first = JINRO_data.find("span", {"class": "blind"})
        JINRO_data_realTime = JINRO_data_first.text  # 실시간 가격
        JINRO_data_realTime_result = JINRO_data_realTime.replace(",", "")
        JINRO_data_realTime_int = int(JINRO_data_realTime_result)
        print(JINRO_data_realTime_int)
        print(JINRO_data_realTime)

        # HANWHA
        url_naver = "https://finance.naver.com/item/main.nhn?code=000880"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HANWHA_data = bs_obj.find("div", {"class": "today"})
        HANWHA_data_first = HANWHA_data.find("span", {"class": "blind"})
        HANWHA_data_realTime = HANWHA_data_first.text  # 실시간 가격
        HANWHA_data_realTime_result = HANWHA_data_realTime.replace(",", "")
        HANWHA_data_realTime_int = int(HANWHA_data_realTime_result)
        print(HANWHA_data_realTime_int)
        print(HANWHA_data_realTime)

        # HYUNDAI
        url_naver = "https://finance.naver.com/item/main.nhn?code=005380"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HYUNDAI_data = bs_obj.find("div", {"class": "today"})
        HYUNDAI_data_first = HYUNDAI_data.find("span", {"class": "blind"})
        HYUNDAI_data_realTime = HYUNDAI_data_first.text  # 실시간 가격
        HYUNDAI_data_realTime_result = HYUNDAI_data_realTime.replace(",", "")
        HYUNDAI_data_realTime_int = int(HYUNDAI_data_realTime_result)
        print(HYUNDAI_data_realTime_int)
        print(HYUNDAI_data_realTime)

        # NAVER
        url_naver = "https://finance.naver.com/item/main.nhn?code=035420"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        NAVER_data = bs_obj.find("div", {"class": "today"})
        NAVER_data_first = NAVER_data.find("span", {"class": "blind"})
        NAVER_data_realTime = NAVER_data_first.text  # 실시간 가격
        NAVER_data_realTime_result = NAVER_data_realTime.replace(",", "")
        NAVER_data_realTime_int = int(NAVER_data_realTime_result)
        print(NAVER_data_realTime_int)
        print(NAVER_data_realTime)

        # LGD
        url_naver = "https://finance.naver.com/item/main.nhn?code=034220"
        # url만 바꾸면 각 기업에 따른 값 크롤링 가능
        html = urllib.request.urlopen(url_naver)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LGD_data = bs_obj.find("div", {"class": "today"})
        LGD_data_first = LGD_data.find("span", {"class": "blind"})
        LGD_data_realTime = LGD_data_first.text  # 실시간 가격
        LGD_data_realTime_result = LGD_data_realTime.replace(",", "")
        LGD_data_realTime_int = int(LGD_data_realTime_result)
        print(LGD_data_realTime_int)
        print(LGD_data_realTime)

        try:
            with conn.cursor() as cursor:
                # CJ 디비넣기
                sql = 'INSERT INTO realtime_data (TIME, CJ, LG, SK, DOOSAN, SAMSUNG, ASIANA, KAKAO, HANWHA, HYUNDAI, JINRO, NAVER, LGD) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql, (time, CJ_data_realTime_int, LG_data_realTime_int, SK_data_realTime_int, DOOSAN_data_realTime_int, samsung_data_realTime_int, ASIANA_data_realTime_int, KAKAO_data_realTime_int, HANWHA_data_realTime_int, HYUNDAI_data_realTime_int, JINRO_data_realTime_int, NAVER_data_realTime_int, LGD_data_realTime_int))

            conn.commit()

        finally:
            conn.close()

        sleep(600)

    else :
        sleep(600)

