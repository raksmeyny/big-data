#!/usr/bin/python

import pandas

df = pandas.read_csv("safirstores_follower.csv")

# find top follower
df['TopFollowers']=df['Number of followers'].convert_objects(convert_numeric=True)
topfollower=df.sort(['TopFollowers'],ascending=[0])
followers=['Username','TopFollowers']
topfollower[followers].to_csv("TopFollower.csv")

# find top number of post
df['TopPosts']=df['Number of posts'].convert_objects(convert_numeric=True)
toppost = df.sort(['TopPosts'],ascending=[0])
post=['Username','TopPosts']
toppost[post].to_csv("TopPost.csv")

# hightest number of likes
df['HightestLike']=df['Average number of likes for last 30 posts'].convert_objects(convert_numeric=True)
hightestlike = df.sort(['HightestLike'],ascending=[0])
like=['Username','HightestLike']
hightestlike[like].to_csv("TopLike.csv")

df.head()