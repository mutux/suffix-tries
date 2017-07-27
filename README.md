# Suffix Trie, Suffix Tries and Triemap implemented in Python

String algorithm for fun! Detailed information can be found on my blogger [MuTuX](http://www.mutux.com/2017/05/string-algorithm-suffix-tries.html "mutux's blog on text mining").


## Examples

```
    st = SuffixTrie("abcefdgacematabce")
	a = "efdg"
	b = "efg"
	c = "atabce"
	d = "abc"
	print "hasSubstring - " + a + ": " + str(st.hasSubstring(a))
	print "hasSubstring - " + b + ": " + str(st.hasSubstring(b))
	print "hasSuffix - " + c + ": " + str(st.hasSuffix(c))
	print "hasSuffix - " + d + ": " + str(st.hasSuffix(d))
```

## Finally
Have fun!
