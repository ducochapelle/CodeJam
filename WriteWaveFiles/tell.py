import winsound
from os import path
from time import sleep

do = "do.py" # generates the wave file
t, t_old = 0.,0.
FileLength = 1.

while True: 
    while t == t_old:
        sleep(FileLength)
        t = path.getmtime(do) # get modiefied datetime
    t_old = t
    print "Generating file..."
    try:
        execfile(do)
        print "Playing file..."
        winsound.PlaySound(FileName+".wav", winsound.SND_FILENAME | winsound.SND_LOOP | winsound.SND_ASYNC)
    except:
        print "Fail"

# ctrl-c to break, pretty ugly
# winsound.PlaySound('*',winsound.SND_PURGE)
