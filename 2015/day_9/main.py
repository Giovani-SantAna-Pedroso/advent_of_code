import sys 
from pprint import pprint


def build_graph(edges):
    graph  = dict()
    for edge in edges:
        pointA, pointB  = edge['nodes']
        if pointA not in graph:
            graph[pointA] = []
        if pointB not in graph:
            graph[pointB] = []

        graph[pointA].append((pointB,int(edge['weight']) ))
        graph[pointB].append((pointA, int(edge['weight']) ))

    return graph

file_name = sys.argv[1]
def parse_line(line):
    line = line.strip()
    cities, weight = line.split('=')
    cities_arr =[ i.strip() for i in  cities.split(" to ")]
    return {'nodes': cities_arr, 'weight':weight}

def dfs_distance():
    ...



with open(file_name, 'r') as file:
    edges =[]
    for line in file:
        parsed_line =parse_line(line)
        edges.append(parsed_line)

    
    graph = build_graph(edges)
    for i in graph:
        print(i)


