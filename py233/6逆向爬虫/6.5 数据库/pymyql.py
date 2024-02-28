import pymysql

def add(sql):
    try:
        conn = pymysql.connect(
        user="root",
        password="root",
        host="localhost",
        database="spider",
        port=3306
    )
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        #new's数据id
        new_id= cursor.lastrowid
        return new_id
    except Exception as e:
        print(e)
        conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def change(sql,isInsert=False):
    