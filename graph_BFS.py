# breath first search
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

def findF_2(people):
    lianxi_queue = deque()
    lianxi_queue += graph[people]
    path = {}
    path[people] = graph[people]
    checked = []
    count = 0
    step = -1
    while lianxi_queue:
        people = lianxi_queue.popleft()
        # path += people
        if people not in checked:
            if people == "F":
                count += 1
            else:
                step += 1
                checked.append(people)
                lianxi_queue += graph[people]
                path[people] = graph[people]
    print "一共有", count, "条需要",step,"步的最短路径可以找到F"
    print path["A"]




#findF("A")
findF_2("A")
