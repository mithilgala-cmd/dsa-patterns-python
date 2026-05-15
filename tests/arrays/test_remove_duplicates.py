from arrays.remove_duplicates import Solution


def test_remove_duplicates() -> None:
    solution = Solution()
    
    arr1 = [1, 1, 2, 2, 2, 3, 3]
    k1 = solution.solve(arr1)
    assert k1 == 3
    assert arr1[:k1] == [1, 2, 3]
    
    arr2 = [1, 2, 3, 4, 5]
    k2 = solution.solve(arr2)
    assert k2 == 5
    assert arr2[:k2] == [1, 2, 3, 4, 5]
    
    arr3 = [1, 1, 1]
    k3 = solution.solve(arr3)
    assert k3 == 1
    assert arr3[:k3] == [1]
    
    arr4 = []
    k4 = solution.solve(arr4)
    assert k4 == 0
