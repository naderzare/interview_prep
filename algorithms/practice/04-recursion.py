"""Recursion practice: linear, branching, divide-and-conquer, memoized."""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Question 1: Countdown.
# Recursively return [n, n-1, ..., 0] for n >= 0. Do not use a loop.
# Example: 3 -> [3, 2, 1, 0]
def countdown(n):
    raise NotImplementedError


# Question 2: Factorial.
# Recursively compute n! for n >= 0; 0! is 1.
# Example: 4 -> 24
def factorial(n):
    raise NotImplementedError


# Question 3: Sum a list.
# Return the sum recursively without using sum() or a loop.
# Example: [3, -1, 4] -> 6; [] -> 0
def recursive_sum(nums):
    raise NotImplementedError


# Question 4: Reverse a string recursively.
# Do not use slicing with a negative step or reversed().
# Example: "code" -> "edoc"
def reverse_string(s):
    raise NotImplementedError


# Question 5: Recursive palindrome check.
# Compare matching ends and recurse on the smaller interior; do not build
# a reversed copy. Example: "racecar" -> True; "robot" -> False
def recursive_palindrome(s):
    raise NotImplementedError


# Question 6: Fast power.
# Return x**n for integer n >= 0 by halving n. Do not call pow() or **.
# Example: (2, 10) -> 1024. Aim for O(log n) recursive calls.
def fast_power(x, n):
    raise NotImplementedError


# Question 7: Flatten nested integers.
# A value is an int or a list of similarly nested values. Return all ints
# in left-to-right order. Example: [1, [2, [3]], 4] -> [1, 2, 3, 4]
def flatten_nested(values):
    raise NotImplementedError


# Question 8: Maximum binary-tree depth.
# An empty tree has depth 0. Combine answers returned by both child calls.
# Example: TreeNode(1, TreeNode(2), TreeNode(3)) -> 2
def tree_depth(root):
    raise NotImplementedError


# Question 9: Merge sort.
# Return a sorted copy using recursive splitting and merging; do not call
# sorted() or list.sort(). Example: [4, 1, 3, 2] -> [1, 2, 3, 4]
def merge_sort(nums):
    raise NotImplementedError


# Question 10: Count grid paths with memoized recursion.
# From (0,0), move only right or down to (rows-1, cols-1). Blocked cells
# contain 1 and open cells 0. The rectangular grid is nonempty.
# Example: [[0,0,0],[0,1,0],[0,0,0]] -> 2
def count_grid_paths(grid):
    raise NotImplementedError


def check_question_1():
    assert countdown(3) == [3, 2, 1, 0]
    assert countdown(0) == [0]


def check_question_2():
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(1) == 1


def check_question_3():
    assert recursive_sum([3, -1, 4]) == 6
    assert recursive_sum([]) == 0


def check_question_4():
    assert reverse_string("code") == "edoc"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def check_question_5():
    assert recursive_palindrome("racecar") is True
    assert recursive_palindrome("robot") is False
    assert recursive_palindrome("") is True


def check_question_6():
    assert fast_power(2, 10) == 1024
    assert fast_power(5, 0) == 1
    assert fast_power(3, 3) == 27


def check_question_7():
    assert flatten_nested([1, [2, [3]], 4]) == [1, 2, 3, 4]
    assert flatten_nested([]) == []
    assert flatten_nested([[], 1, [2]]) == [1, 2]


def check_question_8():
    assert tree_depth(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    assert tree_depth(None) == 0
    assert tree_depth(TreeNode(1, TreeNode(2, TreeNode(3)))) == 3


def check_question_9():
    assert merge_sort([4, 1, 3, 2]) == [1, 2, 3, 4]
    assert merge_sort([]) == []
    assert merge_sort([-1, 3, -1]) == [-1, -1, 3]


def check_question_10():
    assert count_grid_paths([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert count_grid_paths([[0]]) == 1
    assert count_grid_paths([[1]]) == 0


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
