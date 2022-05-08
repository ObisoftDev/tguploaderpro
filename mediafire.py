import re
import bs4
import requests
import user_agent

def get(url):
    if re.match("download[0-9]*\.mediafire\.com", url.lstrip("https://").lstrip("http://").split("/")[0]):
        data = url.lstrip("https://").lstrip("http://").split("/")
        if len(data) <= 2:
            raise Exception("Invalid mediafire download url")
        unique_id = data[2]

    elif re.match("[w]*\.mediafire\.com", url.lstrip("https://").lstrip("http://").split("/")[0]):
        data = url.lstrip("https://").lstrip("http://").split("/")
        if len(data) <= 2:
            raise Exception("Invalid mediafire download url")
        unique_id = data[2]

    else:
        raise Exception("No se encontro ningun link de descarga")

    session = requests.Session()
    session.headers["User-Agent"] = user_agent.generate_user_agent()

    data = session.get(f"https://www.mediafire.com/file/{unique_id}/")
    wrp  = bs4.BeautifulSoup(data.text, "html.parser")
    btn  = wrp.find("a", attrs = {"id": "downloadButton"})
    if btn == None:
       raise Exception("Invalid download url")
    link = btn["href"]

    return link

