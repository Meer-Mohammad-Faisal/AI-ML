s = set()
s.add(20)
s.add(20.0) # same as 20
s.add('20') # length of s after these operations?
print(len(s))
print(s)
# Output will be 2 because 20 and 20.0 are considered the same in