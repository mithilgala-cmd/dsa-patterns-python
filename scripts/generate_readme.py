import csv
import re
from pathlib import Path

def generate_progress_bar(percentage):
    length = 20
    filled = int(length * percentage / 100)
    return "█" * filled + "░" * (length - filled)

def main():
    repo_root = Path(__file__).resolve().parents[1]
    tracker_path = repo_root / "problem_tracker.csv"
    readme_path = repo_root / "README.md"
    
    problems = []
    if tracker_path.exists():
        with open(tracker_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            problems = list(reader)

    total_solved = len(problems)
    patterns = {}
    for p in problems:
        patterns[p['pattern']] = patterns.get(p['pattern'], 0) + 1

    # Define Roadmap Order (Striver A2Z)
    roadmap = [
        ("Step 1: Basics", ["basics", "math", "recursion"]),
        ("Step 2: Sorting", ["sorting"]),
        ("Step 3: Arrays", ["arrays"]),
        ("Step 4: Binary Search", ["binary_search"]),
        ("Step 5: Strings", ["strings"]),
        ("Step 6: Linked List", ["linked_list"]),
        ("Step 7: Recursion (Adv)", []), # Placeholder
        ("Step 8: Bit Manipulation", ["bit_manipulation"]),
        ("Step 9: Stack & Queue", ["stack", "queues"]),
        ("Step 10: Sliding Window & Two Pointers", ["sliding_window", "two_pointers"]),
        ("Step 11: Heaps", ["heap", "two_heaps"]),
        ("Step 12: Greedy", ["greedy"]),
        ("Step 13: Trees", ["trees"]),
        ("Step 14: BST", ["bst"]),
        ("Step 15: Graphs", ["graphs"]),
        ("Step 16: Dynamic Programming", ["dynamic_programming"]),
        ("Step 17: Trie", ["trie"]),
    ]

    stats_md = "## 📊 Progress Dashboard\n\n"
    stats_md += f"**Total Problems Solved:** `{total_solved}`\n\n"
    
    for step_name, folders in roadmap:
        step_solved = sum(patterns.get(f, 0) for f in folders)
        # Assuming some target for each step to show progress, or just show count
        # For now, just show count
        stats_md += f"- **{step_name}**: `{step_solved}` solved\n"

    # Update README.md
    if readme_path.exists():
        content = readme_path.read_text(encoding='utf-8')
        
        # Replace the "Current solved snapshot" section or create a dashboard section
        # For simplicity, we'll look for a marker or just rewrite parts of it
        # Let's try to find a dashboard section or insert it after the title
        
        marker_start = "<!-- DASHBOARD_START -->"
        marker_end = "<!-- DASHBOARD_END -->"
        
        new_dashboard = f"{marker_start}\n{stats_md}\n{marker_end}"
        
        if marker_start in content and marker_end in content:
            content = re.sub(f"{marker_start}.*?{marker_end}", new_dashboard, content, flags=re.DOTALL)
        else:
            # Insert after the first header
            content = content.replace("# DSA Patterns in Python (Placement 2027)\n", f"# DSA Patterns in Python (Placement 2027)\n\n{new_dashboard}\n")

        # Also update the Solved Snapshot list
        snapshot_md = "## 📂 Solved Problems Snapshot\n\n"
        for pattern in sorted(patterns.keys()):
            p_problems = [p['problem_name'] for p in problems if p['pattern'] == pattern]
            snapshot_md += f"- **`{pattern}/`**: {', '.join([f'`{name}.py`' for name in p_problems])}\n"
            
        marker_s_start = "<!-- SNAPSHOT_START -->"
        marker_s_end = "<!-- SNAPSHOT_END -->"
        new_snapshot = f"{marker_s_start}\n{snapshot_md}\n{marker_s_end}"
        
        if marker_s_start in content and marker_s_end in content:
            content = re.sub(f"{marker_s_start}.*?{marker_s_end}", new_snapshot, content, flags=re.DOTALL)
        else:
            # Replace the old section if it exists
            if "## Current solved snapshot" in content:
                # Find the next header or end of file
                lines = content.split('\n')
                start_idx = -1
                end_idx = len(lines)
                for i, line in enumerate(lines):
                    if line.startswith("## Current solved snapshot"):
                        start_idx = i
                    elif start_idx != -1 and line.startswith("## "):
                        end_idx = i
                        break
                
                if start_idx != -1:
                    lines[start_idx:end_idx] = [new_snapshot]
                    content = '\n'.join(lines)
            else:
                content += f"\n\n{new_snapshot}"

        readme_path.write_text(content, encoding='utf-8')
        print(f"Updated {readme_path}")

if __name__ == "__main__":
    main()
