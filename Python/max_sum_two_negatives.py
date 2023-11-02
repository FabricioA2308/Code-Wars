# https://www.codewars.com/kata/6066ae080168ff0032c4107a/train/python

def max_sum_between_two_negatives(arr):
    idxs = [i for i, x in enumerate(arr) if x < 0]
    return max((sum(arr[i+1:j]) for i, j in zip(idxs, idxs[1:])), default=-1)



max_sum_between_two_negatives([-1, 6, -2, 3, 5, -7])

