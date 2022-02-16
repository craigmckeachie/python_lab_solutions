import devices.core as devices
v = devices.VideoDevice("new", 1, "monitor")
print(v.name)

import msg.greet as greet

# Challenge
greet.hello()