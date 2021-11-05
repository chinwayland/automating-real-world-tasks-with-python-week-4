#!/usr/bin/env python3

import os
import datetime
import reports
import emails

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

	subject = "Upload Completed - Online Fruit Store"
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	body = "All fruits were uploaded to our website succesfully. A detailed list is attached to this email."
	message = emails.generage_email(sender, receiver, subject, body, attachment)
	emails.send_email(message)

