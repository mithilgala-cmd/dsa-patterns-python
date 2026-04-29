from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_solution_class() -> type:
    module_path = Path(__file__).resolve().parents[2] / "math" / "gcd_or_hcf.py"
    spec = spec_from_file_location("a2z_math_gcd_or_hcf", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


Solution = load_solution_class()


def test_gcd_or_hcf_happy_path() -> None:
    solution = Solution()
    assert solution.solution(48, 18) == 6


def test_gcd_or_hcf_coprime_numbers() -> None:
    solution = Solution()
    assert solution.solution(35, 64) == 1


def test_gcd_or_hcf_edge_cases_with_zero() -> None:
    solution = Solution()
    assert solution.solution(0, 5) == 5
    assert solution.solution(0, 0) == 0


def test_gcd_or_hcf_constraints_and_signs() -> None:
    solution = Solution()
    assert solution.solution(-24, 60) == 12
    assert solution.solution(10**9, 10**6) == 10**6


def test_gcd_or_hcf_brute_force_matches_optimal() -> None:
    solution = Solution()
    assert solution.solution_brute_force(270, 192) == solution.solution(270, 192)
