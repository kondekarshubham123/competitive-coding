# Input [(1,8),(2,3),(1,5),(16,17),(2,6),(8,9)]
# Output [(1,8,5,9),(2,3,6),(16,17)]

from collections import defaultdict
graph = defaultdict(list)



def final_func(graph,ke,visited,sub_res):
    for ele in graph[ke]:
        if ele not in visited:
            visited.add(ele)
            sub_res.add(ele)
            final_func(graph,ele,visited,sub_res)
    return sub_res
                


def get_pairs(graph):
    visited = set()
    res = []
    for ke,va in graph.items():
        sub_res = set()
        if ke not in visited:
            sub_res.add(ke)
            res.append(final_func(graph,ke,visited,sub_res))
    return res
    # final_func(graph,visited,res,sub_res)



Input = [(1,8),(2,3),(1,5),(16,17),(2,6),(8,9),(15,16),(6,17)]
for x,y in Input:
    graph[x].append(y)
    graph[y].append(x)
print(get_pairs(graph))