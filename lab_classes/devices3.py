class Device:
    """This is a Device Class"""
    x = "howdy"
    def func(self):
        print(Device.x)

d = Device()
d.func()