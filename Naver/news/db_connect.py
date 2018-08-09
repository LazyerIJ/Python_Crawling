import pymysql
import datetime

def db_conn():
    conn = pymysql.connect("localhost","root","dkfkdtkfkd1!","naver_news")
    return conn

def sql_insert(cursor,value_list,table):

    sql = "insert into %s values("%(table)

    for value in value_list:
        sql += "'%s',"%format(value)

    sql = list(sql)
    sql[len(sql)-1]=')'
    print("".join(sql))

    try:
        cursor.execute("".join(sql))
        return "[%s]insert success"%(datetime.datetime.now().time()),1
    except:
        return "[%s]insert failed"%(datetime.datetime.now().time()),0
    

    







