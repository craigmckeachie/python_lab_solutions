def get_preferred(*args, **kwargs):
    limit = len(args)
    if "limit" in kwargs:
        limit = kwargs["limit"]

    preferred_strings = []
    for s in args:
        if s.startswith(("a", "q")):
            preferred_strings.append(s)
            if len(preferred_strings) >= limit:
                return preferred_strings
                
    if len(preferred_strings) == 0:
        return None
    else:
        return preferred_strings

if __name__ == "__main__":
    print(get_preferred("ub40", "Abba"))
    print(get_preferred("queen", "abba"))
    print(get_preferred("a", "abba"))
    print(get_preferred("x", "xxx"))
    print(get_preferred("x", "xxx", "a"))
    print(get_preferred("ab", "ac", "ad", "ae"))
    print(get_preferred("ab", "ac", "ad", "ae", limit = 3))
    print(get_preferred("x"))
    print(get_preferred("a"))
