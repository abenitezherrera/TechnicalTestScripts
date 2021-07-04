import json
import os
import csv

#base_dir='C:/home/user/Documents/user_profiles'
base_dir='C:/Users/abenitezherrera/Desktop/Web Scrapping'

#Get all files in the directory
data_list = []
for file in os.listdir(base_dir):
	if 'json' in file:
		json_path = os.path.join(base_dir, file)
		data_list.append(json_path)
print(data_list)

with open ('output.tsv', 'wt',newline='', encoding='utf-8') as out_file:
	tsv_writer = csv.writer(out_file, delimiter  ='\t')
	tsv_writer.writerow(['user_id','address'])
	for file in data_list:
		with open(file) as f:
			data = json.load(f)

			for user in data['registration_address']:
				address_type = user['type']
				user_id = data['user_id']
				address = user['address']
				if address_type == 'work':
					#print(user_id, address)
					data = list()
					data.append(user_id)
					data.append(address)
					print(data)

				
					
					tsv_writer.writerow(data)
					
