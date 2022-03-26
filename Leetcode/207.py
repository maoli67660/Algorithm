from collections import defaultdict

# 2, [[1, 2], [0, 1]
prerequisites = [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 4]]


# 生成邻接表 和 逆邻接表
def init_graph(prerequisites):
    in_dict = defaultdict(list)  # 链接我的的note
    out_dict = defaultdict(list)  # 我去链接的note
    vertex_set = set()
    for pair in prerequisites:
        in_dict[pair[1]].append(pair[0])
        out_dict[pair[0]].append(pair[1])
        vertex_set.add(pair[0])
        vertex_set.add(pair[1])
    return in_dict, out_dict, vertex_set


def canFinish(prerequisites):
    in_dict, out_dict, vertex_set = init_graph(prerequisites)
    print('============ in_dict ================')
    print(in_dict)
    print('============ out_dict ================')
    print(out_dict)

    queue = []
    for current_vertex in vertex_set:
        if current_vertex not in in_dict:
            queue.append(current_vertex)
    print('===== queue ======')
    print(queue)
    count = 0
    while queue:
        current_vertex = queue.pop(0)
        count = count + 1
        for next_vertex in out_dict[current_vertex]:
            in_dict[next_vertex].remove(current_vertex)
            if len(in_dict[next_vertex]) == 0:
                queue.append(next_vertex)

    return count


print(canFinish(prerequisites))
