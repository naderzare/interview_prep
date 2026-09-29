"""Dynamic-programming practice. Define the state before its recurrence."""


# Question 1: Fibonacci.
# Return F(n) with F(0)=0, F(1)=1. Avoid repeated work.
# Example: F(7) -> 13
def fibonacci(n):
    raise NotImplementedError


# Question 2: Climbing stairs.
# Take 1 or 2 steps at a time; return the number of ways to reach step n.
# n >= 0, and there is one way to stay at step 0. Example: n=4 -> 5
def climb_stairs(n):
    raise NotImplementedError


# Question 3: Minimum cost climbing stairs.
# cost[i] is paid when stepping on stair i. Start at stair 0 or 1 and move
# 1 or 2 steps; the top is past the final stair. Assume at least 2 stairs.
# Example: [10,15,20] -> 15
def min_cost_climbing(cost):
    raise NotImplementedError


# Question 4: House robber.
# Choose nonadjacent houses for maximum total; empty choice is allowed.
# Example: [2, 7, 9, 3, 1] -> 12
def house_robber(nums):
    raise NotImplementedError


# Question 5: Minimum coins.
# Coins can be reused. Return the fewest coins adding to amount, or -1.
# Example: ([1, 2, 5], 11) -> 3; ([2], 3) -> -1
def min_coins(coins, amount):
    raise NotImplementedError


# Question 6: Unique paths with obstacles.
# Start top-left and move only right/down to bottom-right; 1 means blocked.
# The rectangular grid is nonempty. Return 0 if start or end is blocked.
# Example:
# [[0,0,0],[0,1,0],[0,0,0]] -> 2
def unique_paths_with_obstacles(grid):
    raise NotImplementedError


# Question 7: Longest increasing subsequence.
# A subsequence may skip items but keeps their order. Return its length.
# An O(n²) DP is fine. Example: [10,9,2,5,3,7,101,18] -> 4
def lis_length(nums):
    raise NotImplementedError


# Question 8: Equal subset partition.
# Can nonnegative nums be divided into two subsets with equal sums?
# Example: [1, 5, 11, 5] -> True; [1, 2, 3, 5] -> False
def can_partition_equal(nums):
    raise NotImplementedError


# Question 9: Longest common subsequence.
# Return the length of the longest sequence in both strings (not necessarily
# contiguous). Example: ("abcde", "ace") -> 3
def lcs_length(a, b):
    raise NotImplementedError


# Question 10: Edit distance.
# Return the minimum single-character inserts, deletes, and replacements
# to change a into b. Example: ("horse", "ros") -> 3
def edit_distance(a, b):
    raise NotImplementedError


def check_question_1():
    assert fibonacci(7) == 13
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1


def check_question_2():
    assert climb_stairs(4) == 5
    assert climb_stairs(0) == 1
    assert climb_stairs(1) == 1


def check_question_3():
    assert min_cost_climbing([10, 15, 20]) == 15
    assert min_cost_climbing([10, 15]) == 10
    assert min_cost_climbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


def check_question_4():
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert house_robber([]) == 0
    assert house_robber([5, 1, 1, 5]) == 10


def check_question_5():
    assert min_coins([1, 2, 5], 11) == 3
    assert min_coins([2], 3) == -1
    assert min_coins([1], 0) == 0


def check_question_6():
    assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths_with_obstacles([[0]]) == 1
    assert unique_paths_with_obstacles([[1]]) == 0


def check_question_7():
    assert lis_length([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lis_length([]) == 0
    assert lis_length([3, 2, 1]) == 1


def check_question_8():
    assert can_partition_equal([1, 5, 11, 5]) is True
    assert can_partition_equal([1, 2, 3, 5]) is False
    assert can_partition_equal([]) is True


def check_question_9():
    assert lcs_length("abcde", "ace") == 3
    assert lcs_length("", "abc") == 0
    assert lcs_length("abc", "abc") == 3


def check_question_10():
    assert edit_distance("horse", "ros") == 3
    assert edit_distance("", "abc") == 3
    assert edit_distance("abc", "abc") == 0


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
