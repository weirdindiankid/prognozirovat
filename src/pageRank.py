# Filename: pageRank.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: Calculate the personalised PageRank score given a directed graph around specified starting nodes.
# Reference: http://blog.echen.me/2012/07/31/edge-prediction-in-a-social-graph-my-solution-to-facebooks-user-recommendation-contest-on-kaggle/
import pandas as pd 
import numpy as np 
from followings import *
from followers import *

NumIterations = 3
MaxNodesToKeep = 25

	
def pageRank(user, pfollowers, pfollowings):

	followings = pfollowings
	followers = pfollowers
	probs = {}
	probs[user] = 1 # We start at this user

	pageRankProbs = pageRankHelper(user, probs, NumIterations)

	print("Return " + str(pageRankProbs))

	return pageRankProbs

	# pageRankProbs.toList.sortBy { -_._2 }


def pageRankHelper(start, probs, numIterations, alpha=0.5):
	if numIterations == 0:
		return probs
	else:
		# This map holds the updated set of probabilities after the current iteration.
		probsPropagated = {}  # Map[Int, Double]
		# With prob 1-alpha, teleport back to the start node
		probsPropagated[start] = 1 - alpha
		# Propogate previous probabilities
		for node, prob in probs.items():
			forwards = getFollowings(node)
			backwards = getFollowers(node)

			if len(forwards) != 0 or len(backwards) != 0:
				probToPropagate = alpha * prob / (len(forwards) + len(backwards))
			else:
				probToPropagate = 0

			for neighbor in (list(forwards) + list(backwards)):
				if not neighbor in probsPropagated.keys():
					probsPropagated[neighbor] = 0
				probsPropagated[neighbor] += probToPropagate
	return pageRankHelper(start, probsPropagated, numIterations-1, alpha)

def getFollowers(user):
	if user in followers.keys():
		return followers[user]
	else:
		return set()

def getFollowings(user):
	if user in followings.keys():
		return followings[user]
	else:
		return set()
