from picamera import PiCamera
from time import sleep
import requests
camera = PiCamera()
outputfile = '/home/pi/Pictures/upload.jpg'
server_url = 'http://47.110.146.191:5000/upload'

def take_pic(filename):   
    camera.start_preview()
    sleep(5)
    camera.capture(filename)
    camera.stop_preview()
def upload(filename):
    files = {'file':open(filename, 'rb')}
    response = requests.post(server_url, files=files)
    return response
def main():
    take_pic(outputfile)
    response = upload(outputfile)
    print(response)
if __name__ == '__main__':
    main()