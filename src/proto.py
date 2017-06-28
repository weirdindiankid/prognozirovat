# Filename: proto.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: Prototyping and some random experiments.
import pandas as pd 
import numpy as np 
import csv

DATA_PATH = "../data/"
TRAIN_PATH = DATA_PATH + "train_data.csv"

train = pd.read_csv(TRAIN_PATH)

fdict = {}

'''
for i in train.index:
	# Get vid id
	a = train.ix[i].video_id
	# Get list of vids recommended for this video
	ival = [str(m) for m in list(train.ix[i].values[9:]) if str(m) != 'nan']

	if a in fdict.keys():
		fdict[a].append(ival)
	else:
		fdict[a] = ival

with open("followers.py", "w") as f:
	f.write(str(fdict))

'''

for i in train.index:
	a = train
	b = train.ix[i].video_id
	c = a.loc[(a['1'] == b) | (a['2'] == b) |(a['3'] == b) |(a['4'] == b) |(a['5'] == b) |(a['6'] == b) |(a['7'] == b) |(a['8'] == b) |(a['9'] == b) | (a['10'] == b) | (a['11'] == b) | (a['12'] == b) | (a['13'] == b) | (a['14'] == b) | (a['15'] == b) | (a['16'] == b) | (a['17'] == b) | (a['18'] == b) | (a['19'] == b) | (a['20'] == b)]
	c = list(c.video_id.values)
	fdict[b] = c
'''
with open("followings.py", "w") as f:
	f.write(str(fdict))
#c = a.loc[(a['1'] == b) | (a['2'] == b) |(a['3'] == b) |(a['4'] == b) |(a['5'] == b) |(a['6'] == b) |(a['7'] == b) |(a['8'] == b) |(a['9'] == b) | (a['10'] == b) | (a['11'] == b) | (a['12'] == b) | (a['13'] == b) | (a['14'] == b) | (a['15'] == b) | (a['16'] == b) | (a['17'] == b) | (a['18'] == b) | (a['19'] == b) | (a['20'] == b)]
'''
