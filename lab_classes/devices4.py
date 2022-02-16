class Device:
    """This is a Device Class"""
    def __init__(self, name):
        self.name = name

    def start(self):
        print("Start " + self.name)

if  __name__ == '__main__': # it is safest to put our test code in this if statement otherwise if we reference this class and don't remove it it will simply execute when we import
    d = Device("new device")
    d.start()
    print(d.name)
    print(dir(d))