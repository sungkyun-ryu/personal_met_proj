import requests
import os 

def download_file(file_url, save_path):
    with open(save_path, 'wb') as f:
        response = requests.get(file_url)
        if response.status_code == 200:
            print("File Downloading Success!")
        f.write(response.content)