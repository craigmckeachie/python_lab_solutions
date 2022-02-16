def get_preferred(*args, **kwargs):
    limit = len(args)
    if "limit" in kwargs:
        limit = kwargs["limit"]

    preferred_strings = []
    for s in args:
        if s.lower().startswith(("a", "q")):
            preferred_strings.append(s)
            if len(preferred_strings) >= limit:
                return preferred_strings
                
    if len(preferred_strings) == 0:
        return None
    else:
        return preferred_strings

if __name__ == "__main__":
    print(get_preferred("abba", "ub40") == ['abba'])
    print(get_preferred("Boston", "Queen") == ['Queen'])
    print(get_preferred("Prince", "ufo") == None )
