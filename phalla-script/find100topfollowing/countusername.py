#!/usr/bin/python

import pandas
from collections import Counter


data_df = pandas.read_csv("top_20_following.csv")


user = data_df['Username']

username = list(user)

count = Counter()
for name in username:
	count[name]+=1
un = count.most_common(100)
print un

result=['Username']

tmp={ "Username":[i for i,_ in un], "Count":[j for _,j in un] }
T=pandas.DataFrame(tmp)
T.to_csv("Top100Following.csv",mode="w+")

