def get_preferred(*strings):
    preferred_strings = []
    for s in strings:
        if s.startswith(("a", "q")):
            preferred_strings.append(s)
    if preferred_strings:
        return preferred_strings
    else:
        return None

if __name__ == "__main__":
    print(get_preferred("ub40", "abba"))
    print(get_preferred("queen", "abba"))
    print(get_preferred("a", "abba"))
    print(get_preferred("x", "xxx"))
    print(get_preferred("x", "xxx", "a"))
