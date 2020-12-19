import decawave_ble
import time
import math

TAG_NAME = 'DW25CF'

def get_vector(x,y):
    dist = get_dist(x,y)
    angle = get_angle(x,y)
    return dict(dist = dist, angle = angle)

def get_dist(x,y):
    return math.sqrt((x ** 2) + (y ** 2)) / 1000

def get_angle(x,y):
    return math.atan2(y,x)

print("Scanning for Decawave devices...")

while True:
    decawave_devices = decawave_ble.scan_for_decawave_devices()
    print(str(len(decawave_devices)) + " devices found.")
    if TAG_NAME in decawave_devices:
        print("Target tag detected... listening for position.")
        break
    else:
        print("Tag not found... will retry in 10 seconds...")
        time.sleep(10)

while True:
    try:
        scan_data = decawave_ble.get_data(decawave_devices[TAG_NAME])
        position = scan_data['location_data']['position_data']
        print(position)
        if position:
            vector = get_vector(position['x_position'], position['y_position'])
            # print('Dist: %.2fm Angle: %.2f radians ' % (vector['dist'], vector['angle']))
        time.sleep(0.1)
    except:
        print("ERROR: tag cannot be found")
    