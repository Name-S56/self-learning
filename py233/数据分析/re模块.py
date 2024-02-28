import re

result = re.findall(r"\d+","我18岁,身价有200000000元")    #\转义 字符串前面加r
print(result)

result = re.finditer(r"\d+","我18岁,身价有200000000元")    
for item in result: #迭代器中拿东西
    print(item.group())   #.group从匹配的结果中拿数据

result = re.search(r"\d+","我18岁,身价有200000000元") #只匹配到第一次匹配的内容
print(result.group())

#match在匹配的时候,从字符串的开头进行匹配,类似于正则前加上了^
result = re.match(r"\d+","1111我18岁,身价有200000000元")   
print(result)

#预加载,提前把正则对象加载完毕
obj = re.compile(r"\d+")
# 直接把加载好的正则进行使用
result = obj.findall("我18岁,身价有200000000元")
print(result)