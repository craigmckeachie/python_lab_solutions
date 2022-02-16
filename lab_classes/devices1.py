class Device:
    """This is a Device Class"""
    x = "howdy"
    def func():
        print(Device.x)
        print("Device function")

print(Device.x)
Device.func()
print(Device.__doc__)

print(type(Device.x))
print(type(Device.func))
