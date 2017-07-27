class TrieMap(object):
    """ Trie implementation of a map. Associating Keys (strings or other
        sequence type) with values. Values can be any type. """
    def __init__(self, kvs):
        # A node is a dictionary storing the indiced character as the key,
        # and a dictionary as the value. The dictionary includes all
        # the nodes(dictionaries) that connected to it.
        self.root = {}
        # For each key (string)/value pair
        for (k, v) in kvs:
            self.add(k, v)

    def add(self, k, v):
        """ Add a key-value pair """
        cur = self.root
        for c in k:  # for each character in the string
            if c not in cur:
                cur[c] = {}  # add a new node (dictionary)
            cur = cur[c]  # move cur forward to node with key c
        cur['value'] = v  # add the value in the end

    def query(self, k):
        """Given key, return associated value or None """
        cur = self.root
        for c in k:
            if c not in cur:
                return None  # key wasn't in the trie
            cur = cur[c]
        # get value, or None if there's no value associated with this node
        return cur.get('value')

if __name__ == "__main__":
    kvs = [('acdeast', 1000), ('bcde', 2000), ('acdb', 3000), ('bcas', 4000), ('case', 5000), ('ba', 6000), ('ae', 7000)]

    m = TrieMap(kvs)
    print(m.query("case"))
