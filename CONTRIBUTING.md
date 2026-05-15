# Contributing to DSA Patterns

Thank you for your interest in contributing! This project follows a structured workflow to ensure high code quality and consistency.

## 🛠️ Developer Workflow

### 1. Scaffolding a New Problem
Use the provided script to create a new problem module and its corresponding test file.
```bash
python scripts/create_problem.py --pattern <category> --problem <problem_name_snake_case>
```
*Example:* `python scripts/create_problem.py --pattern arrays --problem find_missing_number`

### 2. Implementation Standards
- **Type Safety**: Use Python type hints for all parameters and return types.
- **Documentation**: Include a docstring with the problem description, time complexity, and space complexity.
- **In-Place**: For array problems that specify in-place modification, ensure the original list is modified.

### 3. Testing
We use `pytest` for verification. All new problems must have tests.
```bash
# Run all tests
python -m pytest

# Run specific category
python -m pytest tests/arrays/
```

### 4. Code Quality
We use `ruff` for linting/formatting and `mypy` for type checking.
```bash
python -m ruff check .
python -m mypy .
```

### 5. Syncing Progress
After implementing new problems, run the sync scripts to update the tracker and README dashboard.
```bash
python scripts/sync_tracker.py
python scripts/generate_readme.py
```

## 📂 Project Structure
- `category/`: Implementation of algorithms (e.g., `arrays/`, `sorting/`).
- `tests/category/`: Corresponding unit tests.
- `scripts/`: Automation tools for tracker sync, README generation, and scaffolding.
- `interview_notes/`: Conceptual notes and patterns.
- `problem_tracker.csv`: Centralized tracking of all solved problems.
