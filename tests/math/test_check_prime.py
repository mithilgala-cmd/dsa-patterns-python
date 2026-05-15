from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_solution_class() -> type:
    module_path = (
        Path(__file__).resolve().parents[2] / "math" / "check_prime.py"
    )
    spec = spec_from_file_location("a2z_math_check_prime", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


Solution = load_solution_class()


def test_check_prime() -> None:
    solution = Solution()
    
    # Primes
    assert solution.solve(2) is True
    assert solution.solve(3) is True
    assert solution.solve(5) is True
    assert solution.solve(7) is True
    assert solution.solve(11) is True
    assert solution.solve(13) is True
    assert solution.solve(31) is True
    assert solution.solve(97) is True
    
    # Not primes
    assert solution.solve(1) is False
    assert solution.solve(4) is False
    assert solution.solve(6) is False
    assert solution.solve(9) is False
    assert solution.solve(15) is False
    assert solution.solve(100) is False
    assert solution.solve(-7) is False
