from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_solution_class() -> type:
    module_path = Path(__file__).resolve().parents[2] / "math" / "palindrome_number.py"
    spec = spec_from_file_location("a2z_math_palindrome_number", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


Solution = load_solution_class()


def test_palindrome_number_happy_path() -> None:
    solution = Solution()
    assert solution.solution(12321) is True


def test_palindrome_number_non_palindrome() -> None:
    solution = Solution()
    assert solution.solution(12345) is False


def test_palindrome_number_edge_cases() -> None:
    solution = Solution()
    assert solution.solution(0) is True
    assert solution.solution(7) is True


def test_palindrome_number_constraint_negative_value() -> None:
    solution = Solution()
    assert solution.solution(-121) is False
