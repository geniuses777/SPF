
# coding: utf-8

# In[1]:


#
# csv파일 저장
#
import FinanceDataReader as fdr
import settings
import os
import locale
from datetime import date, timedelta

start_date = '2009-01-01' # 최근 10년간 데이터
end_date = settings.get_today_str() # 오늘날짜
#end_date = date.today() - timedelta(1) # 어제날짜
stocks = ['samsung', 'kakao', 'naver', 'cj', 'lg', 'sk', 'lgdisplay', 'dusan', 'asiana', 'jeju', 'hanhwa', 'hyundai', 'hite']
#stocks = ['005930', '035720', '035420', '001040', '066570', '034730', '034220', '000150', '020560', '089590', '000880', '005380', '000080']

# .csv파일을 저장할 디렉토리
data_dir = os.path.join(
    settings.BASE_DIR, 'chart_data/%s' % (
        settings.get_today_str()))     # timestr : 날짜, 시간
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)
    
############################ csv파일 추가 ############################
## samsung
df = fdr.DataReader('005930', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[0]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[0]))
## kakao
df = fdr.DataReader('035720', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[1]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[1]))
## naver
df = fdr.DataReader('035420', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[2]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[2]))
## cj
df = fdr.DataReader('001040', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[3]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[3]))
## lg
df = fdr.DataReader('066570', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[4]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[4]))
## sk
df = fdr.DataReader('034730', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[5]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[5]))
## lgdisplay
df = fdr.DataReader('034220', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[6]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[6]))
## dusan
df = fdr.DataReader('000150', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[7]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[7]))
## asiana
df = fdr.DataReader('020560', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[8]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[8]))
## jeju
df = fdr.DataReader('089590', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[9]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[9]))
## hanhwa
df = fdr.DataReader('000880', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[10]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[10]))
## hyundai
df = fdr.DataReader('005380', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[11]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[11]))
## hite
df = fdr.DataReader('000080', start_date, end_date)
#df.to_csv('./chart_data/%s/%s.csv' % (settings.get_today_str(), stocks[12]))
df.to_csv("C:\source\SPF\chart_data\%s\%s.csv" % (settings.get_today_str(), stocks[12]))

print(settings.get_today_str())
#yesterday = date.today() - timedelta(1)
#print(yesterday.strftime('%Y-%m-%d'))


# In[ ]:




