def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    n = len(s)
    if numRows == 1:
        return s

    row_num = min(n, numRows)
    rows = [""] * row_num
    going_down = False
    current_row = 0
    for i in range(n):
        rows[current_row] += s[i]
        if current_row == 0 or current_row == row_num - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return "".join(rows)

if __name__ == "__main__":
    s= "PAYPALISHIRING"
    numRows = 3
    print convert(s,numRows)
    