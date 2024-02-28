import pymysql
try:
    #1  create connection
    conn = pymysql.connect(
        user="root",
        password="root",
        host="localhost",
        database="spider",
        port=3306
    )

    #2 execute sql 语句
    cursor = conn.cursor()#游标

    #3 ready sql
    sql = "insert into stu_new(sname,sagq,score,sgender,class) values" \
            "('a',18,66,1,'一班')"
    #执行 sql
    result = cursor.execute(sql)
    print(result)

    #pymsqyl 执行sql时候,默认开启事务
    #rollbac , commit
    conn.commit()
except :
    conn.rollback()
finally:
    if conn:
        conn.close()