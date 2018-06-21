'''
Analyze CSVs of survey response data
Text analysis of free responses. Look for phrases like 'repair credit' and 'legacy'
'''

import csv

def readCSV(file):
	# reader = csv.reader(['1997,Ford,E350,"Super, luxurious truck"'], skipinitialspace=True)
	# for r in reader:
	# 	print r

	# f = open(sys.argv[1],'rb')
	f = open(file, 'rb')
	reader = csv.reader(f)
	for row in reader:
		if row != '':
			print row[7]

if __name__ == '__main__':
	readCSV('haveHome.csv')
