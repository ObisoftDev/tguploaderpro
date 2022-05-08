import time
import os
import re
import unicodedata
import re


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    ext = str(value).split('.')[-1]
    value = str(value).split('.')[0]
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_') + '.' + ext


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def req_file_size(req):
    try:
        return int(req.headers['content-length'])
    except:
        return 0

def get_url_file_name(url,req):
    try:
        if "Content-Disposition" in req.headers.keys():
                name = str(req.headers["Content-Disposition"]).replace('attachment; ','')
                name = name.replace('filename=','').replace('"','')
                return name
        else:
            import urllib
            urlfix = urllib.parse.unquote(url,encoding='utf-8', errors='replace')
            tokens = str(urlfix).split('/');
            return tokens[len(tokens)-1]
    except:
        import urllib
        urlfix = urllib.parse.unquote(url,encoding='utf-8', errors='replace')
        tokens = str(urlfix).split('/');
        return tokens[len(tokens)-1]
    return ''

def get_file_size(file):
    file_size = os.stat(file)
    return file_size.st_size

def createID(count=8):
    from random import randrange
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    id = ''
    i = 0
    while i<count:
        rnd = randrange(len(map))
        id+=map[rnd]
        i+=1
    return id