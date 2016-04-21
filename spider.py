import sys,urllib.request, os
from bs4 import BeautifulSoup
# python /Users/yanzi/work/workspaces/python/spider.py http://www.baidu.com
# print(sys.argv[0])
print(urllib.__file__)

# 获取脚本文件的当前路径
def cur_file_dir():
    path1 = sys.path[0]
    if os.path.isdir(path1):
        return path1
    elif os.path.isfile(path1):
        return os.path.dirname(path1)

def get_source_url():
    url = sys.argv[1]
    if 1:
        return url
    else:
        return url

def get_template_body():
    # 加载模版
    path = cur_file_dir() + "/template.html"
    soup2 = BeautifulSoup(open(path), "html.parser")
    body = soup2.body
    return (soup2, body)

def get_answer(url):
    content = urllib.request.urlopen(url).read()
# fp = open("/Users/yanzi/Desktop/aaa.html", "wb")
# fp.write(content)
# fp.close()
    soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
    answer1 = soup.find('div', class_='single-siti clearfix')
    answer1.i.extract()
    answer2 = soup.find('div', class_='tm-bottom')
    answer2.a.extract()
    answer3 = soup.find('div', class_='analysis clearfix')
    return (answer1, answer2, answer3)

"""
def get_url_from_browser():
 path = cur_file_dir()
 # dr = webdriver.Chrome(executable_path=path + '/chromedriver')
 chromedriver = '/Applications/Google Chrome.app/Contents/MacOS' + '/chromedriver'
 os.environ["webdriver.chrome.driver"] = chromedriver
 dr = webdriver.Chrome(chromedriver)
 dr.get("http://www.163.com")
 url = dr.current_url
 print(url)

def get_url_from_browser2():
 path = cur_file_dir()
 dr = webdriver.Firefox()
 # dr.get("http://www.163.com")
 url = dr.current_url
 print(url)
 # url = dr.open_new_tab("http:\\www.163.com")
 """

# url=get_source_url()
(soup2, body) = get_template_body();
url = input(".....请输入url地址,多个url以空格分开....\n")
# print(url)
urls = url.split(" ")
for temp_url in urls:
    (a1, a2, a3) = get_answer(temp_url)
    body.append(a1)
    body.append(a2)
    body.append(a3)
    tt = BeautifulSoup("<br/>", "html.parser")
    body.append(tt)

#save to answer.html
fp = open("/Users/yanzi/Desktop/answer.html", "w")
fp.write(soup2.prettify())
fp.close()
print('-----------------That is ok---------------')



