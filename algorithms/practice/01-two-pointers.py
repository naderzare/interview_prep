"""Two-pointer practice. Explain why each pointer move is safe."""


# Question 1: Reverse a list in place.
# Change nums and return None. Example: [1, 2, 3] becomes [3, 2, 1].
def reverse_in_place(nums):
    raise NotImplementedError


# Question 2: Valid palindrome.
# Ignore case and non-alphanumeric characters.
# Example: "A man, a plan, a canal: Panama" -> True
def is_palindrome(s):
    raise NotImplementedError


# Question 3: Merge two sorted lists.
# Return a new sorted list without calling sorted() or list.sort().
# Example: [1, 3, 5], [2, 4] -> [1, 2, 3, 4, 5]
def merge_sorted(a, b):
    raise NotImplementedError


# Question 4: Pair sum in a sorted list.
# Return one pair of indices (i, j), i < j, or None.
# Example: ([1, 2, 4, 7], 9) -> (1, 3)
def two_sum_sorted(nums, target):
    raise NotImplementedError


# Question 5: Move zeros.
# Move all zeros to the end in place while preserving nonzero order.
# Return None. Example: [0, 1, 0, 3] becomes [1, 3, 0, 0].
def move_zeros(nums):
    raise NotImplementedError


# Question 6: Remove duplicates from a sorted list in place.
# Return the count k of distinct values; nums[:k] must contain them.
# Example: [1, 1, 2, 2, 3] -> k=3 and prefix [1, 2, 3]
def unique_prefix_length(nums):
    raise NotImplementedError


# Question 7: Squares of a sorted list.
# Return sorted squares in O(n) time without sorting the result.
# Example: [-4, -1, 0, 3] -> [0, 1, 9, 16]
def sorted_squares(nums):
    raise NotImplementedError


# Question 8: Container with most water.
# Heights at indices i and j hold area min(h[i], h[j]) * (j - i).
# Return the maximum area. Example: [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
def max_container_area(heights):
    raise NotImplementedError


# Question 9: Three sum.
# Return all unique sorted triplets [a, b, c] with a + b + c == 0.
# Output order does not matter. Example: [-1, 0, 1, 2, -1, -4]
# -> [[-1, -1, 2], [-1, 0, 1]]
def three_sum(nums):
    raise NotImplementedError


# Question 10: Trapping rain water.
# Each bar has width 1. Return water trapped after rain.
# Example: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6
def trapped_water(heights):
    raise NotImplementedError


def check_question_1():
    nums = [1, 2, 3]
    assert reverse_in_place(nums) is None
    assert nums == [3, 2, 1]
    empty = []
    reverse_in_place(empty)
    assert empty == []


def check_question_2():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True


def check_question_3():
    assert merge_sorted([1, 3, 5], [2, 4]) == [1, 2, 3, 4, 5]
    assert merge_sorted([], [2]) == [2]
    assert merge_sorted([1, 1], [1]) == [1, 1, 1]


def check_question_4():
    assert two_sum_sorted([1, 2, 4, 7], 9) == (1, 3)
    assert two_sum_sorted([2, 2], 4) == (0, 1)
    assert two_sum_sorted([1, 2], 10) is None


def check_question_5():
    nums = [0, 1, 0, 3]
    assert move_zeros(nums) is None
    assert nums == [1, 3, 0, 0]
    no_zeros = [1, 2]
    move_zeros(no_zeros)
    assert no_zeros == [1, 2]


def check_question_6():
    nums = [1, 1, 2, 2, 3]
    assert unique_prefix_length(nums) == 3
    assert nums[:3] == [1, 2, 3]
    assert unique_prefix_length([]) == 0


def check_question_7():
    assert sorted_squares([-4, -1, 0, 3]) == [0, 1, 9, 16]
    assert sorted_squares([-2, -1]) == [1, 4]
    assert sorted_squares([]) == []


def check_question_8():
    assert max_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_container_area([1, 1]) == 1
    assert max_container_area([1, 2, 1]) == 2


def check_question_9():
    normalize = lambda triplets: sorted(tuple(t) for t in triplets)
    assert normalize(three_sum([-1, 0, 1, 2, -1, -4])) == [(-1, -1, 2), (-1, 0, 1)]
    assert normalize(three_sum([0, 0, 0, 0])) == [(0, 0, 0)]
    assert three_sum([]) == []


def check_question_10():
    assert trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trapped_water([1, 0, 1]) == 1
    assert trapped_water([]) == 0


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
