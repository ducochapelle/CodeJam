#let all be fractalleble!

FileName="sound"
FileLength=14*8

from struct import pack
import math
import random
TWO_BYTES = '<h'
FOUR_BYTES = '<i'

def cutoff(var,par):
    if var > par:
        return par
    elif var < -par:
        return -par
    else:
        return var
class R():
    def __init__(self):
        self.last = 0.5
    def sound(self,incr):
        if random.random() > self.last:
            self.last *= incr
        else:
            self.last *= 2-incr
        return self.last*2-1
r = R()

def sinorator(amp, fact):
    for f in range(fact):
        amp = math.sin(amp*math.pi/2)
    return amp

def accumulator(a):
    b = []
    l = 0
    for i in range(len(a)):
        l += a[i][0]**-1
        b += [(l,a[i][1]**-1)]
    return b
    
def generator(time, shape="sin", freq=440):
    if shape == "sin":
        return math.sin(time*2*math.pi*freq)
    if shape == "block":
        period = freq**-1
        time = time % (2*period)
        return 1 if time > period else -1
    if shape == "blocks":
        time = time % freq[-1][0]
        for elem in freq:
            if time < elem[0]:
                return elem[1]
 
def combinator(waves):
    pass
def alternator():
    pass

def sound(time):
    return sound6(time)

        
def sound13(time):
    incr = time/100.+1
    #return random.random()*2-1
    return cutoff(r.sound(incr),1)


def sound12(time):
    kick = generator(time, freq=140.)
    kick_envelope = math.e**(-8*(time%1.))
    clap = generator(time, freq=440.)
    if clap > 0.7 or clap < -0.7:
        clap *= 0.3

    dist = 1+time/10.
    if time%1. > 0 and time%1. < 0.5: 
        return cutoff(dist*kick*kick_envelope,1.)
    elif time%1. > 0.5 and time%1. < 0.55:
        return clap*0.2
    else:
        return 0.0

def sound11(time):
    waves = map(lambda x: generator(time,freq=220*(1+x*3/24.)),
                range(0,int(time*2)+1)
                )
    wave = waves[0]*waves[-1]
    wave *= sinorator(waves[len(waves)/2],int(time/2+1))
    a = [(3/8.,1.),
         (1/2.,0.),
         (1/1.,1.)]
    wave *= generator(time, shape='blocks', freq=a)
    return wave

def sound10(time):
    if time%2<1:
        return 110*(time%(1/110.))
    elif time%4<2:
        return generator(time,freq=110)
    elif time%4<4:
        return 0.5 if 110*(time%(1/110.)) > 0.5 else -0.5

def sound9(time):
    waves = map(lambda x: generator(time,freq=110*x),
                range(1,10)
                )
    wave = reduce(lambda x,y: 0.8*x+0.2*y, waves)
    return wave
    
def sound8(time):
    a = accumulator([(32/3.,1),
    (32,-2),
    (8,1),
    (4,2),
    (12,1),
    (12,1),
    (12,1),
    (12,-3),
    (12,-4),
    (12,-8)])
    b = lambda time: generator(time,shape='blocks',freq=a)
    bs = [b(time+x*0.0001) for x in range(100)]
    baverage = sum(bs)/float(len(bs))
    c = baverage
    return sinorator(generator(time,freq=110*c),2)

def sound7(time):
    wave1 = generator(time, freq=55)
    if time%2 > 1: wave1 = sinorator(wave1,int(time))
    wave1 = wave1 * (1-time%1)**4
    return wave1

def sound6(time):
    volume = map(lambda x,y:(x/4.0, y),range(1,5), [1, 0, 0, 0.5])
    volume = generator(time, shape='blocks', freq=volume)
    wave1a = generator(time, shape="block", freq=220)
    wave1b = generator(time, shape="block", freq=220*7/4.)
    wave2a = generator(time, freq=220)
    wave2b = generator(time, freq=220*7/4.)
    xx = generator(time,freq=1/16.)
    x = generator((time+xx)%1, freq=0.5)
    return wave2a*(1-x+wave1a*x)*wave1b*wave2b

def sound5(time):
    tracks = [sound2(time), sound3(time), sound4(time)]
    f = len(tracks)
    return sum([x/float(f) for x in tracks])

def sound4(time):
    volume = map(lambda x,y:(x/4.0, y),range(1,5), [1, 0, 0, 0.5])
    volume = generator(time, shape='blocks', freq=volume)
    wave1a = generator(time, shape="block", freq=220)
    wave1b = generator(time, shape="block", freq=330)
    wave2a = generator(time, freq=220)
    wave2b = generator(time, freq=330)
    return volume*(0.5*wave1a*wave2a+0.5*wave1b*wave2b)

def sound3(time):
    lst1 = [(0.25,1+ 0/24.),
           (0.50,1+ 3/24.),
           (0.75,1+ 6/24.),
           (1.00,1+ 8/24.),
           (1.25,1+12/24.),
           (1.50,1+16/24.),
           (1.75,1+21/24.),
           (2,   0.5+21/48.)]
    lst1 = map(lambda x: (2*x[0],x[1]),lst1)
    lst2 = sorted(map(lambda x: ((x[0]+0.5)%2, x[1]), lst1))
    freq1 = generator(time,shape="blocks", freq=lst1)
    freq2 = generator(time,shape="blocks", freq=lst2)
    wave1 = generator(time,shape="block",freq=440*freq1)
    wave3 = generator(time,shape="sin",freq=440*freq2)
    wave2 = generator(time,freq=1)
    return wave1*wave2*wave3

def sound2(time):
    freq1 = generator(time,freq=4**-1)
    freq2 = generator(time,freq=2**-1)
    freq3 = 1.5 if freq1 > 0 and freq2 < 0 else 1 if freq1 > 0 else 3**-1
    wave1 = generator(time%1, freq=freq3*16*generator(time,freq=32))
    wave2 = math.ceil(max(0,generator(time,freq=4)))
    return wave1*wave2

def create(FileName, Seconds=1):
    f = open(FileName, 'wb')
    #https://ccrma.stanford.edu/courses/422/projects/WaveFormat/
    Subchunk1Size = 16
    AudioFormat = 1 # PCM
    NumChannels = 1
    SampleRate = 44100
    BitsPerSample = 16
    BlockAlign = NumChannels * BitsPerSample / 8
    ByteRate = SampleRate * NumChannels * BitsPerSample / 8
    NumSamples = SampleRate * Seconds
    Subchunk2Size = NumSamples * NumChannels * BitsPerSample / 8

    header = "RIFF" + 4*"\x00" + "WAVE" + "fmt " #16 bytes
    header += pack(FOUR_BYTES, Subchunk1Size)
    header += pack(TWO_BYTES, AudioFormat)
    header += pack(TWO_BYTES, NumChannels)
    header += pack(FOUR_BYTES, SampleRate)
    header += pack(FOUR_BYTES, ByteRate)
    header += pack(TWO_BYTES, BlockAlign)
    header += pack(TWO_BYTES, BitsPerSample)
    header += "data" # 4 bytes
    header += pack(FOUR_BYTES, Subchunk2Size)
    f.write(header)
    SampleRate = float(SampleRate)
    MaxSampleValue = 2**(BitsPerSample - 1)-1
    for sample in range(NumSamples*NumChannels):
        time = sample/SampleRate # in seconds
        f.write(pack(TWO_BYTES,MaxSampleValue*sound(time)))    
    f.close()

create(FileName+".wav", Seconds=FileLength)

print "Done!"
