def first_aq(x):
    """ Determines if the first letter of a variable is A,a, q, or Q"""
    return x[0] == 'a' or x[0] == 'A' or x[0] == 'q' or x[0] == 'Q'

def small(x):
    """ Takes in a variable and determines if it is less than 5 long in length"""
    return len(x) < 5


"""
Returns a preferred string
"""
def get_preferred(*args, algorithm= first_aq, **kwargs):
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


if __name__ == "__main__":
    print("Test 1 (abba, ub40): " + str(get_preferred("abba", "ub40")[0] == "abba"))
    print("Test 2 (Boston, Queen): " + str(
        get_preferred("Boston", "Queen", algorithm=first_aq)[0] == "Queen"))
    print("Test 3 (Cream, BTO, Who, Aces): " + str(
        get_preferred("Cream", "BTO", "Who", "Aces", algorithm=first_aq)[0] == "Aces"))
    print("Test 4 (ABC, 10cc, Quiet Riot): " + str(
        len(get_preferred("ABC", "10cc", "Quiet Riot", algorithm=first_aq)) == 2))
    print("Test 5 (ABC, 10cc, Quiet Riot): " + str(
        len(get_preferred("ABC", "10cc", "Quiet Riot", limit=1, algorithm=first_aq)) == 1))
    print("Test 6 (Prince, ufo): " + str(get_preferred("Prince", "ufo", algorithm=first_aq) == None))
    print("Test 7 (Prince, ufo): " + str(get_preferred("Prince", "ufo", algorithm=small)[0] == "ufo"))        
