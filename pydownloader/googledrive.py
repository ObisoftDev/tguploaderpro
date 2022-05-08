import requests
from bs4 import BeautifulSoup
import os

def get_direct_url(id):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    try:
        if response.url:
            return response.url
    except:pass
    return None

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def get_info(url):
    req = requests.get(url)
    sp = BeautifulSoup(req.text,"html.parser")
    file_name = sp.find('meta',{'property':'og:title'}).attrs['content']
    file_id = url.split('/')[-2]
    file_url = get_direct_url(file_id)
    return {'file_name':file_name,'file_id':file_id,'file_url':file_url}