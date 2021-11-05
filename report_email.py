#!/usr/bin/env python3

import os
import datetime
import reports

#pre_path = '/Users/waylandchin/source/week4/automating-real-world-tasks-with-python-week-4/'
path_descriptions = 'supplier-data/descriptions/'

report = []
def process_data(data):
	for item in data:
		report.append('name: {}<br/>weight: {}\n'.format(item[0], item[1]))
	return report

text_data = []
for text_file in os.listdir(path_descriptions):
	with open(path_descriptions + text_file, 'r') as file:
		line = file.readline()
		text_data.append(line.strip())

if __name__ == "__main__":
	summary = process_data(text_data)
	paragraph = "<br/><br/>".join(summary)
	title = "Processed on {}\n".format(datetime.date.today())
	attachment = '/tmp/processed.pdf'
	reports.generate_report(attachment, title, paragraph)

