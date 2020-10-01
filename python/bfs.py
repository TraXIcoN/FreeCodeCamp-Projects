# Programmer: Sahil Bairagi
# A BFS algorithm and a function to find path of one vertex to another using bfs in a graph

from queue import Queue

def bfs(graph, start, end):
  q = Queue()
  q.put(start)
  pred = {}
  while not q.empty() and end not in pred:
    node = q.get()
    for next in graph[node]:
      if next not in pred:
        q.put(next)
        pred[next] = node
  return pred

def find_path(graph, start, end):
  pred = bfs(graph, start, end)
  path = []
  if end in pred:
    path = [end]
    vertex = end
    while vertex != start:
      vertex = pred[vertex]
      path = [vertex] + path
  return path
