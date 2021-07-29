# Given a word of length n and n six-sided dice with a character in each side. Find out if this word can be constructed by the set of given dice.
#
# Example 1:
#
# Input:
# word = "hello"
# dice = [[a, l, c, d, e, f], [a, b, c, d, e, f], [a, b, c, h, e, f], [a, b, c, d, o, f], [a, b, c, l, e, f]]
# Output: true
# Explanation: dice[2][3] + dice[1][4] + dice[0][1] + dice[4][3] + dice[3][4]
# Example 2:
#
# Input:
# word = "hello"
# dice = [[a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f], [a, b, c, d, e, f]]
# Output: false
# Example 3:
#
# Input:
# word = "aaaa"
# dice = [[a, a, a, a, a, a], [b, b, b, b, b, b], [a, b, c, d, e, f], [a, b, c, d, e, f]]
# Output: false

from implementation import ford_fulkerson
from collections import defaultdict

# use a max flow analysis to solve this.
# if your flow network only has 1 capacity from the source to each dice, and
# 1 capacity from each dice to each letter, and 1 capacity from each letter to the sink
# then you can only make the word from the given dice if the max flow equals the length of the word
# used Edmonds-Karp for complexity of O(V * E^2)
def dice_to_word1(dice, word):
    letter_to_idx = defaultdict(list)
    for i, c in enumerate(word):
        letter_to_idx[c].append(i)

    node_cnt = len(dice) + len(word) + 2
    graph = [[0] + [1] * len(dice) + [0] * (len(word) + 1)]
    graph.extend([[0] * node_cnt for _ in range(node_cnt-2)])
    graph.append([0] * (len(dice)+1) + [1] * len(word) + [0])

    for i in range(len(dice)):
        dice_node = i + 1
        for l in dice[i]:
            if l in letter_to_idx:
                for j in letter_to_idx[l]:
                    letter_node = len(dice) + 1 + j
                    graph[dice_node][letter_node] = 1

    for i in range(len(dice)+1, len(graph)-1):
        graph[i][-1] = 1

    if ford_fulkerson(graph, 0, len(graph)-1) == len(word):
        return True
    return False


def dice_to_word2(dice, word):
    def backtrack(letter_idx, dice_idx):
        if all(satisfied_letters):
            return True
        if satisfied_letters[letter_idx] or used_dice[dice_per_letter[letter_idx][dice_idx]]:
            return False

        satisfied_letters[letter_idx] = 1
        used_dice[dice_per_letter[letter_idx][dice_idx]] = 1

        for l_i in range(letter_idx, len(word)):
            for d_i in range(0, len(dice_per_letter[l_i])):
                ret = backtrack(l_i, d_i)
                if ret is True:
                    return True

        satisfied_letters[letter_idx] = 0
        used_dice[dice_per_letter[letter_idx][dice_idx]] = 0

        return False

    dice_per_letter = [[] for _ in word]

    for i, c in enumerate(word):
        for j, d in enumerate(dice):
            for l in d:
                if c == l:
                    dice_per_letter[i].append(j)

    satisfied_letters = [0] * len(word)
    used_dice = [0] * len(dice)
    for i in range(len(dice_per_letter)):
        for j in range(len(dice_per_letter[i])):
            return backtrack(i,j)


if __name__ == "__main__":
    assert dice_to_word1([
        ['a', 'l', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'h', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'o', 'f'],
        ['a', 'b', 'c', 'l', 'e', 'f']
    ], "hello") is True

    assert dice_to_word1([
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f']
    ], "hello") is False

    assert dice_to_word2([
        ['a', 'l', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'h', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'o', 'f'],
        ['a', 'b', 'c', 'l', 'e', 'f']
    ], "hello") is True

    assert dice_to_word2([
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['a', 'b', 'c', 'd', 'e', 'f']
    ], "hello") is False

