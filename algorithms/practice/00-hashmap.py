"""Hashmap practice. Solve in order; keep the questions unsolved until you try."""


# Question 1: Contains duplicate.
# Return True if any integer appears more than once.
# Example: [4, 1, 4] -> True; [] -> False
def contains_duplicate(nums):
    raise NotImplementedError


# Question 2: Count words.
# Return a dictionary mapping each word to its number of appearances.
# Example: ["red", "blue", "red"] -> {"red": 2, "blue": 1}
def count_words(words):
    raise NotImplementedError


# Question 3: First unique character.
# Return the index of the first character that occurs once, or -1.
# Example: "leetcode" -> 0; "aabb" -> -1
def first_unique_index(s):
    raise NotImplementedError


# Question 4: Valid anagram.
# Return whether s and t contain exactly the same characters and counts.
# Example: ("listen", "silent") -> True; ("rat", "car") -> False
def is_anagram(s, t):
    raise NotImplementedError


# Question 5: Two sum.
# Return indices (i, j) with i < j and nums[i] + nums[j] == target, or None.
# Example: ([2, 7, 11], 9) -> (0, 1). Do not reuse one index.
def two_sum(nums, target):
    raise NotImplementedError


# Question 6: Group anagrams.
# Group words with identical character counts. Group order does not matter.
# Example: ["eat", "tea", "bat"] -> [["eat", "tea"], ["bat"]]
def group_anagrams(words):
    raise NotImplementedError


# Question 7: Longest consecutive sequence.
# Return the length of the longest run of consecutive values in unsorted nums.
# Aim for O(n) expected time. Example: [100, 4, 200, 1, 3, 2] -> 4
def longest_consecutive(nums):
    raise NotImplementedError


# Question 8: Count subarrays summing to k.
# Count contiguous subarrays whose sum is k; negative numbers are allowed.
# Example: ([1, 2, 1], 3) -> 2
def count_subarrays_sum_k(nums, k):
    raise NotImplementedError


# Question 9: Longest subarray summing to k.
# Return its length, or 0 if none exists. Negative numbers are allowed.
# Example: ([2, -1, 2, 1], 3) -> 3  (the first three values)
def longest_subarray_sum_k(nums, k):
    raise NotImplementedError


# Question 10: Longest balanced binary subarray.
# In an array of only 0s and 1s, find the longest contiguous range with
# equal numbers of 0s and 1s. Example: [0, 1, 0, 0, 1, 1, 0] -> 6
def longest_balanced_binary(nums):
    raise NotImplementedError


def check_question_1():
    assert contains_duplicate([4, 1, 4]) is True
    assert contains_duplicate([4, 1, 2]) is False
    assert contains_duplicate([]) is False


def check_question_2():
    assert count_words(["red", "blue", "red"]) == {"red": 2, "blue": 1}
    assert count_words([]) == {}


def check_question_3():
    assert first_unique_index("leetcode") == 0
    assert first_unique_index("loveleetcode") == 2
    assert first_unique_index("aabb") == -1


def check_question_4():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True


def check_question_5():
    assert two_sum([2, 7, 11], 9) == (0, 1)
    assert two_sum([3, 3], 6) == (0, 1)
    assert two_sum([1, 2], 10) is None


def check_question_6():
    normalize = lambda groups: sorted(sorted(group) for group in groups)
    assert normalize(group_anagrams(["eat", "tea", "bat"])) == [["bat"], ["eat", "tea"]]
    assert normalize(group_anagrams(["a", "a"])) == [["a", "a"]]
    assert group_anagrams([]) == []


def check_question_7():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([1, 2, 0, 1]) == 3
    assert longest_consecutive([]) == 0


def check_question_8():
    assert count_subarrays_sum_k([1, 2, 1], 3) == 2
    assert count_subarrays_sum_k([1, -1, 0], 0) == 3
    assert count_subarrays_sum_k([], 0) == 0


def check_question_9():
    assert longest_subarray_sum_k([2, -1, 2, 1], 3) == 3
    assert longest_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4
    assert longest_subarray_sum_k([], 0) == 0


def check_question_10():
    assert longest_balanced_binary([0, 1, 0, 0, 1, 1, 0]) == 6
    assert longest_balanced_binary([0, 1]) == 2
    assert longest_balanced_binary([0, 0, 0]) == 0


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
