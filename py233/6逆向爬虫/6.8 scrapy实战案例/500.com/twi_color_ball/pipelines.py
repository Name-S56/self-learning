# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twi_color_ball.settings import MYSQL
class TwiColorBallPipeline:
    def open_spider(self,spider):
        self.f =  open("./双色球.csv",mode="a",encoding="utf-8")  #mode =w覆盖

    def close_spider(self,spider):
        if self.f: 
            self.f.close()
        
    def process_item(self, item, spider):
        self.f.write(f"{item['seven']}, {'_'.join(item['red_ball'])} , item{item['blue_ball']}\n")  #red 多个
        return item
    
    #每次都要open文件很麻烦
    #open_spider close_spider

class TwiColorBall_MYSQLPipeline:
    def open_spider(self,spider):
        self.conn =  pymysql.connect(
            host=MYSQL['host'],
            port=MYSQL["port"],
            user= MYSQL['user'],
            password = MYSQL['password'],
            database = MYSQL['database']
        )
    def close_spider(self,spider):
        if self.conn: 
            self.conn.close()
        
    def process_item(self, item, spider):
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao (seven,red_ball,blue_ball) values (%s,%s,%s)"
            cursor.execute(sql,(item['seven'],"_".join(item['red_ball']),item['blue_ball']))#元组
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()
        return item
    
