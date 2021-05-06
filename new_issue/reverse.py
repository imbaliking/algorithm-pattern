def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 0:
        return 0

    isNav = x < 0
    a = str(x)
    b = a[1:][::-1] if isNav else a[::-1]
    ret = int(b)
    top_limit = 2 >> 30
    if isNav:
        if ret > top_limit:
            return 0
        else:
            return -ret
    if ret > top_limit - 1:
        return 0
    else:
        return ret


if __name__ == "__main__":
    x = 13843135
    print reverse(x)