from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_solution_class() -> type:
    module_path = (
        Path(__file__).resolve().parents[2] / "math" / "armstrong_number.py"
    )
    spec = spec_from_file_location("a2z_math_armstrong_number", module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load module from {module_path}")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution


Solution = load_solution_class()


def test_armstrong_number() -> None:
    solution = Solution()
    
    # Armstrong numbers
    assert solution.solve(1) is True
    assert solution.solve(153) is True
    assert solution.solve(370) is True
    assert solution.solve(371) is True
    assert solution.solve(407) is True
    assert solution.solve(1634) is True
    assert solution.solve(9474) is True
    
    # Not Armstrong numbers
    assert solution.solve(10) is False
    assert solution.solve(152) is False
    assert solution.solve(372) is False
    assert solution.solve(-153) is False
