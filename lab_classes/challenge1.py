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

class AudioDevice(Device):
    """This is the AudioDevice class derived from the Device class"""
    def __init__(self, name, device_id, max_volume_level):
        super().__init__(name, device_id)
        self.__max_volume_level = max_volume_level
        self.volume = 5

    def set_volume(self, volume):
        if volume > self.__max_volume_level:
            self.volume = 10
        else:
            self.volume = volume

    def get_power_level(self):
        return self.volume ** 10

if __name__ == "__main__":
    a = AudioDevice("Creative Stage", 3, 10)
    print(a.volume)
    print(a.get_power_level())
    a.set_volume(7)
    print(a.volume)
    print(a.get_power_level())
    a.set_volume(15)
    print(a.volume)
    print(a.get_power_level())

