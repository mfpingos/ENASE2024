# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:50:05 2023

@author: mpingos
"""

import re
import os
import time
import psutil
import shutil

def process_data(data, tags, folder_name):
    # Split TTL data into individual sources
    sources = re.split('\n\n+', data.strip())  # Ensure to strip whitespace

    for source in sources:
        if not source.strip():  # Skip empty sources
            continue

        match_tags = [re.search(r'{} "([^"]+)"'.format(re.escape(tag)), source) for tag in tags]
        header = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.\n@prefix ex: <http://example.org/>.\n\n"
        if all(match_tags):
            tag_values = [match.group(1) for match in match_tags]
            folder_path = folder_name
            for i, tag_value in enumerate(tag_values):
                tag_folder = os.path.join(folder_path, tag_value.lower() + '_subfolder')
                if not os.path.exists(tag_folder):
                    os.makedirs(tag_folder)
                folder_path = tag_folder

                level_ttl = '\n\n'.join([source.strip() + '\n'])
                level_filename = os.path.join(tag_folder, '{}_level_sources.ttl'.format(tags[i].lower()))
                with open(level_filename, 'a') as file:
                    if os.path.getsize(level_filename) == 0:  # Check if file is empty
                        file.write(header)
                    file.write(level_ttl)

                print('TTL file for {} with values {} saved in folder {}'.format(tags[:i+1], tag_values[:i+1], tag_folder))



# Get user input for tags
user_tags = raw_input("Enter the tags separated by spaces: ").split()

# Specify the file path for the TTL data
file_path = raw_input("Enter the file path for the TTL data: ")

folder_name = '_'.join(user_tags).lower() + '_folder'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
else:
    shutil.rmtree(folder_name)

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

    

start_time = time.time()
start_cpu = psutil.cpu_percent(interval=None)
start_memory = psutil.virtual_memory().used



with open(file_path, 'r') as file:
    data = file.read()
    process_data(data, user_tags, folder_name)


end_cpu = psutil.cpu_percent(interval=None)
end_memory = psutil.virtual_memory().used
end_time = time.time()

elapsed_time = end_time - start_time
cpu_usage = end_cpu - start_cpu
memory_usage = end_memory - start_memory

print('\nExecution time: {:.4f} seconds'.format(elapsed_time))
print('Approximate CPU usage: {:.2f}%'.format(cpu_usage))
print('Approximate memory usage: {:.2f} MB'.format(memory_usage / (1024.0 ** 2)))
