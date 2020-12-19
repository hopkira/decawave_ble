import decawave_ble
import time
import math

TAG_NAME = 'DW25CF'

print"Scanning for decawave devices..."
decawave_devices = decawave_ble.scan_for_decawave_devices()
print(str(len(decawave_devices)) + " devices found.")

def get_vector(x,y):
    dist = get_dist(x,y)
    angle = get_angle(x,y)
    return dict(dist = dist, angle = angle)

def get_dist(x,y):
    return math.sqrt((x ** 2) + (y ** 2)) / 1000

def get_angle(x,y):
    return math.atan2(y,x)

while True:
    try:
        scan_data = decawave_ble.get_data(decawave_devices[TAG_NAME])
        position = scan_data['location_data']['position_data']
        if position:
            vector = get_vector(position['x_position'], position['y_position'])
            print('Dist: %.2fm Angle: %.2f radians ' % (vector['dist'], vector['angle']))
        time.sleep(0.1)
    except:
        print("ERROR: tag cannot be found")
    