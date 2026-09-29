"""Binary-search practice. Write the search interval before each solution."""


# Question 1: Exact search.
# Return target's index in a sorted list of distinct integers, or -1.
# Example: ([1, 3, 5, 8], 5) -> 2
def binary_search(nums, target):
    raise NotImplementedError


# Question 2: Search insert position.
# Return the first index where target could be inserted without breaking order.
# Example: ([1, 3, 3, 7], 4) -> 3; target 3 -> 1
def search_insert(nums, target):
    raise NotImplementedError


# Question 3: First occurrence.
# Return the first index of target in a sorted list, or -1.
# Example: ([1, 2, 2, 2, 4], 2) -> 1
def first_occurrence(nums, target):
    raise NotImplementedError


# Question 4: Last occurrence.
# Return the last index of target in a sorted list, or -1.
# Example: ([1, 2, 2, 2, 4], 2) -> 3
def last_occurrence(nums, target):
    raise NotImplementedError


# Question 5: Integer square root.
# For nonnegative n, return floor(sqrt(n)) without using sqrt or **0.5.
# Example: 8 -> 2; 16 -> 4
def integer_sqrt(n):
    raise NotImplementedError


# Question 6: Search a rotated sorted list.
# A distinct, sorted list was rotated at an unknown point. Return target's
# index, or -1. Example: ([4, 5, 6, 1, 2, 3], 2) -> 4
def search_rotated(nums, target):
    raise NotImplementedError


# Question 7: Minimum in a rotated sorted list.
# Values are distinct; return None for empty input.
# Example: [5, 6, 1, 2, 3, 4] -> 1
def min_rotated(nums):
    raise NotImplementedError


# Question 8: Find a peak index.
# Return any i whose value is greater than its existing neighbors.
# nums is nonempty and adjacent values differ; treat outside as -infinity.
# Example: [1, 2, 3, 1] -> 2
def peak_index(nums):
    raise NotImplementedError


# Question 9: Koko eating bananas.
# Each hour, eat up to speed bananas from one pile. Return the smallest
# integer speed that finishes all piles in h hours. Assume h >= len(piles).
# Example: ([3, 6, 7, 11], 8) -> 4
def min_eating_speed(piles, h):
    raise NotImplementedError


# Question 10: Split array largest sum.
# Split nonnegative, nonempty nums into exactly k nonempty contiguous parts,
# with 1 <= k <= len(nums). Minimize
# the largest part sum. Example: ([7, 2, 5, 10, 8], 2) -> 18
def split_array_min_largest_sum(nums, k):
    raise NotImplementedError


def check_question_1():
    assert binary_search([1, 3, 5, 8], 5) == 2
    assert binary_search([1, 3, 5, 8], 4) == -1
    assert binary_search([], 4) == -1


def check_question_2():
    assert search_insert([1, 3, 3, 7], 4) == 3
    assert search_insert([1, 3, 3, 7], 3) == 1
    assert search_insert([], 3) == 0


def check_question_3():
    assert first_occurrence([1, 2, 2, 2, 4], 2) == 1
    assert first_occurrence([1, 2, 2, 2, 4], 3) == -1
    assert first_occurrence([], 2) == -1


def check_question_4():
    assert last_occurrence([1, 2, 2, 2, 4], 2) == 3
    assert last_occurrence([1, 2, 2, 2, 4], 3) == -1
    assert last_occurrence([2], 2) == 0


def check_question_5():
    assert integer_sqrt(8) == 2
    assert integer_sqrt(16) == 4
    assert integer_sqrt(0) == 0


def check_question_6():
    assert search_rotated([4, 5, 6, 1, 2, 3], 2) == 4
    assert search_rotated([4, 5, 6, 1, 2, 3], 7) == -1
    assert search_rotated([1], 1) == 0


def check_question_7():
    assert min_rotated([5, 6, 1, 2, 3, 4]) == 1
    assert min_rotated([1, 2, 3]) == 1
    assert min_rotated([]) is None


def check_question_8():
    assert peak_index([1, 2, 3, 1]) == 2
    assert peak_index([2, 1]) == 0
    assert peak_index([1, 2]) == 1


def check_question_9():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([1], 1) == 1


def check_question_10():
    assert split_array_min_largest_sum([7, 2, 5, 10, 8], 2) == 18
    assert split_array_min_largest_sum([1, 2, 3, 4, 5], 2) == 9
    assert split_array_min_largest_sum([1, 4, 4], 3) == 4


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
