def solution(s1, s2):
    same = 0
    for i in range(min(len(s1), len(s2))):
        if s1[-i:] == s2[:i] or s2[-i:] == s1[:i]:
            same = i
    return len(s1) + len(s2) - same
