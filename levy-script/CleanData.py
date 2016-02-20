#!/usr/bin/python3.4

import pandas
import subprocess
import re
import datetime
import time

#Don't forget to remove the file post_time.csv 

def convertToSeconds(timeString):
    """convert a time string into seconds
    """
    x = time.strptime(timeString,'%H:%M:%S');
    return(datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds());

initialStats={};
finalStats={};

attributes=['Tod','Tod0','Dow0','SecondSince0','Like0','Tow','MaxLike','Like','SpeedCom','SpeedLike']


# columns may have to be changed to index
tmp2=pandas.DataFrame(columns=attributes)
tmp2.to_csv('post_time.csv',mode="w+")
maxLike=0

for j in subprocess.getoutput('ls '+'*-*-*.csv').split('\n'):
    try:
        print(j);
        ## Initializing the variables
        #
        tmp=pandas.read_csv(j,sep=';',header=None,index_col=False);
        k=re.split('-(?=[0-9])|\.',j);
        dow=(int(k[3])+31*(k[2]=='01'));#day of the week
        zeros=pandas.DataFrame(0, index = tmp.index , columns=[0]);
        ## Add current value
        #
        tmp['Tod']=[convertToSeconds(s) for s in tmp[1] ];        
        tmp['Like']=tmp[2];
        tmp['Comment']=tmp[3];
        #
        # Now we add lag effect
        #
        if k[0] in initialStats :
            ## We load some previously extracted data
            #
            dow0,tod0,like0,maxLike,com0=initialStats[k[0]];
            ## We update the attributes
            #
            tmp['Doy0']=zeros+dow0;#day of the week of the post was first observed
            tmp['SecondSince0']=tmp['Tod']+((dow-dow0-1))*86400+86400-tod0;#nb of day since the first post
            tmp['Doy']=dow;
            tmp['Tod0']=zeros+tod0;#first time when the post was observed
            tmp['Like0']=zeros+like0;#nb. of like when the first observation was made
            tmp['MaxLike']=zeros+max(maxLike,max(tmp['Like']));
            tmp['Toy']=tmp['Tod']/86400+tmp['Doy'];
            tmp['Comment0']=com0;
            #
            tmp2=pandas.concat([tmp2,tmp],join='inner',ignore_index=True)
            
#            print(j,min(tmp2['Tod']), tod0);
        else:
            if maxLike!=0:
                ## We initialize scale the 
                #   
                L_tmp2=len(tmp2);
                tmp2['MaxLike']=max(tmp2['Like']);
                tmp2['Tow']=tmp2['Toy']%7;
                tmp2['Dow']=tmp2['Doy']%7;
                tmp2['Dow0']=tmp2['Doy0']%7;
                tmp2['SpeedLike']=tmp2['Like'].diff();
                tmp2['SpeedLike'][0]=tmp2['Like'][0];
                tmp2['SpeedCom']=tmp2['Comment'].diff();
                tmp2['SpeedCom'][0]=tmp2['Comment'][0];
                tmp2=tmp2[attributes]
                tmp2.to_csv("post_time.csv",",",mode="a",header=False);
            ## We initialize all the variables
            #   
            maxLike=max(tmp['Like']);
            initialStats[k[0]]=(dow,tmp['Tod'][0],tmp['Like'][0],maxLike,tmp['Comment'][0]);
            dow0,tod0,like0,_,com0=initialStats[k[0]];
            ## We add lag effect
            #
            tmp['Doy']=dow;
            tmp['Doy0']=zeros+dow0;#day of the week of the post was first observed
            tmp['SecondSince0']=tmp['Tod']-tod0;#nb of day since the first post
            tmp['Tod0']=zeros+tod0;#first time when the post was observed
            tmp['Like0']=zeros+like0;#nb. of like when the first observation was made
            tmp['Toy']=tmp['Tod']/86400+tmp['Doy'];
            tmp['MaxLike']=zeros+maxLike;
            tmp['Comment0']=tmp[3][0];
            ## We update as when we have a new post
            #
            tmp2=tmp;
            
    except OSError:
        print('No file');

tmp2['Dow']=tmp2['Doy']%7;
tmp2['Tow']=tmp2['Doy']%7;
tmp2['Dow0']=tmp2['Doy0']%7;
tmp2['SpeedCom']=tmp2['Comment'].diff();
tmp2['SpeedCom'][0]=tmp2['Comment'][0];
tmp2['SpeedLike']=tmp2['Like'].diff();
tmp2['SpeedLike'][0]=tmp2['Like'][0];
tmp2['MaxLike']=max(tmp2['Like']);

tmp2=tmp2[attributes]
tmp2.to_csv("post_time.csv",",",mode="a",header=False);


