"""
Returns the first string starting with a or q, or the first if neither are preferred
"""
def get_preferred(s1, s2):
    if s1.lower().startswith(("a","q")):
        return s1

    if s2.lower().startswith(("a", "q")):
        return s2

if __name__ == "__main__":
    print(get_preferred("ub40", "abba"))
    print(get_preferred("Queen", "abba"))
