import requests
import timeit

# URLs of the articles
url1 = (
    "https://drive.google.com/uc?export=download&id=18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh"
)
url2 = (
    "https://drive.google.com/uc?export=download&id=18BfXyQcmuinEI_8KDSnQm4bLx6yIFS_w"
)


# Function to download and decode text from a URL
def download_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


# Download the articles
article1 = download_text(url1)
article2 = download_text(url2)


# Knuth-Morris-Pratt (KMP) Algorithm
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  # Match found
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1  # No match found


# Boyer-Moore Algorithm
def boyer_moore_search(text, pattern):
    def bad_character_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - i - 1
        return table

    def good_suffix_table(pattern):
        m = len(pattern)
        table = [0] * m
        last_prefix_position = m
        for i in range(m - 1, -1, -1):
            if pattern[: i + 1] == pattern[m - i - 1 :]:
                last_prefix_position = i + 1
            table[m - i - 1] = last_prefix_position - i + m - 1
        for i in range(m - 1):
            slen = 0
            while slen <= i and pattern[i - slen] == pattern[m - 1 - slen]:
                slen += 1
            if pattern[i - slen] != pattern[m - 1 - slen]:
                table[slen] = m - 1 - i + slen
        return table

    bad_char = bad_character_table(pattern)
    good_suffix = good_suffix_table(pattern)
    i = 0
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1
        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1
        if j < 0:
            return i  # Match found
        else:
            char_shift = bad_char.get(text[i + j], len(pattern))
            suffix_shift = good_suffix[j]
            i += max(char_shift, suffix_shift)
    return -1  # No match found


# Rabin-Karp Algorithm
def rabin_karp_search(text, pattern, prime=101):
    m = len(pattern)
    n = len(text)
    d = 256
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    for i in range(m - 1):
        h = (h * d) % prime

    for i in range(m):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i  # Match found
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t < 0:
                t += prime
    return -1  # No match found


# Substrings for testing
existing_substring1 = article1[:50]  # First 50 characters of article1
nonexistent_substring1 = "this substring does not exist in article1"
existing_substring2 = article2[:50]  # First 50 characters of article2
nonexistent_substring2 = "this substring does not exist in article2"

# Benchmarking with timeit
setup_code = """
from __main__ import kmp_search, boyer_moore_search, rabin_karp_search, article1, article2
"""
test_cases = [
    ("kmp_search(article1, existing_substring1)", "KMP Article 1 Existing"),
    ("kmp_search(article1, nonexistent_substring1)", "KMP Article 1 Non-Existing"),
    ("kmp_search(article2, existing_substring2)", "KMP Article 2 Existing"),
    ("kmp_search(article2, nonexistent_substring2)", "KMP Article 2 Non-Existing"),
    (
        "boyer_moore_search(article1, existing_substring1)",
        "Boyer-Moore Article 1 Existing",
    ),
    (
        "boyer_moore_search(article1, nonexistent_substring1)",
        "Boyer-Moore Article 1 Non-Existing",
    ),
    (
        "boyer_moore_search(article2, existing_substring2)",
        "Boyer-Moore Article 2 Existing",
    ),
    (
        "boyer_moore_search(article2, nonexistent_substring2)",
        "Boyer-Moore Article 2 Non-Existing",
    ),
    (
        "rabin_karp_search(article1, existing_substring1)",
        "Rabin-Karp Article 1 Existing",
    ),
    (
        "rabin_karp_search(article1, nonexistent_substring1)",
        "Rabin-Karp Article 1 Non-Existing",
    ),
    (
        "rabin_karp_search(article2, existing_substring2)",
        "Rabin-Karp Article 2 Existing",
    ),
    (
        "rabin_karp_search(article2, nonexistent_substring2)",
        "Rabin-Karp Article 2 Non-Existing",
    ),
]

# Execute benchmarks
results = {}
for test_case, description in test_cases:
    time_taken = timeit.timeit(
        test_case, setup=setup_code, globals=globals(), number=10
    )
    print(f"{description}: {time_taken:.6f} seconds")
    results[description] = time_taken

# Conclusions
print("\nConclusions:")
for article in ["Article 1", "Article 2"]:
    article_results = {key: value for key, value in results.items() if article in key}
    fastest_algorithm = min(article_results, key=article_results.get)
    print(
        f"Fastest for {article}: {fastest_algorithm} with {results[fastest_algorithm]:.6f} seconds"
    )

overall_fastest = min(results, key=results.get)
print(f"Overall fastest: {overall_fastest} with {results[overall_fastest]:.6f} seconds")
