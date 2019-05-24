
# coding: utf-8

# In[6]:

import pymysql
import os
import settings
import pandas as pd

connection = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777', password='stock7840',
                       db='geniuses777', charset='utf8')

############################################ 상승률(하락률) 계산하기 ############################################

############################################ 삼성 ############################################
try:
    with connection.cursor() as cursor:  
        sql = "select stock_price from stock_hye WHERE company_name='삼성'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "samsung"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
        
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        #if accuracy > 0 :
            #accuracy = "+" + str(accuracy)
            #print(accuracy)
        #elif accuracy < 0 :
            #accuracy = "-" + str(accuracy)
            #print(accuracy)

        cursor.execute(sql, (accuracy, '삼성'))
        
        
        connection.commit()
    
############################################ 카카오 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='카카오'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "kakao"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '카카오'))
        
        
        connection.commit()
    
############################################ 네이버 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='네이버'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "naver"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '네이버'))
        
        
        connection.commit()
    
############################################ CJ ############################################
        sql = "select stock_price from stock_hye WHERE company_name='CJ'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "cj"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'CJ'))
        
        
        connection.commit()

############################################ LG ############################################
        sql = "select stock_price from stock_hye WHERE company_name='LG'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "lg"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'LG'))
        
        
        connection.commit()
    
############################################ SK ############################################
        sql = "select stock_price from stock_hye WHERE company_name='SK'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "sk"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'SK'))
        
        
        connection.commit()

############################################ LGD ############################################
        sql = "select stock_price from stock_hye WHERE company_name='LGD'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "lgdisplay"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'LGD'))
        
        
        connection.commit()

############################################ 두산 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='두산'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "dusan"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
        
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '두산'))
        
        
        connection.commit()

############################################ 아시아나항공 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='아시아나항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "asiana"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
        
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '아시아나항공'))
        
        
        connection.commit()

############################################ 제주항공 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='제주항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
            
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "jeju"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '제주항공'))
        
        
        connection.commit()

############################################ 한화 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='한화'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "hanhwa"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '한화'))
        
        
        connection.commit()

############################################ 현대 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='현대'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "hyundai"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '현대'))
        
        
        connection.commit()

############################################ 하이트진로 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='하이트진로'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        
        #
        # 저장되어있는 주식데이터 불러오기
        #
        sydtpath = os.path.join(settings.BASE_DIR, 'chart_data/%s' % (settings.get_today_str()))
        stock_code = "hite"
        fullpath = sydtpath + os.path.sep + stock_code + '.csv'
        pandf = pd.read_csv(fullpath, index_col="Date")

        # 데이터 전처리
        now = pandf['Close'].values[-1]     # 맨마지막 'Close'데이터
        now.astype('int')    # int형으로 변환
            
            
        sql = "UPDATE `stock_hye` SET `rate` = %s WHERE `company_name` = %s"

        accuracy = float((price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '하이트진로'))
        
        
        connection.commit()

finally:
    connection.close()
    print("MySQL connection is closed")


# In[ ]:



