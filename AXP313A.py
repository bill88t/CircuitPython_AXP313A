from time import sleep

class camera_voltages:
    OV2640 = [1.2, 2.8]
    OV7725 = [1.8, 3.3]

class AXP313A:
    def __init__(self, i2c):
        self.i2c = i2c

    def begin(self):
        if not self.i2c.try_lock():
            return False
        scan = self.i2c.scan()
        self.i2c.unlock()
        print(scan)
        return 0x36 in scan


    def set_power(self,DVDD,AVDDorDOVDD):
        state = 0x19
        ALDOData = 0
        DLDOData = 0
        if (DVDD < 0.5) or (AVDDorDOVDD < 0.5):
            ALDOData = 0
            DLDOData = 0
        elif(DVDD > 3.5) or (AVDDorDOVDD > 3.5):
            ALDOData = 31
            DLDOData = 31
        else:
            ALDOData = (DVDD-0.5) * 10
            DLDOData = (AVDDorDOVDD-0.5) *10
        self.WriteByte(0x10, state)
        sleep(0.01)
        self.WriteByte(0x16, int(ALDOData))
        sleep(0.01)
        self.WriteByte(0x17, int(DLDOData))
        sleep(0.01)

    def set_shutdown_key_level_time(self,offLevelTime):
        data = offLevelTime << 1
        self.WriteByte(0x1E, data)
        sleep(0.01)

    def disable_power(self):
        data = 0x01;
        self.WriteByte(0x10, data)
        sleep(0.01)

    def WriteByte(self, reg, data):
        buf = bytearray(1)
        buf[0] = reg
        buf.extend(bytearray([data]))
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(0x36, buf)
        finally:
            self.i2c.unlock()

def enable_camera(AXPobject, camera: list) -> bool:
    return AXPobject.set_power(camera[0], camera[1])

def disable_camera(AXPobject) -> None:
    AXPobject.disable_power()