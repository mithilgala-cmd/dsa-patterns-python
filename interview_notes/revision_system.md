# Revision System

## Rule
- First revisit: 3 days after solving.
- Second revisit: 7 days after first revisit.
- Third revisit: 14 days after second revisit.

## Workflow
1. Solve problem and log it in `problem_tracker.csv`.
2. Set `next_revision_date`.
3. Run `python scripts/revision_queue.py` daily.
4. Re-solve due problems without looking at old code.
5. Update `mistake_tag` and schedule next revisit.
