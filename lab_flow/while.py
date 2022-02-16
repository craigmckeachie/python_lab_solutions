import math
import datetime

DURATION = 5

dt = datetime.datetime.now()
sec_start = dt.timestamp()
sec_stop = sec_start + DURATION

print("starting computation")
loops = 0
while datetime.datetime.now().timestamp() < sec_stop:
    loops += 1
    x = math.sqrt(loops)

print("computed %i square root operations in %i seconds" % (loops, DURATION))