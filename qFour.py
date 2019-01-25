# -*-coding:utf-8 -*-
# Python Ptt 爬蟲
# 給一個 URL 可以抓取 日期，作者，標題，內文，看板名稱
import requests, bs4
def getArticle(url):
	#Use request to get the URL and check for status
	res = requests.get(url)
	res.raise_for_status()

	#Use BeautifulSoup to parse the html
	soup = bs4.BeautifulSoup(res.text, "html.parser")

	#Find the correct span by using the class name to get: arthur, boardName, title, and time
	arthur = soup.find_all('span' , class_='article-meta-value')[0].getText()
	boardName = soup.find_all('span' , class_='article-meta-value')[1].getText()
	title = soup.find_all('span' , class_='article-meta-value')[2].getText()
	time = soup.find_all('span' , class_='article-meta-value')[3].getText()

	#Find the correct div to get content
	content = soup.find('div' , id = 'main-content').getText()
	#Split the content with "--" to remove comment section
	content = content.split("--")[0]

	#print(arthur)
	#print(boardName)
	#print(title)
	#print(time)
	print(content)

#Example url
url = 'https://www.ptt.cc/bbs/NBA/M.1548312328.A.1C5.html'
getArticle(url)

