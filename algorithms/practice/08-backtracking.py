"""Backtracking practice. Draw the choice tree before writing code."""


# Question 1: Binary strings.
# Return every length-n string made of 0 and 1, in lexicographic order.
# Example: 2 -> ["00", "01", "10", "11"]; 0 -> [""]
def binary_strings(n):
    raise NotImplementedError


# Question 2: Subsets.
# nums has distinct values. Return every subset; output order does not matter.
# Example: [1, 2] -> [[], [1], [2], [1, 2]]
def subsets(nums):
    raise NotImplementedError


# Question 3: Choose k numbers.
# Return all size-k combinations of values 1..n, each combination ascending.
# Example: (3, 2) -> [[1, 2], [1, 3], [2, 3]]
def choose_k(n, k):
    raise NotImplementedError


# Question 4: Permutations.
# nums has distinct values. Return every ordering; output order does not matter.
# Example: [1, 2] -> [[1, 2], [2, 1]]
def permutations(nums):
    raise NotImplementedError


# Question 5: Phone keypad words.
# Digits use 2:abc, 3:def, 4:ghi, 5:jkl, 6:mno, 7:pqrs, 8:tuv, 9:wxyz.
# Return all letter strings; empty input -> []. Example: "23" -> 9 strings,
# including "ad" and "cf".
def keypad_words(digits):
    raise NotImplementedError


# Question 6: Combination sum with reuse.
# Distinct positive candidates may be used any number of times. Return unique
# combinations summing to target, each sorted; order does not matter.
# Example: ([2, 3, 6, 7], 7) -> [[2, 2, 3], [7]]
def combination_sum(candidates, target):
    raise NotImplementedError


# Question 7: Unique subsets with duplicate input.
# Each input position can be used once. Return each distinct subset once.
# Example: [1, 2, 2] -> [[], [1], [2], [1,2], [2,2], [1,2,2]]
def unique_subsets(nums):
    raise NotImplementedError


# Question 8: Palindrome partitions.
# Split s into nonempty pieces that are each palindromes. Return all splits.
# Example: "aab" -> [["a", "a", "b"], ["aa", "b"]]
def palindrome_partitions(s):
    raise NotImplementedError


# Question 9: Word search.
# Return whether word can be formed by adjacent horizontal/vertical cells.
# A cell may be used only once per path. Example: board = ["ABCE", "SFCS",
# "ADEE"], word = "ABCCED" -> True
def word_exists(board, word):
    raise NotImplementedError


# Question 10: N queens.
# Place n queens on an n×n board (n >= 1) with no shared row, column,
# or diagonal.
# Return all boards as lists of strings, using 'Q' and '.'.
# Example: n=1 -> [["Q"]]; n=2 -> []
def solve_n_queens(n):
    raise NotImplementedError


def check_question_1():
    assert binary_strings(2) == ["00", "01", "10", "11"]
    assert binary_strings(0) == [""]
    assert binary_strings(1) == ["0", "1"]


def check_question_2():
    normalize = lambda groups: sorted(tuple(sorted(group)) for group in groups)
    assert normalize(subsets([1, 2])) == [(), (1,), (1, 2), (2,)]
    assert subsets([]) == [[]]


def check_question_3():
    normalize = lambda groups: sorted(tuple(group) for group in groups)
    assert normalize(choose_k(3, 2)) == [(1, 2), (1, 3), (2, 3)]
    assert choose_k(4, 0) == [[]]
    assert choose_k(2, 3) == []


def check_question_4():
    normalize = lambda groups: sorted(tuple(group) for group in groups)
    assert normalize(permutations([1, 2])) == [(1, 2), (2, 1)]
    assert permutations([]) == [[]]
    assert permutations([1]) == [[1]]


def check_question_5():
    assert sorted(keypad_words("23")) == sorted(
        [a + b for a in "abc" for b in "def"]
    )
    assert keypad_words("") == []
    assert sorted(keypad_words("2")) == ["a", "b", "c"]


def check_question_6():
    normalize = lambda groups: sorted(tuple(group) for group in groups)
    assert normalize(combination_sum([2, 3, 6, 7], 7)) == [(2, 2, 3), (7,)]
    assert combination_sum([2], 1) == []


def check_question_7():
    normalize = lambda groups: sorted(tuple(sorted(group)) for group in groups)
    assert normalize(unique_subsets([1, 2, 2])) == [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]
    assert unique_subsets([]) == [[]]


def check_question_8():
    normalize = lambda groups: sorted(tuple(group) for group in groups)
    assert normalize(palindrome_partitions("aab")) == [("a", "a", "b"), ("aa", "b")]
    assert palindrome_partitions("a") == [["a"]]


def check_question_9():
    board = ["ABCE", "SFCS", "ADEE"]
    assert word_exists(board, "ABCCED") is True
    assert word_exists(board, "ABCB") is False
    assert word_exists(["A"], "A") is True


def check_question_10():
    assert solve_n_queens(1) == [["Q"]]
    assert solve_n_queens(2) == []
    assert len(solve_n_queens(4)) == 2


if __name__ == "__main__":
    import sys
    question = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if question not in range(1, 11):
        raise SystemExit("Choose a question from 1 to 10")
    globals()[f"check_question_{question}"]()
    print(f"Question {question}: examples passed")
