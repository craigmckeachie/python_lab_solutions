"""
Returns a preferred string
"""
def get_preferred(*args, algorithm, **kwargs):
    limit = len(args)
    if "limit" in kwargs:
        limit = kwargs["limit"]

    preferred_strings = []
    for s in args:
          if (algorithm(s)):
            preferred_strings.append(s)
            if len(preferred_strings) >= limit:
                return preferred_strings
                
    if len(preferred_strings) == 0:
        return None
    else:
        return preferred_strings

def algo1(s):
    """ Takes in a variable and determines if it is less than 5 long in length"""
    return  len(s) < 5

def algo2(s):
    """ Determines if the first letter of a variable is A,a, q, or Q"""
    return  s.lower().startswith(("a", "q"))


if __name__ == "__main__":
    print("Test 1 (12345, abba, ub40): " + str(get_preferred("12345", "abba", "ub40", algorithm=algo1)[0] == "abba"))
    print("Test 2 (abba, ub40): " + str(get_preferred("abba", "ub40", algorithm= algo2)[0] == "abba"))