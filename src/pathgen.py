# Filename: pathgen.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: 
import pandas as pd
import numpy as np
import networkx as nx
import blackbox as bb 

DATA_PATH = "../data/"
OUTPUT_PATH = "../output/"

# Remove NaNs to include dummy values.
train = pd.read_csv(DATA_PATH + "train_data.csv").fillna(-32)

# Oh pandas -- why must you make life so difficult? Let me use dot notation. Please?
# Pretty please with a cherry on top?
recmat = train[['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']].as_matrix()

nodes = list(train.video_id.values)
unodes = {}

for i in range(len(train)):
    unodes[nodes[i]] = i

ctr = 1
# Now let us get the unique video ids from each of the 20 recommendations and put them in our 
# node dictionary.
for i in range(len(train)):
    for j in range(20):
        if not recmat[i][j] == -32:
            if not recmat[i][j] in unodes.keys():
                unodes[recmat[i][j]] = len(train) + ctr
                recmat[i][j] =  unodes[recmat[i][j]]
                ctr += 1
            else:
                recmat[i][j] = unodes[recmat[i][j]]
        else:
            continue
            
reclist = list(recmat)

test = pd.read_csv(DATA_PATH + "test_data.csv")
stn = test[['source','target']].as_matrix()

# Build a graph using the above preprocessed data as nodes
G = nx.MultiGraph()
G.add_nodes_from(list(unodes.values()))

# Now let us add edges.
# TODO: Weigh edges differently based on order of recommendation?
for i in range(len(train)):

    nans = [j for j,k in enumerate([k for k in reclist[i]]) if k == -32]
    node_i= [k for j,k in enumerate([i for l in range(20)]) if j not in nans]
    edge_weights = [x for j,x in enumerate([1]*20) if j not in nans]
    neighbor_i = [x for j,x in enumerate([t for t in reclist[i]]) if j not in nans]
    zipped = zip(node_i, neighbor_i, edge_weights)
    G.add_weighted_edges_from(zipped, weight="weight")


def getScoreForPair(testPair):
    try:
        score = nx.shortest_path_length(G, source = testPair[0], target = testPair[1], weight="weight")
    except nx.NetworkXNoPath:
        # Assign ridiculously high score so we can definitely say it doesn't exist.
        score = 98372
    return score

'''
def main():
    bb.search(f=getScoreForPair,
        box=[],
        n=16,
        it=16,
        cores=64,
        resfile='bestpar.csv')
'''
if __name__ == '__main__':
    # main()
    
ctnlist = list(test.fillna(-32))
scores_csv = np.asarray(list(map(getScoreForPair, ctnlist)))
np.savetxt(OUTPUT_PATH + "scores.csv", scores_csv, delimiter=",")