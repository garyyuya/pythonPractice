# -*-coding:utf-8 -*-
# 加入1~3行 code 來完成積分的function
def annonymous(x):
	return x**2+1

def integration(fun, start, end):
	step = 0.1
	intercept = start
	area = 0

	while intercept < end:
		intercept += step
		#Calculate the height of the rectangle
		height = annonymous(intercept)
		#Calculate the area by multiplying width and height
		currArea = height*step
		#Add the area
		area += currArea

	return area


print(integration(annonymous,0,10))