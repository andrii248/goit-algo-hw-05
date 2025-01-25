# Substring Search Algorithm Performance Analysis

This project compares the efficiency of three substring search algorithms—Knuth-Morris-Pratt (KMP), Boyer-Moore, and Rabin-Karp—on two textual datasets (Article 1 and Article 2). The benchmarks evaluate the execution time of each algorithm for two types of substrings:

1. A substring that **exists** in the text.
2. A substring that **does not exist** in the text.

## Results

### Performance Summary:

- **Fastest Algorithm for Article 1**:  
  Rabin-Karp for an existing substring with a runtime of **0.000273 seconds**.

- **Fastest Algorithm for Article 2**:  
  Rabin-Karp for an existing substring with a runtime of **0.000305 seconds**.

- **Overall Fastest Algorithm**:  
  Rabin-Karp for an existing substring in Article 1 with a runtime of **0.000273 seconds**.

### Observations:

1. The **Rabin-Karp algorithm** consistently outperformed Knuth-Morris-Pratt and Boyer-Moore for existing substrings in both articles.
2. For non-existent substrings, the runtime varied slightly, but Rabin-Karp remained efficient overall.
3. The algorithm's performance might vary for different datasets depending on text size, pattern length, and hash collisions in Rabin-Karp.

## How to Run

1. Clone this repository.
2. Install Python 3.x and ensure `requests` library is available.
3. Execute the script using:
   ```bash
   python substring_search_benchmark.py
   ```
