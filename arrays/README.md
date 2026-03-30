# 🧠 Arrays

## 📌 What is an Array?
An **array** is a linear data structure that stores elements in a **contiguous block of memory**, allowing:
- **O(1)** access via index
- Efficient traversal
- Predictable memory usage

👉 Arrays are the **foundation of most DSA problems** and often appear in interviews.

---

## 🎯 Why Arrays Matter
- Base for advanced structures (strings, matrices, heaps)
- Used in **sliding window, prefix sum, two pointers**
- Very common in coding interviews (easy → medium → hard progression)

---

## ⚙️ Core Operations & Complexity

| Operation        | Time Complexity |
|----------------|---------------|
| Access         | O(1)          |
| Search         | O(N)          |
| Insert (end)   | O(1) amortized|
| Insert (middle)| O(N)          |
| Delete         | O(N)          |

---

## 🧩 Key Patterns to Master

### 1. Two Pointers
Used when:
- Array is sorted
- Need pair/triplet conditions

**Example Problems:**
- Two Sum (sorted)
- Container With Most Water

---

### 2. Sliding Window
Used for:
- Subarrays
- Maximum/minimum range problems

**Example Problems:**
- Maximum Subarray
- Longest Substring Without Repeating Characters

---

### 3. Prefix Sum
Used when:
- Range sum queries
- Cumulative calculations

**Example Problems:**
- Subarray Sum Equals K

---

### 4. Kadane’s Algorithm
Used for:
- Maximum subarray problems

---

### 5. Hashing with Arrays
Used for:
- Fast lookup (O(1))

---

## ⏳ Complexity Insights

- Most array problems aim for **O(N)** or **O(N log N)**
- Avoid brute force (**O(N²)**) unless necessary
- Always think:
  - Can I reduce nested loops?
  - Can I use extra space for optimization?

---

## 📝 Must-Do Problems (Interview Focused)

### 🟢 Easy
- Two Sum
- Contains Duplicate
- Maximum Subarray

### 🟡 Medium
- Best Time to Buy and Sell Stock
- Product of Array Except Self
- 3Sum

### 🔴 Hard
- Trapping Rain Water
- First Missing Positive

---

## 🚀 How to Practice (Optimized Strategy)

1. **Understand the pattern first**
2. Solve **brute force → optimize**
3. Write clean, readable code
4. Analyze:
   - Time complexity
   - Space complexity
5. Revisit after 2–3 days (spaced repetition)

---

## 🧪 Project Workflow

1. Copy `template.py`
2. Implement solution with:
   - Type hints
   - Edge case handling
3. Add test cases in `tests/`
4. Run:
   ```bash
   python -m pytest
