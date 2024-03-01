#  Category: algorithms
#  Level: Medium
#  Percent: 46.487854%
# pylint: enable=useless-suppression
# pylint: disable=invalid-name, line-too-long, too-few-public-methods
# pylint: disable=missing-class-docstring, missing-function-docstring, missing-module-docstring


#  You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
#
#  You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
#
#
#  	For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
#
#
#
#  Example 1:
#
#  Input
#  ["Solution","pickIndex"]
#  [[[1]],[]]
#  Output
#  [null,0]
#
#  Explanation
#  Solution solution = new Solution([1]);
#  solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
#
#
#  Example 2:
#
#  Input
#  ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
#  [[[1,3]],[],[],[],[],[]]
#  Output
#  [null,1,1,1,1,0]
#
#  Explanation
#  Solution solution = new Solution([1, 3]);
#  solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
#  solution.pickIndex(); // return 1
#  solution.pickIndex(); // return 1
#  solution.pickIndex(); // return 1
#  solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.
#
#  Since this is a randomization problem, multiple answers are allowed.
#  All of the following outputs can be considered correct:
#  [null,1,1,1,1,0]
#  [null,1,1,1,1,1]
#  [null,1,1,1,0,0]
#  [null,1,1,1,0,1]
#  [null,1,0,1,0,0]
#  ......
#  and so on.
#
#
#
#  Constraints:
#
#
#  	1 <= w.length <= 10⁴
#  	1 <= w[i] <= 10⁵
#  	pickIndex will be called at most 10⁴ times.
#
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


import random
import unittest
from bisect import bisect_left
from collections import Counter
from typing import List


#  start_marker
class Solution:
    def __init__(self, w: List[int]):
        self._w = []
        self._lenw = sum(w)
        sumw = 0
        for wgt in w:
            sumw += wgt
            self._w.append(sumw)

    def pickIndex(self) -> int:
        val = random.randint(1, self._lenw)
        return bisect_left(self._w, val)


#  end_marker


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = Solution([3, 14, 1, 7])
        # this test is not deterministic, so it is not guaranteed to pass
        cnt = Counter()
        for _ in range(100000):
            n = s.pickIndex()
            cnt[n] += 1
        self.assertAlmostEqual(cnt[0] / 100000, 3 / 25, delta=0.005)
        self.assertAlmostEqual(cnt[1] / 100000, 14 / 25, delta=0.005)
        self.assertAlmostEqual(cnt[2] / 100000, 1 / 25, delta=0.005)
        self.assertAlmostEqual(cnt[3] / 100000, 7 / 25, delta=0.005)


if __name__ == "__main__":
    unittest.main()
