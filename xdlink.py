import requests
import json

def parse(urls):
    requrl = 'https://moodle-tools.netlify.app/.netlify/functions/encode-xd-url'
    jsondata = {'urls':urls}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    resp = requests.post(requrl,data=json.dumps(jsondata),headers=headers)
    return parsejson(resp.text)

def parsejson(json):
        data = {}
        tokens = str(json).replace('{','').replace('}','').split(',')
        for t in tokens:
            split = str(t).split(':',1)
            data[str(split[0]).replace('"','')] = str(split[1]).replace('"','')
        return data