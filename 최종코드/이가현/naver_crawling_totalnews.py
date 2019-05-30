import urllib.request
import bs4
import pymysql.cursors


conn = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777',password='stock7840', db='geniuses777', charset='utf8')

try:
    with conn.cursor() as cursor:
        sql = 'DELETE FROM total_news WHERE num = %s'
        cursor.execute(sql, ('1',))

        url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=1"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        total_f = bs_obj.find("ul", {"class":"type06_headline"})

        total_s = total_f.findAll("dl")

        for a in total_s:
            new_f = a.find("a")
            new_f_str = str(new_f)
            if new_f_str.find("img") != -1:  #이미지가 존재하는 기사만
                new_s = new_f.find("img", {"height":"72"})
                new_s_txt = new_s.attrs['alt']
                new_f_url = new_f.attrs['href']

                print(new_s_txt)
                print(new_f_url)

                sql = 'INSERT INTO total_news (title, url) VALUES (%s, %s)'
                cursor.execute(sql, (str(new_s_txt), str(new_f_url)))

        url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=2"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        total_f = bs_obj.find("ul", {"class": "type06_headline"})

        total_s = total_f.findAll("dl")

        for a in total_s:
            new_f = a.find("a")
            new_f_str = str(new_f)
            if new_f_str.find("img") != -1:  #이미지가 존재하는 기사만
                new_s = new_f.find("img", {"height": "72"})
                new_s_txt = new_s.attrs['alt']
                new_f_url = new_f.attrs['href']

                print(new_s_txt)
                print(new_f_url)

                sql = 'INSERT INTO total_news (title, url) VALUES (%s, %s)'
                cursor.execute(sql, (str(new_s_txt), str(new_f_url)))

        url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=101&sid2=258&page=3"
        html = urllib.request.urlopen(url)

        bs_obj = bs4.BeautifulSoup(html, "html.parser")

        total_f = bs_obj.find("ul", {"class": "type06_headline"})
        # print(total_f)

        total_s = total_f.findAll("dl")
        # print(total_s)

        for a in total_s:
            new_f = a.find("a")
            new_f_str = str(new_f)
            if new_f_str.find("img") != -1:  #이미지가 존재하는 기사만
                new_s = new_f.find("img", {"height": "72"})
                new_s_txt = new_s.attrs['alt']
                new_f_url = new_f.attrs['href']

                print(new_s_txt)
                print(new_f_url)

                sql = 'INSERT INTO total_news (title, url) VALUES (%s, %s)'
                cursor.execute(sql, (str(new_s_txt), str(new_f_url)))
    conn.commit()

finally:
    conn.close()
