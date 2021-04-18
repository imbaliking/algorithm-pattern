
def lengthOfLongestSubstring(s):
    ret_length = 0
    length = len(s)
    dupstring = set()
    rk = -1
    for i in range(length):
        if i > 0:
            dupstring.remove(s[i-1])
        while rk+1 < length and s[rk+1] not in dupstring:
            dupstring.add(s[rk+1])
            rk += 1
        ret_length = max(ret_length,rk-i+1)
    return ret_length

if __name__ == "__main__":
    test_string = "pwwakew"
    print lengthOfLongestSubstring(test_string)


