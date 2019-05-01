import requests
from bs4 import BeautifulSoup

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent

print("")
url = input("What is the url of the mp3s, please?: ")
print("")
ext = 'mp3'
result = get_url_paths(url, ext)

outfile = open('AutoPlayList.m3u', "w")

print(result)

for elem in result:
    outfile.write(elem + '\n')

outfile.close()

print("")

print("Your output file can be found in this folder, as 'AutoPlayList.m3u.'")

print("")