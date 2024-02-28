import pymysql
from pymysql.cursors import DictCursor
conn = pymysql.connect(
    user="root",
    password="root",
    host="localhost",
    database="spider",
    port=3306
)
cursor = conn.cursor(cursor= DictCursor)

sql = "select * from stu"

ret = cursor.execute(sql)

#warning, 查询操作return值在cursor里
all = cursor.fetchall()
#fetchone
#fetchmany (10)
