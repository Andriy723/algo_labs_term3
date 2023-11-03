import unittest
from src.main import has_cycle
from src.main import main


class TestCycleDetection(unittest.TestCase):
    def test_cycle(self):
        with open('input1.txt', 'r') as input_txt:
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
                    return True
        return False

        self.assertEqual(has_cycle(graph, Node, is_visited, -1), True)

    def test_no_cycle(self):
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
                    return True
        return False

        self.assertEqual(has_cycle(graph, Node, is_visited, -1), False)
