if __name__ == '__main__':
    input = open("graph.txt")
    graph = {}
    duration = {}

    max_time = 0
    visited_nodes = {}
    earliest_time = {}
    latest_time = {}
    critical_path = []
    vertex = []
    gap = {}

    for inputs in input:
        node, prerequesite, time = inputs.split()
        if int(time) > 0:
            duration[node] = time

        if prerequesite != ';':
            if node not in graph:
                graph[node] = [prerequesite]
            else:
                graph[node].append(prerequesite)

        else:
            graph[node] = prerequesite

    for node in graph:
        timer = 0

        for node_content in graph[node]:
            if len(graph[node]) <= 1:
                if(node_content == ';'):
                    visited_nodes[node] = duration[node]
                    earliest_time[node] = duration[node]
                elif node_content in visited_nodes:
                    visited_nodes[node] = (int(duration[node]) + int(visited_nodes[node_content]))
                    earliest_time[node] = visited_nodes[node]
            else:
                if timer == 0:
                    visited_nodes[node] = (int(duration[node]) + int(visited_nodes[node_content]))
                    earliest_time[node] = visited_nodes[node]
                    timer = visited_nodes[node]
                else:
                    if (int(duration[node]) + int(visited_nodes[node_content])) > timer:
                        visited_nodes[node] = (int(duration[node]) + int(visited_nodes[node_content]))
                        earliest_time[node] = visited_nodes[node]
                        timer = visited_nodes[node]

    for node in visited_nodes:
        if max_time < int(visited_nodes[node]):
            max_time = int(visited_nodes[node])

    for node in reversed(graph):
        aux = True
        for aux_node in graph:
            for node_content in graph[aux_node]:
                if(node == node_content):
                    if node not in vertex:
                        latest_time[node] = (int(latest_time[aux_node]) - int(duration[aux_node]))
                        aux = False
                        vertex.append(node)
                    else:
                        latest_time[node] = min((int(latest_time[aux_node]) - int(duration[aux_node])), latest_time[node])

        if(aux == True):
            latest_time[node] = max_time

    for node in graph:
        if(int(earliest_time[node]) == int(latest_time[node])):
            critical_path.append(node)
        else:
            gap[node] = (int(latest_time[node]) - int(earliest_time[node]))

    print(f'Total time: {max_time}')
    print(f'Critical Path: {critical_path}')
    print(f'Gaps: {gap}')