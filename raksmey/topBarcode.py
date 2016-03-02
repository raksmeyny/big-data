import pandas
import csv
from collections import Counter

data_df = pandas.read_csv('allInvoices2.csv')
# print (data_df.Barcode)
barcode = list(data_df.Barcode)
# print barcode
cnt = Counter()
for bar in barcode:
	cnt[bar]+=1
# print cnt
# sc = cnt.most_common(10)
sc = cnt.most_common()
print sc
with open('topBarcode.csv', 'w') as fp:
    cf= csv.writer(fp, delimiter=',')
    cf.writerows(sc)