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

class VideoDevice(Device):
    """This is the VideoDevice class derived from the Device class"""
    def __init__(self,name,device_id,device_type):
        super().__init__(name,device_id)
        self.__device_type = device_type

    @property
    def device_type(self):
        return self.__device_type

if  __name__ == '__main__':
    v = VideoDevice("new device", 2, "monitor")
    v.start()
    print(v.device_type)
    print(v.device_id)

    print(type(v))
    print(isinstance(v,VideoDevice))
    print(issubclass(type(v),Device))