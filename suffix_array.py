import functools
class suffix_array:
    def __init__(self, s):
        self.s = s
        self.s_len = len(s)
        self.ranks = []
        self.lcps = []
        self.construct()

    def construct(self):
        sa = self.sa
        s_len = self.s_len
        ranks = self.ranks
        tmp = [ 0 for i in range(s_len + 1) ]
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
        while t <= s_len:
            sorted(ranks, key = functools.cmp_to_key(compare_sa))
            tmp[sa[0]] = 0
            for p in range(1, s_len + 1):
                tmp[sa[p]] = tmp[sa[p - 1]] + 1 if compare_sa(sa[p - 1], sa[p]) else tmp[sa[p - 1]]
            for q in range(s_len + 1):
                ranks[q] = tmp[q]
            t *= 2
        self.sa = sa
        self.construct_lcp()

    def construct_lcp(self):
        h = 0
        self.lcp = [ 0 for i in range(self.s_len) ]
        for i in range(self.s_len):
            j = self.sa[self.ranks[i] - 1]
            if h > 0:
                h = h - 1
            while j + h < self.s_len and i + h < self.s_len:
                if self.s[j + h] != self.s[i + h]:
                    break
                h = h + 1
            self.lcps[self.ranks[i] - 1] = h

    def find(self, ts):
        l_ts = len(ts)
        l, h = 0, self.s_len
        while h - l > 1:
            m = (l + h) // 2
            if self.s[self.sa[m]:self.sa[m] + l_ts] < ts:
                l = m
            else:
                h = m
        if self.s[self.sa[h]:self.sa[h] + l_ts] == ts:
            return self.sa[h]
        return -1

sa = suffix_array('helloworld')
sa.construct()
for rank in sa.ranks:
    print('str: ', sa.s[:rank])
