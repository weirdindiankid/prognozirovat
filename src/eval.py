# Filename: eval.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: Final path score evaluator. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.style.use('ggplot')
import csv

DATA_PATH = "../data/"
OUTPUT_PATH = "../output/"

# Get shortest path scores
scores = pd.read_csv(OUTPUT_PATH + "scores.csv")

scores_lst = list(scores.scores.values)

# Remove definitely non-existent data from consideration so we don't skew metrics too bad
cs = scores.loc[scores.scores < 10000]

# Get test dataset
test = pd.read_csv(DATA_PATH + "test_data.csv")

edge_id_lst = list(test.edge_id.values)

# In scores, I have the shortest path from source to target with indices corresponding
# to those in test_data.csv

# Let's analyse the shortest path distribution
# cs.describe()
'''
count    98072.000000
mean         3.924260
std          3.134469
min          0.000000
25%          1.000000
50%          3.000000
75%          7.000000
max         13.000000
Name: scores, dtype: float64
'''

# Let's combine them in a dictionary [edge_id -> shortest_path]
spath = {}

for i in range(len(edge_id_lst)):
	spath[edge_id_lst[i]] = scores_lst[i]

# Now let us see if we can come up with a decent threshold
path_threshold = 4

# This will contain the output we will write
# Haven't figured out how to add headers, so I will manually add those after the CSV is written.
finalDict = {}

for k,v in spath.items():
	if v < path_threshold:
		finalDict[k] = 1
	else:
		finalDict[k] = 0

# Write this out to my CSV
with open(OUTPUT_PATH + "edge_predict.csv", "w") as cfile:
	w = csv.writer(cfile)
	for k,v in finalDict.items():
		w.writerow([k,v])