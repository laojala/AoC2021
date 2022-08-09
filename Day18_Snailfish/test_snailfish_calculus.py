import unittest
import snailfish_calculus as sn

data = ['[', '[', 1, ',', 2, ']', ',', '[', '[', 3, ',', 4, ']', ',', 5, ']', ']']


class TestSnailFishCalculus(unittest.TestCase):

    def test_addition(self):
        test_addition = sn.read_file("test/addition.data")
        self.assertEqual((sn.add(test_addition[0], test_addition[1])), data)

    def test_out(self):
        self.assertEqual(sn.out(data), "[[1,2],[[3,4],5]]")

    def test_item_to_list(self):
        self.assertEqual(sn.item_to_list("[[1,2],[[3,4],5]]"), data)

    def test_explode(self):
        self.assertEqual(1, 1)
    # [[[[[9, 8], 1], 2], 3], 4]
    # becomes[[[[0, 9], 2], 3], 4]