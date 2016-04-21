import sys,urllib.request, os
from selenium import webdriver
from bs4 import BeautifulSoup
# python /Users/yanzi/work/workspaces/python/spider.py http://www.baidu.com
# print(sys.argv[0])
# print(urllib.__file__)

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

url=get_source_url()
print(url)
wp = urllib.request.urlopen(url)
content = wp.read()
# fp = open("/Users/yanzi/Desktop/aaa.html", "wb")
# fp.write(content)
# fp.close()
soup = BeautifulSoup(content, "html.parser")
# print(soup.title)
answer1 = soup.find('div', class_='single-siti clearfix')
answer2 = soup.find('div', class_='tm-bottom')
answer3 = soup.find('div', class_='analysis clearfix')

# 加载模版
path = cur_file_dir() + "/template.html"
soup2 = BeautifulSoup(open(path), "html.parser")
body = soup2.body
body.append(answer1)
body.append(answer2)
body.append(answer3)
fp = open("/Users/yanzi/Desktop/answer.html", "w")
fp.write(soup2.prettify())
fp.close()
print('That is ok...')



