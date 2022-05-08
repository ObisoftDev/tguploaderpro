import requests
import json
import threading
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace
import time
import codecs
import uuid
import os

from .threads import ObigramThread
from pyobigram.utils import get_url_file_name,req_file_size

class Downloader(object):
    def __init__(self,filename='',dest=''):
        self.filename = filename
        self.dest = dest
        self.stoping = False
    def downloadFile(self,url='',progressfunc=None,args=None):
        req = requests.get(url, stream = True,allow_redirects=True)
        if req.status_code == 200:
            file_size = req_file_size(req)
            file_name = get_url_file_name(url,req)
            if self.filename!='':
                file_name = self.filename
            file_wr = open(self.dest+file_name,'wb')
            chunk_por = 0
            chunkrandom = 100
            total = file_size
            time_start = time.time()
            time_total = 0
            size_per_second = 0
            for chunk in req.iter_content(chunk_size = 1024):
                    if self.stoping:break
                    chunk_por += len(chunk)
                    size_per_second+=len(chunk);
                    tcurrent = time.time() - time_start
                    time_total += tcurrent
                    time_start = time.time()
                    if time_total>=1:
                        if progressfunc:
                            progressfunc(self,file_name,chunk_por,total,size_per_second,args)
                        time_total = 0
                        size_per_second = 0
                    file_wr.write(chunk)
            file_wr.close()
            return self.dest+file_name
        return self.dest+self.filename
    def stop(self):self.stoping=True


