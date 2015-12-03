import sys
import pandas as pd
import csv

def main(argv):	
	myDataLoc=argv	
	myData = pd.DataFrame.from_csv(myDataLoc,index_col=False,encoding = "ISO-8859-1");
	var=list(myData.columns.values)
	o = []
	for v in var:
		row = []		
		c = input(v)
		row.append(v)
		row.append(c)
		o.append(row)
	
	print(o)

	with open('Schema.csv','w') as out:
		csv_out=csv.writer(out)
		csv_out.writerow(['name','type'])
		for row in o:
			csv_out.writerow(row)


if __name__ == '__main__':	
	main(sys.argv[1])

