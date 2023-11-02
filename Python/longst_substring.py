def longest(t1, t2):
    rows_length: int = len(t1)
    cols_length: int = len(t2)
    d2 = [[0] * (cols_length + 1) for _ in range(rows_length + 1)]
    for r in range(1, rows_length + 1):
        for c in range(1, cols_length + 1):
            if t1[r - 1] == t2[c - 1]:
                d2[r][c] = 1 + d2[r - 1][c - 1]
            else:
                d2[r][c] = max(d2[r - 1][c], d2[r][c - 1])

    return d2[-1][-1]
