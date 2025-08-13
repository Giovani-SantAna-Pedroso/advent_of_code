# https://www.youtube.com/watch?v=seDbFvnidnw&t=31s
from pprint import pprint
def buildgraph(edges):
    graph  = dict()
    for edge in edges:
        pointA, pointB = edge
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []

        graph[pointA].append(pointB)
        graph[pointB].append(pointA)

    pprint(graph)
    return graph



edges = [['i','j'],
        ['k','i'],
         ['m','k'],
         ['k','l'],
         ['o','n'],
         ]

buildgraph(edges)
