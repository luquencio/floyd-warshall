# This is an easy floyd warshall implementation on python
#I Tried to make this algorithm closest to the real way to do it

def floydwarshall(graph):

    # Initialize distance and predesessor:
    # copy graph into distance,adding infinite where there is
    # no edge, and 0 in the diagonal
    distance = {}
    predesessor = {}
    for u in graph:
        distance[u] = {}
        predesessor[u] = {}
        for v in graph:
            distance[u][v] = 1000
            predesessor[u][v] = -1
        distance[u][u] = 0
        for neighbor in graph[u]:
            distance[u][neighbor] = graph[u][neighbor]
            predesessor[u][neighbor] = u

    for t in graph:
        # with a distance u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdistance = distance[u][t] + distance[t][v]
                if newdistance < distance[u][v]: ##Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
                    distance[u][v] = newdistance
                    predesessor[u][v] = predesessor[t][v] # make a new route through t

    return distance, predesessor



graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}

distance, predesessor = floydwarshall(graph)
print "predesessorecesors in shortest path:"
for v in predesessor: print "%s: %s" % (v, predesessor[v])
print "Shortest distanceance from each vertex"
for v in distance: print "%s: %s" % (v, distance[v])

'''
predesessorecesors in shortest_path:
0: {0: -1, 1: 0, 2: 0, 3: 2, 4: 1, 5: 4}
1: {0: -1, 1: -1, 2: 5, 3: 5, 4: 1, 5: 4}
2: {0: -1, 1: -1, 2: -1, 3: 2, 4: -1, 5: -1}
3: {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1}
4: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: 4}
5: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: -1}

Shortest distanceance from each vertex:
0: {0: 0, 1: 6, 2: 8, 3: 17, 4: 17, 5: 20}
1: {0: 1000, 1: 0, 2: 21, 3: 18, 4: 11, 5: 14}
2: {0: 1000, 1: 1000, 2: 0, 3: 9, 4: 1000, 5: 1000}
3: {0: 1000, 1: 1000, 2: 1000, 3: 0, 4: 1000, 5: 1000}
4: {0: 1000, 1: 1000, 2: 10, 3: 7, 4: 0, 5: 3}
5: {0: 1000, 1: 1000, 2: 7, 3: 4, 4: 1000, 5: 0}
'''
