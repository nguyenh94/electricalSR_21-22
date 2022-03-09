import smbus
import time

# address = 09
# need 3 bytes

# data = bus.read_i2c_block_data(0x08, 0x00, 2)

# val = ((data[0] << 4) | (data[1] >> 4 )) << 1

# val2 = (val * 2.5 ) / 4096
    
# print (val2)

# Enable I2C clock stretching
dtparam=i2c_arm_baudrate=10000

class ADC:
	address = 0x09

	REG_ADDR_RESULT = 0x00
	REG_ADDR_ALERT  = 0x01
	REG_ADDR_CONFIG = 0x02
	REG_ADDR_LIMITL = 0x03
	REG_ADDR_LIMITH = 0x04
	REG_ADDR_HYST   = 0x05
	REG_ADDR_CONVL  = 0x06
	REG_ADDR_CONVH  = 0x07

	def __init__(self):
		bus.write_byte_data(self.address, self.REG_ADDR_CONFIG,0x20)

	def adc_read(self):
		data=bus.read_i2c_block_data(self.address, self.REG_ADDR_RESULT, 3)
		raw_val=(data[0]&0x0f)<<8 | data[1]
		return raw_val

if __name__ == "__main__":
	bus = smbus.SMBus(1)
	adc= ADC()
	while True:
		print(adc.adc_read())
		print("1")
		time.sleep(.5)