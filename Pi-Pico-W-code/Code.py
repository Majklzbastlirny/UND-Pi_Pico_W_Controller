#Micropython code for Raspberry Pi Pico W (RP2040)
#Author: Michal Basler
#Date: 21.01.2023
#Version: 1.0
#Description: This code is for showing mainly time and other data with nixie tubes. 

#What should this code do?
#Show time (HH:MM:SS)
#Show date (DD.MM.YY)
#Show temperature and maybe humidity (Celsius, most likely from DS18B20 or I2C sensor like BME280. If multiple DS18B20 sensors are found, display the value of them invidualy)
#Act as a clock (alarm, timer, stopwatch)
#Show other data (like voltage, current, power, etc. This data will be pushed from other microcontroller via API)

#Notes:
#Display notes
#Display is accesed via multiplex. there are 3 pins for nixie tube addressing (0 = nixie most to the left, 5 = nixie most to the right, 6 and above will display nothing = off)
#Another parrallel set of 4 pins is for actually sending digit to tube. ( BCD format for digits)
#Other pins/keys
#There are 5 buttons. But only 1 pin to read them. So it depends on the multiplex.
#There is also 1 pin for controlling decimal point. Also dependent on multiplex.
#There is also 1 pin for controlling colons, and 1 pin for buzzer. NOT dependent on multiplex.

#Time is set via NTP server and RTC. RTC is set to UTC time. Timezone is set in code. NTP sync is done every 10 minutes.

#Libraries
import utime
import machine
import onewire
import ds18x20
import network
import urequests
import json
import ntptime

#Variables
#Pin definitions

#Multiplex
mux_S0 = machine.Pin(0, machine.Pin.OUT) #Least significant bit
mux_S1 = machine.Pin(1, machine.Pin.OUT)
mux_S2 = machine.Pin(2, machine.Pin.OUT) #Most significant bit
#Nixie tubes numbers (BCD)
D0 = machine.Pin(3, machine.Pin.OUT) #Least significant bit
D1 = machine.Pin(4, machine.Pin.OUT)
D2 = machine.Pin(5, machine.Pin.OUT)
D3 = machine.Pin(6, machine.Pin.OUT) #Most significant bit
#Nixie tubes decimal point
DP = machine.Pin(7, machine.Pin.OUT)
#Colons
COL = machine.Pin(8, machine.Pin.OUT)
#Buzzer
ALM = machine.Pin(9, machine.Pin.OUT)
#Buttons
KEY = machine.Pin(10, machine.Pin.IN,)
#DS18B20
ds_pin = machine.Pin(11)
#I2C
SDA = machine.Pin(12)
SCL = machine.Pin(13)




#Variables
#Wifi
ssid = "SSID"
password = "PASSWORD"
#NTP
ntp_server = "time.cloudflare.com"
#Timezone
timezone = "CET-1CEST,M3.5.0,M10.5.0/3"




