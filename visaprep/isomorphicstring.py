def are_isomorphic(n, s, t):
    mapping_s_to_t = {}
    mapping_t_to_s = {}

    for i in range(n):
        char_s = s[i]
        char_t = t[i]
        if char_s in mapping_s_to_t and mapping_s_to_t[char_s] != char_t:
            return "false"
        if char_t in mapping_t_to_s and mapping_t_to_s[char_t] != char_s:
            return "false"
        mapping_s_to_t[char_s] = char_t
        mapping_t_to_s[char_t] = char_s

    return "true"
n = int(input().strip())
s = input().strip()
t = input().strip()
print(are_isomorphic(n, s, t))
