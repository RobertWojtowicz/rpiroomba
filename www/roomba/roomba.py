# *********
# RPiRoomba v1.0
# *********

import create2api
import RPi.GPIO as GPIO
from time import sleep
from sys import argv

# Driving control:
def forward():
    bot = create2api.Create2()
    bot.drive_straight(200) #Normal speed of Roomba is 280

def left():
    bot = create2api.Create2()
    bot.turn_clockwise(-11)
    sleep(0.5)
    bot.drive_straight(0)

def stop():
    bot = create2api.Create2()
    bot.drive_straight(0)
	
def right():
    bot = create2api.Create2()
    bot.turn_clockwise(11)
    sleep(0.5)
    bot.drive_straight(0)

def backward():
    bot = create2api.Create2()
    bot.drive_straight(-200) #Normal speed of Roomba is -280

# Driving mode:
def open():
    bot = create2api.Create2()
    bot.start()
    bot.safe()

def close():
    bot = create2api.Create2()
    bot.stop()

# Camera options:
def camera_0():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    servo = GPIO.PWM(24, 50)
    servo.start(0)
    servo.ChangeDutyCycle(2 + (90 / 18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()

def camera_30():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    servo = GPIO.PWM(24, 50)
    servo.start(0)
    servo.ChangeDutyCycle(2 + (60 / 18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()

def camera_60():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    servo = GPIO.PWM(24, 50)
    servo.start(0)
    servo.ChangeDutyCycle(2 + (30 / 18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()

def camera_90():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(24, GPIO.OUT)
    servo = GPIO.PWM(24, 50)
    servo.start(0)
    servo.ChangeDutyCycle(2 + (0 / 18))
    sleep(0.5)
    servo.ChangeDutyCycle(0)
    servo.stop()
    GPIO.cleanup()
	
def led_on():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.cleanup()

def led_off():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, 0)

# Basic controls:
def wake_up():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23, GPIO.HIGH)
    sleep(1)
    GPIO.output(23, GPIO.LOW)
    sleep(1)
    GPIO.output(23, GPIO.HIGH)
    GPIO.cleanup()

def go_sleep():
    bot = create2api.Create2()
    bot.start()
    bot.power()
    bot.stop()

def clean():
    bot = create2api.Create2()
    bot.start()
    bot.clean()
    bot.stop()

def spot():
    bot = create2api.Create2()
    bot.start()
    bot.spot()
    bot.stop()

def dock():
    bot = create2api.Create2()
    bot.start()
    bot.seek_dock()
    bot.stop()

_, function_name = argv
locals()[function_name]()
