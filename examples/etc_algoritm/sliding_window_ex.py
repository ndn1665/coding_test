s = "abcabcbb"

ans = 0
left_cursor = 0
used = {}
for right_cursor, char in enumerate(s):
    if char in used and left_cursor <= used[char]:
        left_cursor = used[char] + 1
    else:
        ans = max(ans, right_cursor - left_cursor + 1)
    used[char] = right_cursor
