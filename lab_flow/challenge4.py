import math
import datetime
from statistics import mean

tests = []
for test in range(1,5):
    DURATION = 5

    dt = datetime.datetime.now()
    sec_start = dt.timestamp()
    sec_stop = sec_start + DURATION
    
    print("starting computation")
    loops = 0
    while datetime.datetime.now().timestamp() < sec_stop:
        loops += 1
        x = math.sqrt(loops)
    
    tests.append(loops)
    print("computed %i square root operations in %i seconds" % (loops, DURATION))        

print(tests)
average = mean(tests)
print(f"The average is {average}")

