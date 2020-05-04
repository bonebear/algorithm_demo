# breadth first search
#coding=utf-8

from collections import deque

graph = {}
graph["A"] = ["B", "C", "E"]
graph["B"] = ["C"]
graph["C"] = ["F"]
graph["E"] = ["F"]
graph["F"] = []


def findF(people):
    lianxi_queue = deque()
    lianxi_queue += graph[people]
    checked = []
    while lianxi_queue:
        people = lianxi_queue.popleft()
        if people not in checked:
            if people == "F":
                print "A can find F !"
                return True
            else:
                checked.append(people)
                lianxi_queue += graph[people]



findF("A")
