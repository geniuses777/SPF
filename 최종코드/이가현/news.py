import urllib.request
import bs4
import pymysql.cursors

conn = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777', password='stock7840', db='geniuses777',
                       charset='utf8')

try:
    with conn.cursor() as cursor:

        # CJ
        url = "https://search.naver.com/search.naver?&where=news&query=CJ&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        CJ_title_fir = bs_obj.find("ul", {"class": "type01"})
        CJ_title_sec = CJ_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('CJ',))

        for dl in CJ_title_sec:
            CJ_title_th = dl.find("a", {"class": "_sp_each_title"})
            CJ_title_th_txt = CJ_title_th.text
            CJ_news_url = CJ_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('CJ', str(CJ_title_th_txt), str(CJ_news_url)))

        # LG
        url = "https://search.naver.com/search.naver?&where=news&query=lg&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        lg_title_fir = bs_obj.find("ul", {"class": "type01"})
        lg_title_sec = lg_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('LG',))

        for dl in lg_title_sec:
            lg_title_th = dl.find("a", {"class": "_sp_each_title"})
            lg_title_th_txt = lg_title_th.text
            lg_news_url = lg_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('LG', str(lg_title_th_txt), str(lg_news_url)))

        # SK
        url = "https://search.naver.com/search.naver?&where=news&query=sk&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        sk_title_fir = bs_obj.find("ul", {"class": "type01"})
        sk_title_sec = sk_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('SK',))

        for dl in sk_title_sec:
            sk_title_th = dl.find("a", {"class": "_sp_each_title"})
            sk_title_th_txt = sk_title_th.text
            sk_news_url = sk_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('SK', str(sk_title_th_txt), str(sk_news_url)))

        # DOOSAN
        url = "https://search.naver.com/search.naver?&where=news&query=%EB%91%90%EC%82%B0&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        DOO_title_fir = bs_obj.find("ul", {"class": "type01"})
        DOO_title_sec = DOO_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('두산',))

        for dl in DOO_title_sec:
            DOO_title_th = dl.find("a", {"class": "_sp_each_title"})
            DOO_title_th_txt = DOO_title_th.text
            DOO_news_url = DOO_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('두산', str(DOO_title_th_txt), str(DOO_news_url)))

        # SAMSUNG
        url = "https://search.naver.com/search.naver?&where=news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        SS_title_fir = bs_obj.find("ul", {"class": "type01"})
        SS_title_sec = SS_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('삼성',))

        for dl in SS_title_sec:
            SS_title_th = dl.find("a", {"class": "_sp_each_title"})
            SS_title_th_txt = SS_title_th.text
            SS_news_url = SS_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('삼성', str(SS_title_th_txt), str(SS_news_url)))

        # ASIANA
        url = "https://search.naver.com/search.naver?&where=news&query=%EC%95%84%EC%8B%9C%EC%95%84%EB%82%98%ED%95%AD%EA%B3%B5&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        ASIANA_title_fir = bs_obj.find("ul", {"class": "type01"})
        ASIANA_title_sec = ASIANA_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('아시아나항공',))

        for dl in ASIANA_title_sec:
            ASIANA_title_th = dl.find("a", {"class": "_sp_each_title"})
            ASIANA_title_th_txt = ASIANA_title_th.text
            ASIANA_news_url = ASIANA_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('아시아나항공', str(ASIANA_title_th_txt), str(ASIANA_news_url)))

        # KAKAO
        url = "https://search.naver.com/search.naver?&where=news&query=%EC%B9%B4%EC%B9%B4%EC%98%A4&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        KAKAO_title_fir = bs_obj.find("ul", {"class": "type01"})
        KAKAO_title_sec = KAKAO_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('카카오',))

        for dl in KAKAO_title_sec:
            KAKAO_title_th = dl.find("a", {"class": "_sp_each_title"})
            KAKAO_title_th_txt = KAKAO_title_th.text
            KAKAO_news_url = KAKAO_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('카카오', str(KAKAO_title_th_txt), str(KAKAO_news_url)))

        # HANWHA
        url = "https://search.naver.com/search.naver?&where=news&query=%ED%95%9C%ED%99%94&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HANWHA_title_fir = bs_obj.find("ul", {"class": "type01"})
        HANWHA_title_sec = HANWHA_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('한화',))

        for dl in HANWHA_title_sec:
            HANWHA_title_th = dl.find("a", {"class": "_sp_each_title"})
            HANWHA_title_th_txt = HANWHA_title_th.text
            HANWHA_news_url = HANWHA_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('한화', str(HANWHA_title_th_txt), str(HANWHA_news_url)))

        # HYUNDAI
        url = "https://search.naver.com/search.naver?&where=news&query=%ED%98%84%EB%8C%80%EC%B0%A8&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        HYUNDAI_title_fir = bs_obj.find("ul", {"class": "type01"})
        HYUNDAI_title_sec = HYUNDAI_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('현대',))

        for dl in HYUNDAI_title_sec:
            HYUNDAI_title_th = dl.find("a", {"class": "_sp_each_title"})
            HYUNDAI_title_th_txt = HYUNDAI_title_th.text
            HYUNDAI_news_url = HYUNDAI_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('현대', str(HYUNDAI_title_th_txt), str(HYUNDAI_news_url)))

        # JINRO
        url = "https://search.naver.com/search.naver?&where=news&query=%ED%95%98%EC%9D%B4%ED%8A%B8%EC%A7%84%EB%A1%9C&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        JINRO_title_fir = bs_obj.find("ul", {"class": "type01"})
        JINRO_title_sec = JINRO_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('하이트진로',))

        for dl in JINRO_title_sec:
            JINRO_title_th = dl.find("a", {"class": "_sp_each_title"})
            JINRO_title_th_txt = JINRO_title_th.text
            JINRO_news_url = JINRO_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('하이트진로', str(JINRO_title_th_txt), str(JINRO_news_url)))

        # 네이버
        url = "https://search.naver.com/search.naver?&where=news&query=%EB%84%A4%EC%9D%B4%EB%B2%84&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        NAVER_title_fir = bs_obj.find("ul", {"class": "type01"})
        NAVER_title_sec = NAVER_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('네이버',))

        for dl in NAVER_title_sec:
            NAVER_title_th = dl.find("a", {"class": "_sp_each_title"})
            NAVER_title_th_txt = NAVER_title_th.text
            NAVER_news_url = NAVER_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('네이버', str(NAVER_title_th_txt), str(NAVER_news_url)))

        # LGD
        url = "https://search.naver.com/search.naver?&where=news&query=LG%EB%94%94%EC%8A%A4%ED%94%8C%EB%A0%88%EC%9D%B4&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&start=1&refresh_start=0"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        LGD_title_fir = bs_obj.find("ul", {"class": "type01"})
        LGD_title_sec = LGD_title_fir.findAll("dl")

        sql = 'DELETE FROM company_news WHERE company_name = %s'
        cursor.execute(sql, ('LGD',))

        for dl in LGD_title_sec:
            LGD_title_th = dl.find("a", {"class": "_sp_each_title"})
            LGD_title_th_txt = LGD_title_th.text
            LGD_news_url = LGD_title_th.attrs['href']

            sql = 'INSERT INTO company_news (company_name, news, url) VALUES (%s, %s, %s)'
            cursor.execute(sql, ('LGD', str(LGD_title_th_txt), str(LGD_news_url)))

    conn.commit()

finally:
    conn.close()