class ObigramClient(object):
    def __init__(self,token):
        self.token = token
        self.path = 'https://api.telegram.org/bot' + token + '/'
        self.files_path = 'https://api.telegram.org/file/bot' + token + '/'
        self.runing = False
        self.funcs = {}
        self.update_id = 0
        self.onmessage = None
        self.oninline = None
        self.SendFileTypes = {'document':'SendDocument','video':'SendVideo'}
        self.this_thread = None
        self.threads = {}

    def startNewThread(self,targetfunc=None,args=(),update=None):
        self.this_thread = ObigramThread(targetfunc=targetfunc,args=args,update=update)
        self.threads[self.this_thread.id] = self.this_thread
        self.this_thread.start()
        pass

    def parseUpdate(self,update):
        parse = str(update).replace('from','sender')
        parse = str(parse).replace('my_chat_member','message')
        return parse

    def run(self):
        self.runing = True
        while self.runing:
            try:
                getUpdateUrl = self.path + 'getUpdates?offset=' + str(self.update_id+1)
                update = requests.get(getUpdateUrl)
                update = self.parseUpdate(str(update.text))
                updates = json.loads(update, object_hook = lambda d : Namespace(**d)).result

                if len(updates) > 0:
                    self.update_id = updates[-1].update_id

                try:
                    for func in self.funcs:
                        for update in updates:
                                if func in update.message.text:
                                    self.startNewThread(self.funcs[func],(update,self),update)
                except:pass

                try:
                        for update in updates:
                            try:
                                if update.inline_query:
                                    if self.oninline:
                                        self.startNewThread(self.oninline,(update,self),update)
                                    break
                            except:
                                if self.onmessage:
                                    self.startNewThread(self.onmessage,(update,self),update)
                except Exception as ex:print(str(ex))

            except Exception as ex:
                print(str(ex))
            pass
        self.threads.clear()
        pass

    def sendMessage(self,chat_id=0,text='',parse_mode=''):
        try:
            text=text.replace('%', '%25')
            text=text.replace('#', '%23')
            text=text.replace('+', '%2B')
            text=text.replace('*', '%2A')
            text=text.replace('&', '%26')
            sendMessageUrl = self.path + 'sendMessage?chat_id=' + str(chat_id) + '&text=' + text + '&parse_mode=' + parse_mode
            result = requests.get(sendMessageUrl).text
            return json.loads(result, object_hook = lambda d : Namespace(**d)).result
        except:pass
        return None

    def deleteMessage(self,chat_id,msg_id):
        try:
            deleteMessageUrl = self.path + 'deleteMessage?chat_id='+str(chat_id)+'&message_id='+str(msg_id)
            result = requests.get(deleteMessageUrl).text
            return json.loads(result, object_hook = lambda d : Namespace(**d)).result
        except:pass
        return None

    def editMessageText(self,message,text='',parse_mode=''):
        if message:
            try:
                text=text.replace('%', '%25')
                text=text.replace('#', '%23')
                text=text.replace('+', '%2B')
                text=text.replace('*', '%2A')
                text=text.replace('&', '%26')
                editMessageUrl = self.path+'editMessageText?chat_id='+str(message.chat.id)+'&message_id='+str(message.message_id)+'&text=' + text + '&parse_mode=' + parse_mode
                result = requests.get(editMessageUrl).text
                parse = json.loads(result, object_hook = lambda d : Namespace(**d))
                sussesfull = False
                try: 
                    sussesfull = parse.ok and parse.result 
                    if sussesfull == False:
                         print('Warning EditMessage: '+str(parse.description))
                except: pass
                message.text = text
                return message
            except: pass
        return None


    def sendFile(self,chat_id,file,type='document'):
        sendDocumentUrl = self.path + self.SendFileTypes[type]
        of = codecs.open(file)
        payload_files = {type:(file,of)}
        payload_data = {'chat_id':chat_id}
        result = requests.post(sendDocumentUrl,files=payload_files,data=payload_data).text
        of.close()
        parse = json.loads(result, object_hook = lambda d : Namespace(**d))
        return parse.result

    def getFile(self,file_id):
        getFileUrl = self.path + 'getFile?file_id=' + str(file_id)
        result = requests.get(getFileUrl).text
        parse = json.loads(result, object_hook = lambda d : Namespace(**d)).result
        return parse

    def downloadFile(self,file_id=0,destname='',progressfunc=None,args=None):
        reqFile = self.getFile(file_id)
        downloadUrl = self.files_path + str(reqFile.file_path)
        req = requests.get(downloadUrl, stream = True,allow_redirects=True)
        if req.status_code == 200:
            file_wr = open(destname,'wb')
            chunk_por = 0
            chunkrandom = 100
            total = reqFile.file_size
            time_start = time.time()
            time_total = 0
            size_per_second = 0
            for chunk in req.iter_content(chunk_size = 1024):
                    chunk_por += len(chunk)
                    size_per_second+=len(chunk);
                    tcurrent = time.time() - time_start
                    time_total += tcurrent
                    time_start = time.time()
                    file_wr.write(chunk)
                    if time_total>=1:
                        if progressfunc:
                            progressfunc(destname,chunk_por,total,size_per_second,args)
                        time_total = 0
                        size_per_second = 0
            file_wr.close()
        return destname

    def answerInline(self,inline_query_id=0,result=[]):
        answerUrl = self.path + 'answerInlineQuery'
        payload = { 'inline_query_id' : inline_query_id,'results':result}
        result = requests.post(answerUrl,json=payload).text
        parse = json.loads(result, object_hook = lambda d : Namespace(**d))
        sussesfull = False
        try: 
            sussesfull = parse.ok and parse.result 
            if sussesfull == False:
                 print('Error InlineAnswer: '+str(parse.description))
        except: pass
        return sussesfull

    def on (self,name,func):self.funcs[name] = func
    def onMessage (self,func):self.onmessage = func
    def onInline(self,func):self.oninline = func


#Inline Queries
def inlineQueryResultArticle(id=0,title='',text='',description='',url='',hide_url=False,thumb_url='',thumb_width=10,thumb_height=10):
    return {'type':'article',
            'id':id,
            'title':title,
            'input_message_content':{'message_text':text,'description':description},
            'url':url,
            'hide_url':hide_url,
            'thumb_url':thumb_url,
            'thumb_width':thumb_width,
            'thumb_height':thumb_height}