from pyquery import PyQuery

p = PyQuery(html)

p("div aaa").after("""div class="ccc">hhh</div>""")#尾部添加
p("div aaa").append("""<span>iii</span>""")

p("div bbb").attr("class","aaa")#bbb改成aaa
p("div.bbb").attr("id","123")#新增属性 无这个标签

p("div.bbb").remove_attr("id")#删除属性
p("div.bbb").remove()#删除标签