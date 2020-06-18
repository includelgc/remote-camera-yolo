import RPi.GPIO as GPIO
import time
import camera

channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# while True:
#     if GPIO.input(channel) == GPIO.HIGH:
#         print('HIGH')
#     else:
#         print('LOW')
#     time.sleep(0.2)
while True:
    if GPIO.input(channel) == GPIO.HIGH:
        camera.main()
        time.sleep(60)
