import functools
class suffix_array:
    def __init__(self, s):
        self.s = s
        self.s_len = len(s)
        self.ranks = []

    def construct(self):
        sa = []
        tmps, ranks = [], self.ranks
        for i in range(self.s_len + 1):
            sa.append(i)
            ranks.append(ord(self.s[i]) if i < n else -1)

        def compare_sa(i, j):
            if ranks[i] != ranks[j]:
                return ranks[i] < ranks[j]
            else:
                ri = ranks[i + k] if i + k <= self.s_len else -1
                rj = ranks[j + k] if j + k <= self.s_len else -1
                return ri < rj

        t = 1
        while t <= self.s_len:
            sorted(ranks, key = functools.cmp_to_key(compare_sa))
            tmp[sa[0]] = 0
            for p in range(1, self.s_len + 1):
                tmp[sa[p]] = tmp[sa[p - 1]] + 1 if compare_sa(sa[p - 1], sa[p]) else 0
            for q in range(self.s_len + 1):
                ranks[q] = tmp[q]
            t *= 2

sa = suffix_array('helloworld')
sa.construct()
for rank in sa.ranks:
    print('str: ', sa.s[:rank])
