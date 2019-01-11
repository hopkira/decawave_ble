import decawave_ble

# Paths for saving results
output_path_stem = 'output/device_data'
text_output_path = output_path_stem + '.txt'
json_output_path = output_path_stem + '.json'

# Scan for Decawave devices
print('\nScanning for Decawave devices')
decawave_devices = decawave_ble.scan_for_decawave_devices()
num_decawave_devices = len(decawave_devices)
print('Found {} Decawave devices'.format(num_decawave_devices))

# Get data from Decawave devices and write files
print('\nGetting data from Decawave devices')
decawave_device_data = decawave_ble.get_data_multiple_devices(decawave_devices)
decawave_ble.write_data_multiple_devices_to_json_local(
	decawave_device_data,
	json_output_path)
decawave_ble.write_data_multiple_devices_to_text_local(
	decawave_device_data,
	text_output_path)