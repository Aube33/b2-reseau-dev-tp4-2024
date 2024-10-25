import sys
import requests

DL_FILE = "/tmp/web_page"
argv = sys.argv[1:]

def get_content(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'Failed to retrieve the webpage. Status code: {response.status_code}')

def write_content(content:str, file:str):
    f = open(file, "w", encoding="utf-8")
    f.write(content)
    f.close()

if len(argv)==0:
    print("Usage: python web_sync.py <URL>")
else:
    url_request = argv[0]
    html_content = get_content(url_request)
    write_content(html_content, DL_FILE)