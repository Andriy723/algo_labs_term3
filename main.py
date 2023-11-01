def main():
    with open('input.txt', 'r') as input_txt:
        graph = {}
        for line in input_txt:
            Node, *neighbors = map(int, line.split())
            graph[Node] = neighbors

    is_visited = {
        Node: False for Node in graph
    }
    for Node in graph:
        if not is_visited[Node]:
            if has_cycle(graph, Node, is_visited, -1):
                with open('output.txt', 'w') as output_txt:
                    output_txt.write('True')
                return
    with open('output.txt', 'w') as output_txt:
        output_txt.write('False')


def has_cycle(graph, Node, is_visited, parent):
    is_visited[Node] = True
    for neighbor in graph[Node]:
        if not is_visited[neighbor]:
            if has_cycle(graph, neighbor, is_visited, Node):
                return True
        elif parent != neighbor:
            return True
    return False

if __name__ == "__main__":
    main()
