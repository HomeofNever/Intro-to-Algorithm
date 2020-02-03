from checkpoint1 import ask_array

# Recursively BFS, until the whole graph is done


def bfs(array, visited, queue):
    new_queue = []
    for j in queue:
        if j not in visited:
            visited.append(j)
            for i in range(0, len(array[j])):
                if array[j][i] == 1:
                    new_queue.append(i)
    return new_queue


def pick_node(total_visited, all_nodes):
    difference = all_nodes.difference(total_visited)
    if len(difference) > 0:
        return difference.pop()
    else:
        return -1


def strong_connected(array, thold):
    n = len(array)
    all_nodes = set(range(0, n))
    total_visited = set()
    while True:
        node = pick_node(total_visited, all_nodes)
        if node == -1:
            break
        queue = []
        queue.append(node)
        visited = []
        while len(queue) != 0:
            queue = bfs(array, visited, queue)

        total_visited.update(set(visited))
        if len(visited) >= thold:
            # print("Found Matched SEQ: {}".format(visited))
            return 1

    return 0


if __name__ == '__main__':
    thold = input("threshold (integer): ")
    thold = int(thold)
    print(strong_connected(ask_array(), thold))
