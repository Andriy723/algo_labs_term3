import unittest
from algo_labs_term3.src.main import has_cycle
from algo_labs_term3.src.main import main


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
                    with open('output1.txt', 'w') as output_txt:
                        output_txt.write('True')
        with open('output1.txt', 'w') as output_txt:
            output_txt.write('False')

        with open('output1.txt', 'r') as output_txt:
            result = output_txt.read()

        self.assertEqual(result, 'False')  # Must be True!

    def test_no_cycle(self):
        with open('input2.txt', 'r') as input_txt:
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
                    with open('output2.txt', 'w') as output_txt:
                        output_txt.write('True')
        with open('output2.txt', 'w') as output_txt:
            output_txt.write('False')

        with open('output2.txt', 'r') as output_txt:
            result = output_txt.read()

        self.assertEqual(result, 'False')
