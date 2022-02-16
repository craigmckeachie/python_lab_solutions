def get_preferred(s1, s2, *strings):
    if s1.startswith(("a","q")):
        return s1

    if s2.startswith(("a", "q")):
        return s2

    for s in strings:
        if s.startswith(("a", "q")):
            return s

    return None

if __name__ == "__main__":
    print(get_preferred("ub40", "abba"))
    print(get_preferred("queen", "abba"))
    print(get_preferred("a", "abba"))
    print(get_preferred("x", "xxx"))
    print(get_preferred("x", "xxx", "a"))
