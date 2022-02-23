# # from math import sin, radians
# # from time import sleep

# # def wave():
# # 	for a in range(-180, 180):
# # 		s = round( float( "{:.02f}".format( sin( radians(a) ) * 100 ) ) ) // 2
# # 		print(f"{a} degrees:", end="\t")
# # 		print( (s + 50) * " ", end="*\n" )
# # 		sleep(0.01)

# # while True:
# # 	wave()

# import time

# # Import the MCP4725 module.
# import math
# import spidev
# bus = 0
# device = 0
# spi = spidev.SpiDev()
# spi.open(bus, device)
# spi.max_speed_hz = 50000
# spi.mode = 2

# # write through the first 8 bits has to have 01 
# # # as the beginning 2 bits then the rest of the bits will be continued
# # for x in range(100):
# #     spi.xfer([0x7F, 0xFF, 0xC0])
# #     time.sleep(0.1)
# #     spi.xfer([0x40, 0x00, 0x00])
# #     time.sleep(0.1)
# # spi.close()

# array = [127, 133, 140, 146, 152, 158, 164, 170, 176, 182, 188, 193, 198, 203, 208, 213, 218, 222,
# 226, 230, 234, 237, 240, 243, 245, 247, 249, 251, 252, 253, 254, 254, 254, 254, 254, 253, 252, 250, 248, 246, 244, 241, 238, 235, 232, 228, 224, 220, 215, 211, 206, 201, 196, 190, 185, 179, 173, 167, 161, 155, 149, 143, 136, 130, 124, 118, 111, 105, 99, 93, 87, 81, 75,
# 69, 64, 58, 53, 48, 43, 39, 34, 30, 26, 22, 19, 16, 13, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0,
# 1, 2, 3, 5, 7, 9, 11, 14, 17, 20, 24, 28, 32, 36, 41, 46, 51, 56, 61, 66, 72, 78, 84, 90,
# 96, 102, 108, 114, 121, 127]


# # transfer 127 
# i = 0
# while i != -1:
# 	value = "{0:b}".format(int(array[i])) #convert decimal in table to binary 
# 	value = int(value)
# 	print("line 47 value in binary is", value)
# 	i += 1
	
# 	value = value >> 10
# 	value |= 0b01000000 
# 	# value = "{0:b}".format(int(value))
# 	# value = int(value)
# 	# print("Line 52 after bitshift value is", value)
# 	spi.xfer([0x7F, 0x00, 0x00]) # 127
# 	# time.sleep(1)
# 	# spi.xfer([0x40, 0x00, 0x00]) # 0
# 	# time.sleep(0.1)
# 	spi.xfer([0x40, 0x05, 0x00]) # 48
# 	# time.sleep(1)
# 	# spi.xfer([0x40, 0x00, 0x00]) # 0
# 	# time.sleep(0.1)
# # while True:

# #     for i in range(4095,0,-50):
# #         spi.raw_value = 1400 + int(1240 * (math.sin( 2 * math.pi * i / 4095)))  
		

# # import math
# # from pyb import DAC

# # # create a buffer containing a sine-wave
# # buf = bytearray(100)
# # for i in range(len(buf)):
# #     buf[i] = 128 + int(127 * math.sin(2 * math.pi * i / len(buf)))

# # # output the sine-wave at 400Hz
# # dac = DAC(1)
# # dac.write_timed(buf, 400 * len(buf), mode=DAC.CIRCULAR)

import time

# Import the MCP4725 module.
import math
import spidev
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

array = [127, 133, 140, 146, 152, 158, 164, 170, 176, 182, 188, 193, 198, 203, 208, 213, 218, 222,
226, 230, 234, 237, 240, 243, 245, 247, 249, 251, 252, 253, 254, 254, 254, 254, 254, 253, 252, 250, 248, 246, 244, 241, 238, 235, 232, 228, 224, 220, 215, 211, 206, 201, 196, 190, 185, 179, 173, 167, 161, 155, 149, 143, 136, 130, 124, 118, 111, 105, 99, 93, 87, 81, 75,
69, 64, 58, 53, 48, 43, 39, 34, 30, 26, 22, 19, 16, 13, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0,
1, 2, 3, 5, 7, 9, 11, 14, 17, 20, 24, 28, 32, 36, 41, 46, 51, 56, 61, 66, 72, 78, 84, 90,
96, 102, 108, 114, 121, 127]


# transfer 127 
i = 0
while i != -1:
    #value = "{0:b}".format(int(array[i])) #convert decimal in table to binary 
    orig_val = array[i]
    byte1 = array[i]
    byte1 &= 0b1111111111111111
    byte1 = byte1 >> 10
    byte1 |= 0b01000000 
    byte2 = array[i]
    byte2 = byte2 << 6
    byte2 = byte2 >> 8
    byte2 &= 0b1111111111111111
    byte3 = array[i]
    byte3 = byte3 << 14
    byte3 = byte3 >> 8
    #value = bin(array[i])
    
    i += 1

    # spi.xfer([byte1, byte2, byte3]) # 127

    # time.sleep(1)
    spi.xfer([0x40, 0x00, 0x00]) # 0
    # time.sleep(0.1)
    #spi.xfer([0x40, 0x05, 0x00]) # 48