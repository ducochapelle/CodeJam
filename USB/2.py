
##pyusb
##libusb
##win32api
##win32con
##python as administrator
##

###turn off/turn on the device?

import usb
import time
import win32api
#import win32con
KEYEVENTF_EXTENDEDKEY = 1
KEYEVENTF_KEYUP = 2
SHIFT_PRESSED = 16

tone2char = {}
tone2char[48]='B'
tone2char[49]='V'
tone2char[50]='E'
tone2char[51]='C'
tone2char[52]='L'
tone2char[53]='D'
tone2char[54]='S'
tone2char[55]='O'
tone2char[56]='Z'
tone2char[57]='M'
tone2char[58]='H'
tone2char[59]='U'
tone2char[60]='1'
tone2char[61]='2'
tone2char[62]='3'
tone2char[63]='4'
tone2char[64]='5'
tone2char[65]='6'
tone2char[66]='7'
tone2char[67]='8'
tone2char[68]='9'
tone2char[69]='0'
tone2char[70]='+'
tone2char[71]='A'
tone2char[72]='^'


    
def send(array):
    # win32api.keybd_event(win32con.SHIFT_PRESSED, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    key = tone2char[array[2]]
    if key == '+':
        if array[0] == 9:
            win32api.keybd_event(16, 0, 2, 0)
        if array[0] == 8:
            win32api.keybd_event(16, 0, 1, 0)
        return
    elif key == '^':
        return # do this shit
    else:
        if array[0] == 9:
            win32api.keybd_event(ord(key),0,0,0)
            return
        return

dev = usb.core.find(idVendor=0x0763, idProduct=0x2026)
if dev is None:
    raise ValueError('Device not found')
dev.set_configuration()
cfg = dev.get_active_configuration()
intf = usb.util.find_descriptor(
    cfg, bInterfaceNumber = 1,
    bAlternateSetting = 0
)
ep = usb.util.find_descriptor(
    intf,
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_IN
)
assert ep is not None
for i in range(1000):
    try:
        a = ep.read(4)
    except usb.core.USBError:
        pass
    else:
        print a
        send(a)
        

