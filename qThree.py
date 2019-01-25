# -*-coding:utf-8 -*-
# 算低於 1000 的 3 跟 5 的倍數總和
# Function to calculate sum of 3 or 5 multiples under 1000
def getThreeFiveMultiples():
	totalSum = 0;
	for i in range(1000):
		# If i is multiple of 3 or 5, we will add it to our sum
		if i % 3 == 0 or i % 5 == 0:
			totalSum = totalSum + i

	return totalSum

print(getThreeFiveMultiples())