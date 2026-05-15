from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_solution_class() -> type:
    module_path = (
        Path(__file__).resolve().parents[2] / "math" / "print_divisors.py"
    )
    spec = spec_from_file_location("a2z_math_print_divisors", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


Solution = load_solution_class()


def test_print_divisors() -> None:
    solution = Solution()
    
    assert solution.solve(1) == [1]
    assert solution.solve(12) == [1, 2, 3, 4, 6, 12]
    assert solution.solve(15) == [1, 3, 5, 15]
    assert solution.solve(25) == [1, 5, 25]
    assert solution.solve(31) == [1, 31]
    assert solution.solve(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36]
