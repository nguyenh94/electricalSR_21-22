import matplotlib.pyplot as plt
import math
import spidev
import time

bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 10000000
spi.mode = 2

sampling_rate = 4000
time_per_sample = 1/sampling_rate
signal_duration = 1
sample_count = sampling_rate * signal_duration
singal_frequency = 100 # do half or less
angular_frequency = 2 * math.pi * singal_frequency
amplitude = 2**16/2-1
offset = 2**16/2
phase = 0

array = []
y_arr = []
#t_seq = np.arange(sample_count) * time_per_sample
for i in range((int)(sample_count)):
    x = float(i) * time_per_sample
    array.append(x)
    y = offset + amplitude * math.sin(angular_frequency * x + phase)
    # shiftval = (1  << 22) + (int(y) << 6) # padding six zero's at the end and adding 01 in the front in a 24 bit word
    y_arr.append(y)
    # y1, y2, y3 = (shiftval & 0xFFFFFF).to_bytes(3, 'big')
    # spi.xfer([y1,y2,y3])
    # time.sleep(0.1)

i = 0
buff =10
deltaTime = 1/sampling_rate #in seconds (can have decimals too), in which it should wait in case it has not taken that much time to ensure smooth signal. if its sample Rate is 5000 Hz, delta time is 1/5000
while (1):
    buff=buff - 1 
    start_time = time.time()
    # Do some stuff
    # send data via SPI etc
    shiftval = (1  << 22) + (int(y_arr[i]) << 6) # padding six zero's at the end and adding 01 in the front in a 24 bit word
    y1, y2, y3 = (shiftval & 0xFFFFFF).to_bytes(3, 'big')
    spi.xfer([y1,y2,y3])
    end_time = time.time()
    while((end_time - start_time) < deltaTime ): ### wait till the prescribed delta ti,e
        end_time = time.time()
    i += 1
    if i == len(y_arr):
        i = 0
