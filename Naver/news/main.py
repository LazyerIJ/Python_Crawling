import os
import sys
import scrapy_naver
import db_connect
import time

page_base = 'http://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1='
page_dict = {'100':'politic',
             '101':'economy',
             '102':'society',
             '103':'life',
             '104':'world',
             '105':'IT'}

url_nextpage = '#&date=2018-01-20 00:00:00&page='
url_id_len = -23
dir_data = './news'
mysql_table = 'news_id'

def chk_file_name(label):

    if not os.path.isdir(dir_data):
        os.mkdir(dir_data)
    os.chdir(dir_data)
    if not os.path.isdir('./'+label):
        os.mkdir('./'+label)
    os.chdir(label) 

    file_list = os.listdir()
    max_name = 0
    for name in file_list:
        if int(name[:-4])>max_name:
            max_name = int(name[:-4])
    return max_name

def print_title_content(file_name,title,content):
    sysout = sys.stdout
    if file_name=='':
        print('title : ' , title)
        print('content : ' , content)
        pass
    else:
        file_name = '%d.txt'%file_name
        sys.stdout = open(file_name,'w')
        print(title)
        print("====")
        print(content)
        sys.stdout.close()
    sys.stdout = sysout
    print('File_Name>>'+file_name)
    


def scrapy_naver_news_categories():
    for data,label in page_dict.items():
        page = page_base + data
        url_list = scrapy_naver.get_url(page)
        yield label,url_list


def scrapy_naver_news(url_list):
    for url in url_list:
        url_id = url[url_id_len:]
        title,content = scrapy_naver.get_title_and_content(url)
        yield url_id,label,title,content
        time.sleep(3)

if __name__=='__main__':

    conn = db_connect.db_conn()
    cursor = conn.cursor()
    

    for label,url_list in scrapy_naver_news_categories():
        file_name = int(chk_file_name(label))
        for news_id,news_label,title,content in scrapy_naver_news(url_list):
            insert_list = [news_id,news_label]

            info,result = db_connect.sql_insert(cursor,insert_list,mysql_table)
            conn.commit()
            print(info,"value='%s',label='%s'"%(news_id,news_label))

            if(result==1):
                print("label>>"+label)
                print_title_content(file_name,title,content)
                file_name += 1
    conn.close()






