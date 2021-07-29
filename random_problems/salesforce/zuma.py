from functools import lru_cache
from collections import Counter


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(None)
        def reduce(board):
            did_reduce = True
            while did_reduce:
                did_reduce = False
                prev_color, streak = None, 0
                for i, ball in enumerate(board):
                    if ball != prev_color:
                        if streak >= 3:
                            board = board[:i - streak] + board[i:]
                            did_reduce = True
                            break
                        else:
                            prev_color, streak = ball, 1
                    else:
                        streak += 1
                else:
                    if streak >= 3:
                        board = board[:i + 1 - streak] + board[i + 1:]
                        did_reduce = True
            return board

        @lru_cache(None)
        def find_anchors(board):
            if not board:
                return []
            ret = []
            prev_color = board[0]
            for i in range(1, len(board)):
                if board[i] != prev_color:
                    ret.append(i)
                    prev_color = board[i]
            return ret

        def backtrack(cur_hand, cur_board):
            nonlocal min_moves
            cur_board = reduce(cur_board)
            if len(cur_board) == 0:
                min_moves = min(len(hand) - sum(cur_hand.values()), min_moves)
                return
            elif (len(hand) - sum(cur_hand.values())) >= min_moves:
                return

            for i in range(len(board)+1):
                for ball, cnt in cur_hand.items():
                    if cnt > 0:
                        cur_hand[ball] -= 1
                        boards.append(cur_board[:i] + ball + cur_board[i:])
                        backtrack(cur_hand, cur_board[:i] + ball + cur_board[i:])
                        cur_hand[ball] += 1
                        boards.pop()

        hand = [c for c in hand if c in board]
        cur_hand = Counter(hand)
        # for seeing the path to solution
        boards = []
        min_moves = float('inf')
        backtrack(cur_hand, board[:])
        return min_moves if min_moves != float('inf') else -1


if __name__ == "__main__":
    s = Solution()
    # assert s.findMinStep("RRWWRRBBRR", "WB") == 2

    assert s.findMinStep("RBYYBBRRB", "YRBGB") == 3




