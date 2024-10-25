import sys
import requests

DL_FILE = "/tmp/web_"
argv = sys.argv[1:]

def get_content(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'Failed to retrieve the webpage. Status code: {response.status_code}')
    return content

def write_content(content:str, file:str):
    f = open(file, "w")
    f.write(content)
    f.close()

if len(argv)==0:
    print("Usage: python web_sync_multiple.py <URL's file>")
else:
    urls_file = argv[0]
    with open(urls_file, "r", encoding="UTF-8") as file:
        urls = file.readlines()
        for url in urls:
            url = url.split("\n")[0]
            url_formatted = url.split("://")[1]
            html_content = get_content(url)

            urlFile = DL_FILE+url_formatted
            write_content(html_content, urlFile)