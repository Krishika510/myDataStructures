import unittest
import Breadthfirst_Search

BFS = Breadthfirst_Search

class breadthFirstSearchTest(unittest.TestCase):
    def test_case(self):
        graph = BFS.Node("A")
        graph.addChild("B").addChild("C").addChild("D")
        graph.children[0].addChild("E").addChild("F")
        graph.children[2].addChild("G").addChild("H")
        graph.children[0].children[1].addChild("I").addChild("J")
        graph.children[2].children[0].addChild("K")
        self.assertEqual(graph.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

if __name__ == '__main__':
    unittest.main()
