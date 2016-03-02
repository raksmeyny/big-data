import pandas
import json

# file name
new_allInvoice2 = "new_allInvoice2.csv"

# data frame name
sales=pandas.read_csv("members.csv")
newSales=pandas.read_csv("allInvoices2.csv")

# get Transaction from data frame
TransactionNumberList = list(sales.TransactionNumber)
customeridNumberList = list(sales.CustomerID)
theIndex = (len(customeridNumberList))

# create dictionary product
dictProduct = {}
for item in range(theIndex):
	dictProduct[TransactionNumberList[item]] = customeridNumberList[item]

newList = []
newTransactionNumberList = list(newSales.TransactionNumber)
for newTransactionNumber in newTransactionNumberList:

	# checked if it keys
	if newTransactionNumber in dictProduct.keys():
		print newTransactionNumber
		newList.append(dictProduct[newTransactionNumber])
	else:
		newList.append(0)

# save output
newSales['CustomerID']=newList
newSales.to_csv(new_allInvoice2)