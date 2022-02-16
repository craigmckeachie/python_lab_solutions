"""
Returns a preferred string given two strings as input
Now returns None in the default case
"""
def get_preferred(s1, s2):
    if s1.startswith(("a","q")):
        return s1

    if s2.startswith(("a", "q")):
        return s2

if __name__ == "__main__":
    print(get_preferred("ub40", "abba"))
    print(get_preferred("a", "abba"))
    print(get_preferred("x", "xxx"))
