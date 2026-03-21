import pytest
from arrays.two_sum import Solution

def test_two_sum():
    solution = Solution()
    
    assert sorted(solution.twoSum([2, 7, 11, 15], 9)) == [0, 1]
    assert sorted(solution.twoSum([3, 2, 4], 6)) == [1, 2]
    assert sorted(solution.twoSum([3, 3], 6)) == [0, 1]
    assert solution.twoSum([1, 2, 3], 10) == []
