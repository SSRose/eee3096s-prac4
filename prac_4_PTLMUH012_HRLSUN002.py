#!/usr/bin/python

"""Program for a simple environment monitor system.
The system includes a temperature sensor (MCP9700A), an LDR (1K), a pot (1K), an ADC (MCP3008 IC) and 4 push button switches"""

import RPi.GPIO as GPIO
import Adafruit_MCP3008
import spidev
import time
import os

# Open SPI bus
#spi = spidev.SpiDev()
#spi.open(0,0)
#spi.max_speed_hz=1000000

GPIO.setwarnings(False)
# Set pin numbering as GPIO pin numbering
GPIO.setmode(GPIO.BCM)