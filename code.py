import board
import busio
import digitalio
import adafruit_tlc5947
import time

#Initialization of the plate parameters
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
latch = digitalio.DigitalInOut(board.D5)
led = adafruit_tlc5947.TLC5947(spi, latch)

#Some common functions.
# monotonic is a function that accepts the following parameters:
# i_0 initial intensity, range [0-4095])
# i_f final intensity, must be higher than i_0
# step intensity step
# timestep the amount of time in seconds to wait until the next intensity change

def monotonic(i_0, i_f, step, timestep):
    elapsed = 0
    for i in range(i_0, i_f, step):
        led[12] = led[22] = led[23] = i
        time.sleep(timestep)
        elapsed = elapsed + timestep
        print(elapsed, i)


def constant(i_0):
    led[12] = led[22] = led[23] = i_0


while True:
    constant(100)
