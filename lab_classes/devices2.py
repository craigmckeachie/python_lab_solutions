class Device:
    """This is a Device Class"""
    x = "howdy"
    def func(self):
        print("Device function")

d = Device()
d.func()

Device.func(d)
print(Device.x)