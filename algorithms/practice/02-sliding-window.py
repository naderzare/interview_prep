"""Sliding-window practice. State what the current window represents."""


# Question 1: Maximum sum of k consecutive numbers.
# Return None when k < 1 or k > len(nums).
# Example: ([2, 1, 5, 1, 3], 3) -> 9
def max_sum_length_k(nums, k):
    raise NotImplementedError


# Question 2: Most vowels in a substring of length k.
# Count a, e, i, o, u (lowercase input); 1 <= k <= len(s).
# Example: ("abciiidef", 3) -> 3
def max_vowels(s, k):
    raise NotImplementedError


# Question 3: Find anagram start indices.
# Return every index where a substring of s is an anagram of p.
# s and nonempty p contain lowercase letters.
# Example: ("cbaebabacd", "abc") -> [0, 6]
def anagram_starts(s, p):
    raise NotImplementedError


# Question 4: Longest substring without repeated characters.
# Return its length. Example: "abcabcbb" -> 3; "" -> 0
def longest_unique_substring(s):
    raise NotImplementedError


# Question 5: Longest run of 1s after at most k flips.
# nums contains only 0 and 1. Example: ([1, 1, 0, 0, 1, 1, 1], 1) -> 4
def longest_ones_after_flips(nums, k):
    raise NotImplementedError


# Question 6: Fruit baskets.
# Return the longest contiguous range containing at most two distinct values.
# Example: [1, 2, 1, 3, 3, 2] -> 3
def longest_two_types(items):
    raise NotImplementedError


# Question 7: Shortest positive-number subarray with sum >= target.
# Return its length, or 0 when none exists. All nums are positive.
# Example: (7, [2, 3, 1, 2, 4, 3]) -> 2
def min_length_at_least(target, nums):
    raise NotImplementedError


# Question 8: Does a permutation appear?
# Return whether s2 contains a substring that rearranges all of s1.
# Lowercase letters only. Example: ("ab", "eidbaooo") -> True
def contains_permutation(s1, s2):
    raise NotImplementedError


# Question 9: Longest uniform substring after at most k replacements.
# s contains uppercase letters. Change at most k characters in one substring
# so all its characters match. Example: ("AABABBA", 1) -> 4
def longest_replacement(s, k):
    raise NotImplementedError


# Question 10: Minimum window containing all required characters.
# Return the shortest substring of s containing t's characters with counts;
# return "" if impossible. Example: ("ADOBECODEBANC", "ABC") -> "BANC"
def min_covering_window(s, t):
    raise NotImplementedError


def check_question_1():
    assert max_sum_length_k([2, 1, 5, 1, 3], 3) == 9
    assert max_sum_length_k([-2, -1, -3], 2) == -3
    assert max_sum_length_k([1, 2], 3) is None


def check_question_2():
    assert max_vowels("abciiidef", 3) == 3
    assert max_vowels("aei", 2) == 2
    assert max_vowels("xyz", 2) == 0


def check_question_3():
    assert anagram_starts("cbaebabacd", "abc") == [0, 6]
    assert anagram_starts("abab", "ab") == [0, 1, 2]
    assert anagram_starts("a", "aa") == []


def check_question_4():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("") == 0


def check_question_5():
    assert longest_ones_after_flips([1, 1, 0, 0, 1, 1, 1], 1) == 4
    assert longest_ones_after_flips([0, 0], 0) == 0
    assert longest_ones_after_flips([1, 0, 1], 1) == 3


def check_question_6():
    assert longest_two_types([1, 2, 1, 3, 3, 2]) == 3
    assert longest_two_types([1, 2, 3, 2, 2]) == 4
    assert longest_two_types([]) == 0


def check_question_7():
    assert min_length_at_least(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_length_at_least(4, [1, 1, 1]) == 0
    assert min_length_at_least(3, [3]) == 1


def check_question_8():
    assert contains_permutation("ab", "eidbaooo") is True
    assert contains_permutation("ab", "eidboaoo") is False
    assert contains_permutation("a", "a") is True


def check_question_9():
    assert longest_replacement("AABABBA", 1) == 4
    assert longest_replacement("ABAB", 2) == 4
    assert longest_replacement("ABCDE", 1) == 2


def check_question_10():
    assert min_covering_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_covering_window("a", "aa") == ""
    assert min_covering_window("aa", "aa") == "aa"


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
