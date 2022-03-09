import spidev
import time
bus = 0
device = 0
spi = spidev.SpiDev()
spi.open(bus, device)
spi.max_speed_hz = 50000
spi.mode = 2

# write through the first 8 bits has to have 01 
# as the beginning 2 bits then the rest of the bits will be continued

for x in range(100):
    spi.xfer([0x7F, 0xFF, 0xC0])
    time.sleep(0.1)
    spi.xfer([0x40, 0x00, 0x00])
    time.sleep(0.1)
spi.close()
