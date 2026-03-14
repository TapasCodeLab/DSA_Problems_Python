from typing import List

# Using Set
# class Solution:
#     def removeSubfolders(self, folder: List[str]) -> List[str]:
#         folder.sort(key=lambda x: len(x))
#         present = set(folder)
#
#         def is_sub_folder(name):
#             structure = list(name.split('/'))
#             for i in range(len(structure)):
#                 if '/'.join(structure[:i]) in present:
#                     return True
#             return False
#
#         res = []
#         for f in folder:
#             if not is_sub_folder(f):
#                 res.append(f)
#
#         return res


#trie approach

class node:
    def __init__(self):
        self.folders = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = node()
        folder.sort()
        res = []
        root.folders[''] = node()
        for current in folder:
            directories = current.split("/")
            head = root
            for directory in directories:
                if directory not in head.folders:
                    head.folders[directory] = node()
                head = head.folders[directory]
                if head.end:
                    break
            else:
                head.end = True
                res.append(current)
        return res

import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def testcase1(self):
        self.assertEqual(self.solution.removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]), ["/a","/c/d","/c/f"])

    def testcase2(self):
        self.assertEqual(self.solution.removeSubfolders(["/a","/a/b/c","/a/b/d"]), ["/a"])

    def testcase3(self):
        self.assertIn(self.solution.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]), [["/a/b/c","/a/b/d","/a/b/ca"],["/a/b/c","/a/b/ca","/a/b/d"]])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()