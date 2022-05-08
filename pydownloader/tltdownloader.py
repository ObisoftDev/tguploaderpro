import time
import os
import re
import requests
from .utils import req_file_size,get_file_size,get_url_file_name,slugify,createID
from telethon import TelegramClient
import os



class TLTDownloader(object):
    def __init__(self,bot,ev):
        self.bot:TelegramClient = bot
        self.ev = ev
        self.id = createID(12)
        pass

    async def download(self,progressfunc=None,args=None):
        for chunk in self.bot.iter_download(self.ev.file,chunk_size=1024):
            print('download')
        pass