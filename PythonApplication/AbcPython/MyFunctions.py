def MyAverage(x,y):
	print('This is a function in a file')
	return (x+y)/2

def MyStat(data):
	totalsum=0
	for x in data:
		totalsum=totalsum+x
	n=len(data)
	mean=totalsum/n
	return totalsum, mean
