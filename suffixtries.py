class SuffixNode:
    def __init__(self, suffix_link=None):
        self.children = {}
        if suffix_link is not None:
            self.suffix_link = suffix_link
        else:
            self.suffix_link = self

    def add_edge(self, edge, node):  # (key,value): key is the edge label, value is the node to be appended
        self.children[edge] = node


def suffix_tries(s):
    root = SuffixNode()
    deepest = SuffixNode(root)
    root.add_edge(s[0], deepest)

    for c in s[1:len(s)]:
        cur = deepest
        prev = None
        # for char c, travel start from the deepest node, along the suffix_links
        while c not in cur.children:
            tmp = SuffixNode()
            cur.add_edge(c, tmp)

            if prev is not None:
                prev.suffix_link = tmp

            prev = tmp
            cur = cur.suffix_link

        if cur is root:
            prev.suffix_link = root
        else:
            prev.suffix_link = cur.children[c]

        # update current deepest node, prepare for the next char
        deepest = deepest.children[c]

if __name__ == "__main__":
    suffix_tries("abacbade")
