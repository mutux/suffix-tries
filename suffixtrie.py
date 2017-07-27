class SuffixTrie(object):

    def __init__(self, t):
        t += '$'  # add terminator
        self.root = {}
        for i in range(len(t)):
            cur = self.root
            for c in t[i:]:
                if c not in cur:
                    cur[c] = {}  # adding new outgoing edge
                cur = cur[c]

    def followPath(self, s):
        cur = self.root
        for c in s:
            if c not in cur:
                return None
            cur = cur[c]
        return cur

    def hasSubstring(self, s):
        return self.followPath(s) is not None

    def hasSuffix(self, s):
        node = self.followPath(s)
        return node is not None and '$' in node

if __name__ == "__main__":
    st = SuffixTrie("abcefdgacematabce")
    a = "efdg"
    b = "efg"
    c = "atabce"
    d = "abc"
    print("hasSubstring - " + a + ": " + str(st.hasSubstring(a)))
    print("hasSubstring - " + b + ": " + str(st.hasSubstring(b)))
    print("hasSuffix - " + c + ": " + str(st.hasSuffix(c)))
    print("hasSuffix - " + d + ": " + str(st.hasSuffix(d)))
