class Device:
    """This is a Device Class"""
    def __init__(self, name, device_id):
        self.__name = name
        self.device_id = device_id

    @property
    def name(self):
        return self.__name

    @property
    def device_id(self):
        return self.__device_id

    @device_id.setter
    def device_id(self, device_id):
        if device_id < 0:
            self.__device_id = 0
        else:
            self.__device_id = device_id

    def start(self):
        print("Start " + self.name)

if  __name__ == '__main__':
    d = Device("new device", -2)
    d.start()
    print(d.name)
    print(d.device_id)