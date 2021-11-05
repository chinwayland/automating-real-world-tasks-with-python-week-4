#!/usr/bin/env python3

import os
import requests

ip = requests.get('https://api.ipify.org').content.decode('utf8')
url = 'http://' + ip + '/fruits/'
directory_text = 'supplier-data/descriptions/'
directory_images = 'supplier-data/images/'
dictionary = {}

for filename in os.listdir(directory_text):
	with open(directory_text + filename, 'r') as text:
		line = text.readline()
		line = line.replace('\n', '')
		dictionary['name'] = line
		line = text.readline()
		line = line.replace(' lbs', '')
		dictionary['weight'] = int(line)
		line = text.readline()
		line = line.replace('\n', '')
		dictionary['description'] = line
		dictionary['image_name'] = filename.replace('txt', 'jpeg')
	response = requests.post(url, data = dictionary)
	print(response.status_code)
