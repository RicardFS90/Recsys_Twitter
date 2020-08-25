#Import dependencies
import random 
import pandas as pd 

#Obtain a random sample from the huge .tsv file by skipping random rows
filename = 'training.tsv'

n = 300000000

s = 1000000 #desired sample size

skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list

print(skip)

df = pd.read_csv(filename, skiprows=skip, delimiter='\x01', header=None)

#Defining dataset features as dataset columns
all_features = ["text_ tokens", "hashtags", "tweet_id", "present_media", "present_links", "present_domains",\
                "tweet_type","language", "tweet_timestamp", "engaged_with_user_id", "engaged_with_user_follower_count",\
               "engaged_with_user_following_count", "engaged_with_user_is_verified", "engaged_with_user_account_creation",\
               "engaging_user_id", "engaging_user_follower_count", "engaging_user_following_count", "engaging_user_is_verified",\
               "engaging_user_account_creation", "engagee_follows_engager","reply_timestamp","retweet_timestamp","retweet_with_comment_timestamp","like_timestamp"]

df.columns=all_features

#Export dataframe to .csv file
export_filename = 'tocho2.csv'

df.to_csv(export_filename, encoding='utf-8')
