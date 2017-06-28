# Filename: naive.py

import pandas as pd 
import numpy as np 
from avail import * # available_targets and available_sources contain
# video ids that are available in our training set
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics.pairwise import cosine_similarity
import scipy as sp 
import networkx as nx

DATA_PATH = "../data/"


train = pd.read_csv(DATA_PATH + "train_data.csv")
tcomplete = pd.read_csv(DATA_PATH + "train_data.csv")

'''
for i in range(1,21):
	del train[str(i)]

del train['uploader']
'''



df = train[train.video_id.isin(available_targets)]
mf = train[train.video_id.isin(available_sources)]
df = df.append(mf, ignore_index=True)


#df.to_csv('../data/testset.csv')

# Tuple (index, video_id)
uid = list(zip(df.index.values, df.video_id.values))
did = {}
for i,j in uid:
	did[j] = i

del df['video_id']

df = pd.get_dummies(df, columns=['category'])


test = pd.read_csv(DATA_PATH + "test_data.csv")
# Probably won't use these.
vid = pd.read_csv(DATA_PATH + "videos_metadata.csv")
users = pd.read_csv(DATA_PATH + "users_metadata.csv", encoding="ISO-8859-1")

