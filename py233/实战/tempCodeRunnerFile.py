 for item in data["data"]:
            title = item["object"]["title"]
            content = item["object"]["content"]
            url = item["object"]["url"]
            print(title,content,url)
            with open(f"{name}.md", "a", encoding="utf-8") as file:
                file.write(f"## {title}\n")
                file.write("### 内容\n")
                file.write(content+"\n")
                file.write(f"##$ 文章详细url:{url}")