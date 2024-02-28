# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#管道默认不工作 找settings
class GamePipeline: #随便定义一个类
    def process_item(self, item, spider):   #定死的,处理数据的专用方法
        #item 数据 
       # print(item)
        return item     #return到下一个管道

class NewPipeline: #随便定义一个类
    def process_item(self, item, spider):   
        item['love'] = "满身疮痍"
        print(item)
        return item    