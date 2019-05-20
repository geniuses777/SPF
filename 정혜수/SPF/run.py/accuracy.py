
# coding: utf-8

# In[3]:

import pymysql

connection = pymysql.connect(host='222.122.86.187', port=3306, user='geniuses777', password='stock7840',
                       db='geniuses777', charset='utf8')

############################################ 오차율 계산하기 ############################################

############################################ 삼성 ############################################
try:
    with connection.cursor() as cursor:  
        sql = "select stock_price from stock_hye WHERE company_name='삼성'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='삼성'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '삼성'))
        
        
        connection.commit()
    
############################################ 카카오 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='카카오'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='카카오'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '카카오'))
        
        
        connection.commit()
    
############################################ 네이버 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='네이버'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='네이버'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '네이버'))
        
        
        connection.commit()
    
############################################ CJ ############################################
        sql = "select stock_price from stock_hye WHERE company_name='CJ'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='CJ'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'CJ'))
        
        
        connection.commit()
    

############################################ LG ############################################
        sql = "select stock_price from stock_hye WHERE company_name='LG'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='LG'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'LG'))
        
        
        connection.commit()
    

############################################ SK ############################################
        sql = "select stock_price from stock_hye WHERE company_name='SK'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='SK'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
              

        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'SK'))
        
        
        connection.commit()
    

############################################ LGD ############################################
        sql = "select stock_price from stock_hye WHERE company_name='LGD'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='LGD'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, 'LGD'))
        
        
        connection.commit()
    

############################################ 두산 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='두산'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='두산'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '두산'))
        
        
        connection.commit()
    

############################################ 아시아나항공 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='아시아나항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='아시아나항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '아시아나항공'))
        
        
        connection.commit()
    

############################################ 제주항공 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='제주항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='제주항공'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '제주항공'))
        
        
        connection.commit()
    

############################################ 한화 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='한화'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='한화'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '한화'))
        
        
        connection.commit()
    

############################################ 현대 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='현대'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='현대'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '현대'))
        
        
        connection.commit()
    

############################################ 하이트진로 ############################################
        sql = "select stock_price from stock_hye WHERE company_name='하이트진로'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_stock_price = cursor.fetchone()
        
        for i in result_stock_price:
            price = i
            
        sql = "select now from company WHERE name='하이트진로'"
        
        cursor.execute("set names utf8")
        
        cursor.execute(sql)
        
        result_now = cursor.fetchone()
        
        for i in result_now:
            now = i
            
            
        sql = "UPDATE `stock_hye` SET `accuracy` = %s WHERE `company_name` = %s"

        accuracy = float(abs(price-now)/now*100)
        
        cursor.execute(sql, (accuracy, '하이트진로'))
        
        
        connection.commit()
    
        

finally:
    connection.close()
    print("MySQL connection is closed")


# In[ ]:



