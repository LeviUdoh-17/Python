import codecs
from bs4 import BeautifulSoup
# import lxml

with codecs.open("100days/web_dev/bs4-start/website.html", "r", encoding="utf8") as files:
    content = files.read()
soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
# print(soup.title.string)
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get('href'))
# heading = soup.find(name='h1', id='name')
# print(heading)

sectional_heading = soup.find(name='h3', class_='heading')
print(sectional_heading.get_text())
print(sectional_heading.name)
print(sectional_heading.get('class'))
company_url = soup.select_one(selector='p a')
print(company_url)