"""	COEN 239 - assignment 2

	Name: Alexander Hadiwijaya (ahadiwijaya)
	Student ID: W1342311
	Source: https://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-minimum-spanning-tree-mst-2/
"""

import math
import sys

inf = float('inf');

# adjacency matrix
A = [
	[0, 1, 1, 1, 1],
	[1, 0, 1, 1, 1],
	[1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1],
	[1, 1, 1, 1, 0]
	]

# cost matrix
C = [
	[inf, 3, 4, 5, 6],
	[3, inf, 1, 4, 2],
	[4, 1, inf, 5, 7],
	[5, 4, 5, inf, 3],
	[6, 2, 7, 3, inf]
	]

# set of edges (pair vertices) in mst
mst = {}
prt = [None] * len(A) # Array to store constructed MST
key = [sys.maxint] * len(A)
mstSet = [False] * len(A)

"""
	Helper function to print MST
"""
def printMst():
	weight = 0;
	print "Edges \t Distance";
	for i in range(1, len(A)):
		print prt[i], " - ", i, "\t", C[i][prt[i]];
		weight += C[i][prt[i]]

	print("MST weight: %d" % weight);

def minKey():
		min_val = sys.maxint
		min_index = -1
 
		for i in range(len(A)):
			if key[i] < min_val and mstSet[i] == False:
				min_val = key[i]
				min_index = i
 
		return min_index

"""
	Minimum Spanning Tree
"""
def mstPrim(parent):
	key[parent] = 0   # Make key 0 so that this vertex is picked as first vertex
	prt[parent] = -1  # First node is always the root of
 
	for i in range(len(A)):
		u = minKey()

		# Put the minimum distance vertex in the shortest path tree
		mstSet[u] = True

		for j in range(len(A)):
			if A[u][j] == 1 and mstSet[j] == False and key[j] > C[u][j]:
					key[j] = C[u][j]
					prt[j] = u

	printMst();

"""
	Input starting vertex
	By default it start from vertex 0
"""
def main(argv):
	parent = 0
	if len(argv) > 1:
		parent = int(argv[1]);

	mstPrim(parent);
	return;

if __name__ == '__main__':
	main(sys.argv);
