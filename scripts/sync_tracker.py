import csv
import os
from pathlib import Path

VALID_PATTERNS = {
    "basics", "arrays", "backtracking", "binary_search", "bit_manipulation",
    "bst", "dynamic_programming", "graphs", "greedy", "hashing", "heap",
    "intervals", "linked_list", "math", "math_geometry", "queues", "recursion",
    "sliding_window", "sorting", "stack", "strings", "trees", "trie",
    "two_heaps", "two_pointers", "union_find"
}

def main():
    repo_root = Path(__file__).resolve().parents[1]
    tracker_path = repo_root / "problem_tracker.csv"
    
    # Read existing entries
    existing_problems = {}
    if tracker_path.exists():
        with open(tracker_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                existing_problems[(row['pattern'], row['problem_name'])] = row

    # Scan for python files in pattern folders
    found_problems = []
    for pattern in VALID_PATTERNS:
        pattern_dir = repo_root / pattern
        if not pattern_dir.exists():
            continue
            
        for py_file in pattern_dir.glob("*.py"):
            if py_file.name == "__init__.py":
                continue
                
            problem_name = py_file.stem
            key = (pattern, problem_name)
            
            if key in existing_problems:
                found_problems.append(existing_problems[key])
            else:
                # Add new problem with default values
                found_problems.append({
                    "problem_id": f"scanned_{pattern}_{problem_name}",
                    "pattern": pattern,
                    "problem_name": problem_name,
                    "platform": "LocalScan",
                    "difficulty": "TBD",
                    "status": "solved",
                    "next_revision_date": "",
                    "last_solved_date": "",
                    "notes": "Auto-detected"
                })

    # Sort by pattern and problem_name
    found_problems.sort(key=lambda x: (x['pattern'], x['problem_name']))

    # Write back to CSV
    fieldnames = ["problem_id", "pattern", "problem_name", "platform", "difficulty", "status", "next_revision_date", "last_solved_date", "notes"]
    with open(tracker_path, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(found_problems)
    
    print(f"Synced {len(found_problems)} problems to {tracker_path}")

if __name__ == "__main__":
    main()
