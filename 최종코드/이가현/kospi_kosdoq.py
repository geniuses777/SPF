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

    time = now.strftime('%Y-%m-%d %H:%M:%S')

    print(time)
    print(now.hour)

    if now.hour >= 9 and now.hour < 16 :

        url = "https://finance.naver.com/"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        kospi_first = bs_obj.find("div", {"class": "heading_area"})
        kospi = kospi_first.find("span", {"class": "num"})  # 실시간 코스피값
        kospi_fir = kospi_first.find("span", {"class": "num"})
        kospi_sec = kospi_fir.text
        kospi_result = kospi_sec.replace(",", "")
        kospi = float(kospi_result)
        print(kospi)


        kosdaq_first = bs_obj.find("div", {"class": "kosdaq_area group_quot"})
        kosdaq = kosdaq_first.find("span", {"class": "num"})  # 실시간 코스닥값
        kosdaq_fir = kosdaq_first.find("span", {"class": "num"})
        kosdaq_sec = kosdaq_fir.text
        kosdaq_result = kosdaq_sec.replace(",", "")
        kosdaq = float(kosdaq_result)
        print(kosdaq)

        try:
            with conn.cursor() as cursor:
                # CJ 디비넣기
                sql = 'INSERT INTO kospi_kosdaq (TIME, KOSPI, KOSDAQ) VALUES (%s, %s, %s)'
                cursor.execute(sql, (time, kospi, kosdaq))

            conn.commit()

        finally:
            conn.close()

        sleep(600)

    else :
        sleep(600)