
##pyusb
##libusb
##win32com
##python as administrator
##
##http://msdn.microsoft.com/en-us/library/aa266279(v=vs.60)
##Key	Code
##BACKSPACE	{BACKSPACE}, {BS}, or {BKSP}
##BREAK	{BREAK}
##CAPS LOCK	{CAPSLOCK}
##DEL or DELETE	{DELETE} or {DEL}
##DOWN ARROW	{DOWN}
##END	{END}
##ENTER	{ENTER}or ~
##ESC	{ESC}
##HELP	{HELP}
##HOME	{HOME}
##INS or INSERT	{INSERT} or {INS}
##LEFT ARROW	{LEFT}
##NUM LOCK	{NUMLOCK}
##PAGE DOWN	{PGDN}
##PAGE UP	{PGUP}
##PRINT SCREEN	{PRTSC}
##RIGHT ARROW	{RIGHT}
##SCROLL LOCK	{SCROLLLOCK}
##TAB	{TAB}
##UP ARROW	{UP}
##F1	{F1}
##F2	{F2}
##F3	{F3}
##F4	{F4}
##F5	{F5}
##F6	{F6}
##F7	{F7}
##F8	{F8}
##F9	{F9}
##F10	{F10}
##F11	{F11}
##F12	{F12}
##F13	{F13}
##F14	{F14}
##F15	{F15}
##F16	{F16}
##
##To specify keys combined with any combination of the SHIFT, CTRL, and ALT keys, precede the key code with one or more of the following codes:
##
##Key	Code
##SHIFT	+
##CTRL	^
##ALT	%
##
##


###turn off/turn on the device?

import usb
import time
import win32com
import win32com.client
shell = win32com.client.Dispatch("Wscript.Shell")

#tone2char = dict([ (n+48,str(chr(n+97))) for n in range(0,25) ])
tone2char = {}
tone2char[48]='b'
tone2char[49]='v'
tone2char[50]='e'
tone2char[51]='c'
tone2char[52]='l'
tone2char[53]='d'
tone2char[54]='s'
tone2char[55]='o'
tone2char[56]='z'
tone2char[57]='m'
tone2char[58]='h'
tone2char[59]='u'
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
tone2char[71]='a'
tone2char[72]='^'


global shift
global ctrl
shift = 0
ctrl = 0
    
def send(array):
    global shift
    global ctrl
    key = tone2char[array[2]]
    if key == '+':
        if array[0] == 9:
            shift = 1
        if array[0] == 8:
            shift = 0
        return
    if key == '^':
        if array[0] == 9:
            ctrl = 1
        if array[0] == 8:
            ctrl = 0
        return
    if array[0] == 9:
        if shift == 1:
            shell.SendKeys("+"+key)
            return
        if ctrl == 1:
            shell.SendKeys("^"+key)
            return
        else:
            shell.SendKeys(key)
            return
        return



# find our device
dev = usb.core.find(idVendor=0x0763, idProduct=0x2026)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
interface_number = cfg[(0,0)].bInterfaceNumber
#line doesnt work, i just fake the intf:
#alternate_settting = usb.control.get_interface(interface_number)
intf = usb.util.find_descriptor(
    cfg, bInterfaceNumber = 1,
    bAlternateSetting = 0
)

ep = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
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
        

