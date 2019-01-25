# -*-coding:utf-8 -*-
# 計算出現次數前三多的filename

def printTopThree(urls):
	#get the filename from each url and store them into the resultList
	resultList = []
	for i in urls:
		#split current url with seperator "/"
		tempL = i.split("/")
		#get the last element which is the filename
		tempStr = tempL[-1]
		#store the filename into the list
		resultList.append(tempStr)

	#create a dictionany to store filename and its corresponding count
	dic = {}
	for i in resultList:
		#if the dictionary does not have the key yet -> add the key and value(count) = 1
		if i not in dic.keys():
			dic[i] = 1
		#if the dicionanry already has the key -> increase the count 
		else:
			dic[i] = dic[i] + 1

	#get the top three frequent filename
	printMaxAndRemove(dic)
	printMaxAndRemove(dic)
	printMaxAndRemove(dic)

#function to get the most frequent filename -> print it then remove it from the dictionary
def printMaxAndRemove(dic):

	#get the most frequent count
	maxNum = -1
	for i in dic.values():
		if i >= maxNum:
			maxNum = i

	#find the corresponding key that has the most frequent count
	for i in dic.keys():
		if dic.get(i) == maxNum:
			print(i + " " + str(dic.get(i)))
			del dic[i]
			break


		

urls = [
"http://www.google.com/a.text",
"http://www.google.com.tw/a.text",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.text",
"http://www.google.com/b.text",
"https://facebook.com/movie/b.text",
"http://www.yahoo.com/123/000/c.jpg",
"http://www.gliacloud.com/haha.png",
]

printTopThree(urls)