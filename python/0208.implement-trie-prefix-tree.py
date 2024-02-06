#  Category: algorithms
#  Level: Medium
#  Percent: 64.55284%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
#  Implement the Trie class:
#
#
#  	Trie() Initializes the trie object.
#  	void insert(String word) Inserts the string word into the trie.
#  	boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#  	boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
#
#  Example 1:
#
#  Input
#  ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#  [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#  Output
#  [null, null, true, false, true, null, true]
#
#  Explanation
#  Trie trie = new Trie();
#  trie.insert("apple");
#  trie.search("apple");   // return True
#  trie.search("app");     // return False
#  trie.startsWith("app"); // return True
#  trie.insert("app");
#  trie.search("app");     // return True
#
#
#
#  Constraints:
#
#
#  	1 <= word.length, prefix.length <= 2000
#  	word and prefix consist only of lowercase English letters.
#  	At most 3 * 10⁴ calls in total will be made to insert, search, and startsWith.
#


import unittest

DUMMY = None

#  start_marker
from collections import defaultdict


class Trie:

    def __init__(self):
        self.trie = defaultdict(dict)

    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if c not in trie:
                trie[c] = {}
            trie = trie[c]
        trie["_"] = {}

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return "_" in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
#  end_marker
class TestSolution(unittest.TestCase):
    def test_case_1(self):
        input = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
        expected = [None, None, True, False, True, None, True]
        trie = Trie()
        result = [
            None,
            trie.insert("apple"),
            trie.search("apple"),
            trie.search("app"),
            trie.startsWith("app"),
            trie.insert("app"),
            trie.search("app"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
