import pytest
from sorting.selection_sort import Solution as SelectionSort
from sorting.bubble_sort import Solution as BubbleSort

@pytest.mark.parametrize("solution_class", [SelectionSort, BubbleSort])
def test_sorting_algorithms(solution_class):
    solution = solution_class()
    
    # Test case 1: Regular array
    assert solution.solve([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
    
    # Test case 2: Already sorted
    assert solution.solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 3: Reverse sorted
    assert solution.solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Test case 4: Empty array
    assert solution.solve([]) == []
    
    # Test case 5: Single element
    assert solution.solve([1]) == [1]
    
    # Test case 6: Duplicate elements
    assert solution.solve([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]
