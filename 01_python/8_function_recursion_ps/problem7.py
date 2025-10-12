# Write a python function to remove a given word from a list ad strip it at the same
#time.

def rem(l,word):
    n = [ ]
    for item in l:
        l.remove(word)
        return l

l = ["Harry" , "Rohan", "Shubham", "an"]

print(rem(l,"an"))

